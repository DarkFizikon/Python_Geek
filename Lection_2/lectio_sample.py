list_1 = [] #Создание пустого списка. Список упорядоченный конечный набор элементов

list_2 = list() #Создание пустого списка. В списках существет нумерация, работают как массивы.

print(*list_1) #Вывод списка без использования квадртаных скобок! * убирает квадратные скобки

for i in list_1:
    print(list[i]) # Пройтись по каждому элементу списка
print(list[1]) # Печать определенного элемента из спска

list_1.append(8) #Добавление в конец списка необходимого элемента

print(list_1.pop()) #Удаление последнего элемента и возвращает его на выводе, напрмер можно записать a = list_1.pop(). Также можно указать значение элемента, которое удалиться ставим номер в скобках

print(list_1.insert(2,11)) # Добавление элемента в спсиок. В данном примере вставляется число 11, на второй элемент, все значения после 2-го элемента сдвигаются правее

t = () #Создание пустого кортежа. Кортеж - неизменяемый список, имеет класс tuple. Кортеж работает быстрее списка
t = (1, ) #Создание кортежа зо значение tuple, необходимо после значения указать запятую
v = [1,2,3]
t = tuple(v) #Преобраование списка в кортеж

a, b = 1, 2 #Множественное присваивание
a, b, c = v
print(a,b,c) #Распаковка кортежа. Из кортежа можно выводить элементы как и из списков

for i in range(len(t)):
    print(t[i]) #Вывод каждого элемента кортежа отдельно, также работает и со списками

dictionary = {} #Создание пустого словаря. Словарь - неупорядоченная коллекция произвольных объектов с доступом по ключу
d = dict() #Также создание пустого словаря
d['q'] = 'qwerty' #В словарь d Создаем ключ, по которому кладется занчение qwerty. На выводе увидим {'q' : 'qwerty'}
d['w'] = 'werty' #На выводе увидим - {'q' : 'qwerty', 'w' : 'werty'}
print(d['q']) # На выводе получим qwerty
del d['w'] #удаление элемента
for item in d:
    print('{} : {}'.format(item, d[item])) #item - это ключи и обращение к ключам. на выводе увидим ключ и через двоеточие значение, которое принадлежит даному ключу

for (k,v) in d.items():
    print(k, v) #на выводе опят же на выводе увидим ключи и их значение. dicrionary.items() - это обращение по ключу к значениеям

colors = {'red', 'green', 'blue'} #Задание множества. Множества содержат в себе ууникальные элементы, которые не обязательно упорядоченны
colors.add('gray') #Добавление в множество нового элемента, которого нет, но если есть значение, то оно не добавиться!
colors.remove('red') #Удаление из множества значения
colors.discard('red') # Удаление значения с проверкой, если есть удаляет, если нет. то пропускает
colors.clear() #Удаление всех элементов из множества
q = set() #Создание пустого множества

#Опреации с множетсвами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} - копирование
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, - объединение множества
i = a.intersection(b) # i = {8, 2, 5} - пересечение множества
dl = a.difference(b) # dl = {1, 3} - разность множеств
dr = b.difference(a) # dr = {13, 21} - также разность множества
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} сначала находится пересечение a и b. А затем действия выполняются по порядку
d = frozenset(c) #Замороженное множество, которое нельзяизменить. То есть если мы не хотим изменять множество - задаем его таким образом

#List compression примеры
#Пример 1
list_1 = []
for i in range(1,101):
    list_1.append(i)
#Эту же функци можно задат следующим образом:
list_1 = [i for i in range(1,101)]
list_1 = [i for i in range(1,101) if i%2 == 0] #Задаем в спсиок только четные цифры
list_1 = [(i,i) for i in range(1,101) if i%2 == 0] #Создание пары каждому из чисел(кортежи)
list_1 = [i*2 for i in range(10) if i%2 == 0] #Арифметические действия в лист компрешн