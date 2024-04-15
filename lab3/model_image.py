import streamlit as st 
import requests 
from PIL import Image 
from transformers import BlipProcessor, BlipForConditionalGeneration 
import concurrent.futures 
 
 
@st.cache(allow_output_mutation=True) 
def load_model(): 
    return BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base") 
 
@st.cache(allow_output_mutation=True) 
def load_processor(): 
    return BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base") 
 
def process_image(image): 
    inputs = processor(image, return_tensors="pt") 
    out = model.generate(**inputs) 
    caption = processor.decode(out[0], skip_special_tokens=True) 
    return caption 
 
model = load_model() 
processor = load_processor() 
 
 
st.title("Blip Image Captioning") 
img_url = st.text_input("Введите URL изображения:") 
result = st.button('Распознать изображение') 
if img_url: 
    try: 
        with st.spinner("Загрузка изображения..."): 
            raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB") 
 
        caption = None 
        with concurrent.futures.ThreadPoolExecutor() as executor: 
            future = executor.submit(process_image, raw_image) 
            caption = future.result() 
 
        st.image(raw_image, caption=f"Исходное изображение: {img_url}") 
        st.text(f"Описание: {caption}") 
    except: 
        st.error("Ошибка при загрузке или обработке изображения.")
