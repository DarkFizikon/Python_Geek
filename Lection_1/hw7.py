n = 8
i = 1
sum_tusk = 0
sum_call = 0
print("The working day has start")
while i <= n:
    task = int(input(f"How much tusks solution Maks in {i} hours: "))
    sum_tusk += task
    call = int(input("Wife is calling. Pick up the phone? (0 - no; 1 - yes): "))
    sum_call += call
    i += 1

print(f"The working day is over. Total tasks completed = {sum_tusk}")
if sum_call > 0:
    print("He need to go to the store")