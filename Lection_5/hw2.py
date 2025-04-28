import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

""" # Пример данных
data = {
    'age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'spending_score': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Проверка данных
print(df.info())
print(df.head())

# Проверка типов данных и преобразование, если необходимо
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['spending_score'] = pd.to_numeric(df['spending_score'], errors='coerce')

# Проверка на наличие пропусков
print(df.isnull().sum())

# Построение линейного графика
plt.figure(figsize=(10, 6)) """

df=pd.read_csv('data.csv')

print(df.columns)
sns.lineplot(x='age', y='spending_score', data=df)

# Настройка оформления графика
plt.title('Age vc Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.grid(True)

# Сохранение графика в файл
plt.savefig('spending_score_vs_age.png')

# Вывод сообщения о том, что график сохранен
print("График сохранен в файл 'spending_score_vs_age.png'")
