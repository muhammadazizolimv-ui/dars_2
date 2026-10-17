raqamlar = list(map(int, input("Sonlarni kiriting (bo'sh joy bilan): ").split()))

yangi_royaat = []
korilgan = set()

for a in raqamlar:
    if a not in korilgan:
        yangi_royaat.append(a)
        korilgan.add(a)

print("Takrorlarsiz ro'yaat:", yangi_royaat)
