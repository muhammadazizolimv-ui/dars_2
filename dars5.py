matn = input("Matn kiriting: ")
soni = {}

for belgi in matn:
    if belgi in soni:
        soni[belgi] += 1
    else:
        soni[belgi] = 1

for belgi, son in soni.items():