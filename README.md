# mlops_pracs 
Практические работы по предмету "Автоматизация машинного обучения"
## Участники команды
РИМ-13006 Томилов Максим, Шишкин Михаил, Нуртдинов Дмитрий, Степанова Элина 
### Module 1
<details>

- Необходимо из создать простейший конвейер для автоматизации работы с моделью машинного обучения.
- Отдельные этапы конвейера машинного обучения описываются в разных python–скриптах, которые потом соединяются в единую цепочку действий с помощью bash-скрипта.
- Все файлы необходимо разместить в подкаталоге lab1 корневого каталога
  
Этапы:

1. Создаем python-скрипт (data_creation.py), который создает различные наборы данных, описывающие некий процесс (например, изменение дневной температуры). Таких наборов несколько, в некоторые данные можно включить аномалии или шумы. Часть наборов данных должны быть сохранены в папке “train”, другая часть в папке “test”. Одним из вариантов выполнения этого этапа может быть скачивание набора данных из сети, и разделение выборки на тестовую и обучающую. Учтите, что файл должен быть доступен и методы скачивания либо есть в ubuntu либо устанавливаются через pip в файле pipeline.sh
   
2. Создаем python-скрипт (data_preprocessing.py), который выполняет предобработку данных, например, с помощью sklearn.preprocessing.StandardScaler. Трансформации выполняются и над тестовой и над обучающей выборкой.
   
3. Создаем python-скрипт (model_preparation.py), который создает и обучает модель машинного обучения на построенных данных из папки “train”. Для сохранения модели в файл можно воспользоваться [pickle](https://docs.python.org/3/library/pickle.html) (см. пример)

4. Создаем python-скрипт (model_testing.py), проверяющий модель машинного обучения на построенных данных из папки “test”.

5. Пишем bash-скрипт (pipeline.sh), последовательно запускающий все python-скрипты. При необходимости усложните скрипт. В результате выполнения скрипта на терминал в стандартный поток вывода печатается одна строка с оценкой метрики на вашей модели, например:


#### Как запустить?

<details>

#### Использование
Для того чтобы запустить данный pipeline необходимо:
1. Клонировать данный репозиторий на ПК или ВМ (с ОС Linux)
2. Сделать файл **pipeline.sh** исполняемым, выполнив в терминале в каталоге с файлами проекта команду
```
chmod +x pipeline.sh
```
3. Запустить bash-скрипт **pipeline.sh**, выполнив в терминале в каталоге с файлами проекта любую из представленных команд:
```
./pipeline.sh
```

</details>
</details>

### Module 2
<details>

* Вам нужно разработать собственный конвейер автоматизации для проекта машинного обучения. Для этого вам понадобится виртуальная машина с установленным Jenkins, python и необходимыми библиотеками. В ходе выполнения практического задания вам необходимо автоматизировать сбор данных, подготовку датасета, обучение модели и работу модели.  

Этапы задания 
1. Развернуть сервер с Jenkins, установить необходимое программное обеспечение для работы над созданием модели машинного обучения.
2. Выбрать способ получения данных (скачать из github, из Интернета, wget, SQL запрос, …). 
3. Провести обработку данных, выделить важные признаки, сформировать датасеты для тренировки и тестирования модели, сохранить.
4. Создать и обучить на тренировочном датасете модель машинного обучения, сохранить в pickle или аналогичном формате. !
5. Загрузить сохраненную модель на ​предыдущем этапе и проанализировать ее качество на тестовых данных. 
</details>

### Module 3
<details>
