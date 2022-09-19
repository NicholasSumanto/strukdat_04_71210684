import json

with open('mahasiswa.json', 'r') as datafile:
    data = json.load(datafile)

    mahasiswa = int(input("Masukan jumlah mahasiswa baru : "))

    for i in range(0, mahasiswa):
       
        nama = input("Masukan nama Anda : ")
        daftar = []
        dict = {}
        jml_hobi = int(input("Masukan Jumlah hobi : "))
        daftar_hobi = []
        for j in range(1, jml_hobi+1):
            hobi = input("Masukan Hobi ke-{index} : ".format(index=j))
            daftar_hobi.append(hobi)

        prestasi = input("Masukan Prestasi Anda : ")

        list.append({"BioData":{"Hobi":daftar_hobi,"Prestasi":prestasi}})
        data[nama] = daftar

        print("=== Data berhasil ditambahkan ===")
        print()

#tambahkan data ke json
with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)


