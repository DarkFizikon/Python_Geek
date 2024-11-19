#Функция Фибоначчи
print('Выводит значение числа Фибоначчи о указанному порядковому номеру')
def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n-1) + f(n-2)

n = int(input())

print(f(n-2))

#Замена минимальных оценок на мксимальные
print('Меняем максимальное число в списке на минимальное')
n = int(input())

list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)


max_n = max(list1)
min_n = min(list1)

for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n

print(list1)

#Функция, которая проверяет простое ли число?

print('Введенное число простое?')

def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False

        i +=1

        if flag:
            return 'Yes'
        else:
            return 'No'

n = int(input())      
print(prime(n))

#Вывод чисел в обратном порядке
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n-1) + f'{k}'

n = int(input())
print(f(n))