positive = 0
negative = 0

while True:
    i = int(input("Entry the app's rating: "))
    if i == 0 or i < -100 or i > 100:
        break
    elif i > 0:
        positive +=1
    else:
        negative +=1

print(f"The number positive numbers = {positive}")
print(f"The number negative numbers = {negative}")