import random
import pandas as pd

# Создание списка с значениями 'robot' и 'human'
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создание DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений в столбце 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание нового DataFrame для one-hot кодирования
one_hot_df = pd.DataFrame()

# Создание бинарных столбцов для каждого уникального значения
for value in unique_values:
    one_hot_df[value] = (data['whoAmI'] == value).astype(int)

# Объединение one-hot DataFrame с исходным DataFrame
result_df = pd.concat([data, one_hot_df], axis=1)

# Вывод первых строк результата
result_df.head()