boy = int(input("Enter the number of boys: "))
girl = int(input("Enter the number of girls: "))
answer = ''

if boy / girl > 2 or (girl / boy > 2):
    print("No solution for this stuation")
elif boy >= girl:
    k = boy - girl
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girl - k):
        answer += 'BG'
else:
    k = girl - boy
    for gbg in range(k):
        answer += 'GBG'
    for gb in range (boy - k):
        answer += 'GB'

print(f"Seats like this: {answer}")