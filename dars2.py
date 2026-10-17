input = input("Sonlarni kiriting: ")
juft = []
toq = []

for son in input.split():
    son = int(son)
    if son % 2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")

