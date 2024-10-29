n = int(input("Enter list size: "))
list = []
for i in range(n):
    number = int(input())
    list.append(number)

print(f"Unsort list: {list}")

for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(f"Sort list: {list}")