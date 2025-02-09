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