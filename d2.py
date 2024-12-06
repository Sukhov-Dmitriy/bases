import numpy as np
import pandas as pd

# Установка параметров отображения для более удобного просмотра данных
pd.set_option('display.max_columns', 13)  # Максимальное количество столбцов для отображения
pd.set_option('display.max_rows', 10)      # Максимальное количество строк для отображения
pd.set_option('display.max_colwidth', 45)  # Максимальная ширина столбца
pd.set_option('display.width', 80)          # Ширина отображения

# Загрузка обучающего набора данных из CSV файла и указание, что 'house_id' будет использоваться в качестве индекса
data = pd.read_csv('houses.csv', index_col='house_id')

# Загрузка тестового набора данных из CSV файла с тем же индексом
data_test = pd.read_csv('houses_test.csv', index_col='house_id')

# Здесь необходимо дописать код для очистки данных и подготовки модели
# 1. Удаление строк с пропущенными значениями
data_cleaned = data.dropna()
data_test_cleaned = data_test.dropna()

# 2. Удаление зависимых признаков (например, с высокой корреляцией)
correlation_matrix = data_cleaned.corr()

# Установка порога корреляции для выявления зависимых признаков
threshold = 0.9
to_drop = []  # Список для хранения имен зависимых признаков

# Цикл для проверки каждой пары признаков на корреляцию
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        # Если корреляция превышает установленный порог
        if abs(correlation_matrix.iloc[i, j]) > threshold:
            colname = correlation_matrix.columns[i]  # имя текущего столбца
            if colname not in to_drop:  # Проверка, не добавлялся ли уже столбец в список
                to_drop.append(colname)

# Удаление зависимых признаков из очищенной таблицы
data_cleaned.drop(columns=to_drop, inplace=True)

# 3. Определение целевой переменной (цена дома) и признаков для обучения модели
y = data_cleaned['SalePrice']  # Целевая переменная
X = data_cleaned.drop(columns=['SalePrice'])  # Все остальные столбцы, кроме целевой переменной

# 4. Делим данные на обучающую и тестовую выборки, чтобы избежать переобучения
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Обучаем модель линейной регрессии
from sklearn.linear_model import LinearRegression

model = LinearRegression()  # Создаем объект модели
model.fit(X_train, y_train)  # Обучаем модель на обучающей выборке

# 6. Прогнозирование на тестовом наборе данных
y_pred_test = model.predict(data_test_cleaned)

# Загрузка ответов из файла с истинными значениями
answer = pd.read_csv('answer.csv', index_col='house_id')

# Импорт необходимых метрик для оценки качества модели
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# Оценка качества модели с использованием MAPE и RMSE
print('MAPE: ', mean_absolute_percentage_error(answer.values, y_pred_test))  # Вывод средней абсолютной процентной ошибки
print('MSE: ', mean_squared_error(answer.values, y_pred_test)**0.5)  # Вывод корня из среднеквадратичной ошибки