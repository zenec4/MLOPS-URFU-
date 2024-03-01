#!/bin/bash

# Создание виртуальной среды
python3 -m venv myenv

# Активация виртуальной среды
source myenv/bin/activate

# Установка библиотек из файла requirements.txt
pip install -r requirements.txt

# Функция для деактивации виртуальной среды
function deactivate_venv {
    deactivate
}

# Установка обработчика на сигналы завершения работы скрипта
trap deactivate_venv EXIT

# Запуск скрипта data_creation.py
python data_creation.py || { echo "Ошибка при выполнении скрипта data_creation.py"; exit 1; }

# Запуск скрипта model_preprocessing.py
python model_preprocessing.py || { echo "Ошибка при выполнении скрипта model_preprocessing.py"; exit 1; }

# Запуск скрипта model_preparation.py
python model_preparation.py || { echo "Ошибка при выполнении скрипта model_preparation.py"; exit 1; }

# Запуск скрипта model_testing.py
python model_testing.py || { echo "Ошибка при выполнении скрипта model_testing.py"; exit 1; }

# Если скрипты дошли до этой точки, значит, они успешно выполнены
echo "Все скрипты успешно выполнены"
