num = int(input('Entry ticket number: '))

if num//100000 >=1 and num//100000<=9:
    firstpart = num//1000
    secondpart = num%1000
    sum1 = sum2 = 0
    while firstpart > 0:
        sum1 += firstpart % 10
        firstpart //= 10
    print(f"Sum of first 3 numbers {sum1}")
    while secondpart > 0:
        sum2 += secondpart % 10
        secondpart //= 10
    print(f"Sum of last 3 numbers {sum2}")
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
else:
    print("Wrong entry!")        