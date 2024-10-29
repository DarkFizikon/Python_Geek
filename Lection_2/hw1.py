n = int(input("Enter the number of video cards: "))
mods = []
max = 0

for i in range(n):
    mod = int(input(f"Video card {i+1}: "))
    mods.append(mod)
    if mods[i]>max:
        max = mods[i]
print(mods)

while max in mods:
    mods.remove(max)

print(mods)