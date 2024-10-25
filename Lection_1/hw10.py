n = int(input("Enter the number of cards: "))
total_sum = 0

for i in range(1,n+1):
    total_sum +=i
        
for i in range(1,n):
    number = int(input(f"Enter card number from 1 to {n}: "))
    total_sum -= number

print(f"Lost card number is {total_sum}")