n = 8
i = 1
sum_tusk = 0
go_to_store = False
print("The working day has start")
while i <= n:
    task = int(input(f"How much tusks solution Maks in {i} hours: "))
    sum_tusk += task
    call = int(input("Wife is calling. Pick up the phone? (0 - no; 1 - yes): "))
    if call == 1:
        go_to_store = True
    i +=1

print(f"The working day is over. Total tasks completed = {sum_tusk}")
if go_to_store:
    print("He need to go to the store")