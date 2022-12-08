angka = input ("masukan angka :")
dihitung = input ("masukan angka yang ingin dihitung :")

sum = 0
for each in angka:
    if each == dihitung:
        sum = sum + 1

print ("angka",dihitung,"muncul sebanyak",sum,"kali")
