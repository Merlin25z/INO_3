import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('car_data.csv')

# Диаграмма box plot: цена от типа кузова
plt.figure(figsize=(10, 6))
sns.boxplot(x='Body Style', y='Price ($)', data=df)
plt.title('Зависимость цены от типа кузова')
plt.xlabel('Тип кузова')
plt.ylabel('Цена ($)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Annual Income', y='Price ($)', hue='Gender', data=df)
plt.title('Скорректированный график рассеяния: доход vs цена')
plt.xlabel('Годовой доход')
plt.ylabel('Цена ($)')
plt.show()


plt.figure(figsize=(10, 6))
sns.countplot(x='Body Style', hue='Dealer_Region', data=df)
plt.title('Распределение типов кузова по регионам дилеров')
plt.xlabel('Тип кузова')
plt.ylabel('Количество')
plt.xticks(rotation=45)
plt.show()
