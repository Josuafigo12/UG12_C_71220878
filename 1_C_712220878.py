kalimat_atau_kata = input("masukan kata atau kalimat :")
def reserve (kalimat_atau_kata):
    str= ""
    for i in kalimat_atau_kata:
        str = i + str
    return str
print(reserve(kalimat_atau_kata))

