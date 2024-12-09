import pandas as pd

# Загрузка данных
data = pd.read_csv('data/dst-3.0_16_1_hh_database.csv', sep=';')

# Функция для определения категории образования
def categorize_education(education_str):
    # Разделяем строку на слова
    words = education_str.split()
    
    # Проверяем первые три слова
    if len(words) >= 3:
        if words[0] == 'Высшее':
            return 'высшее'
        elif words[0] == 'Неоконченное' and words[1] == 'высшее':
            return 'неоконченное высшее'
        elif words[0] == 'Среднее' and words[1] == 'специальное':
            return 'среднее специальное'
        elif words[0] == 'Среднее':
            return 'среднее'
    
    return None  # Если категория не распознана

# Применяем функцию к столбцу "Образование и ВУЗ"
data['Образование'] = data['Образование и ВУЗ'].apply(categorize_education)

# Проверяем уникальные категории образования
print(data['Образование'].unique())

# Считаем количество соискателей со средним уровнем образования
average_education_count = data[data['Образование'] == 'среднее'].shape[0]
print(f'Количество соискателей со средним уровнем образования: {average_education_count}')