import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

""" # Пример данных
data = {
    'salary': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000],
    'bonus': [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000],
    'years_at_company': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Создание DataFrame
df = pd.DataFrame(data) """

df = pd.read_csv('data.csv')

# Проверка данных на наличие пропусков
print(df.isnull().sum())

# Удаление строк с пропущенными значениями, если они есть
df = df.dropna(subset=['salary', 'bonus', 'years_at_company'])

# Построение точечного графика
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=df,
    x='salary',
    y='bonus',
    size='years_at_company',
    sizes=(40, 400),  # Настройка размера точек
    legend=False  # Отключение легенды, так как она не нужна
)

# Настройка оформления графика
plt.title('Взаимосвязь между зарплатой и бонусами')
plt.xlabel('Зарплата')
plt.ylabel('Бонусы')
plt.grid(True)

# Сохранение графика в файл
plt.savefig('salary_vs_bonus.png')

# Вывод сообщения о том, что график сохранен
print("График сохранен в файл 'salary_vs_bonus.png'")

# Отображение графика
plt.show()
