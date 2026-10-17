soz = input("Soz kiriting: ")

for harf in soz:
    if soz == soz[::-1]:
        print(f"{soz} palindrom so'z")
    else:
        print(f"{harf} undosh harf")