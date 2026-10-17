sonlar = [-3, 0, 7, -1, 5, 0, -8]

musbat = []
manfiy = []
nol = []

for a in sonlar:
    if a > 0:
        musbat.append(a)
    elif a < 0:
        manfiy.append(a)
    else:
        nol.append(a)

print("Musbat sonlar:", musbat)
print("Manfiy sonlar:", manfiy)
print("Nol sonlar:", nol)