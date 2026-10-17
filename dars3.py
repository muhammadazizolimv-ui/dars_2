matn = input("Matn kiriting: ")

belgilar_soni = len(matn)
sozlar = matn.split()
sozlar_soni = len(sozlar)
boshlik_soni = matn.count(" ")

print(f"Belgilar soni: {belgilar_soni}")
print(f"So'zlar soni: {sozlar_soni}")
print(f"Bo'sh joylar soni: {boshlik_soni}")
