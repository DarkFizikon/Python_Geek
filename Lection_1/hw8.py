n = int(input("Make a number: "))
count = 0

while True:
    m = int(input("Entry a number: "))
    count += 1
    if m == n:
        print(f"Good job! Attempts: {count}")
        break
    elif m > n:
        print("The number more than need. Try again!")       
    else:
        print("The number less than need. Try again!")
        