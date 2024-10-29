films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
my_list = []

n = int(input("How much films you want add: "))

for i in range(n):
    name = input("Enter the film name:")
    if name in films:
        my_list.append(name)
    else:
        print(f"Error! Film {name} doesn't exist!")

print(f"\nYour list of favorite movies: {my_list}")
