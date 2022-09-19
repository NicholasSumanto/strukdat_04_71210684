import json

with open('mahasiswa.json', 'r+') as datafile:
    data = json.load(datafile)
    orang = int(input("Masukkan jumlah mahasiswa baru :"))
    for i in (0,orang):
        nama = input("Masukkan nama Anda:")
        jumlah_hobi = (input("Masukkan Jumlah hobi :"))
        count = 1
        daftar_hobi = list()
        for j in (0,jumlah_hobi):
            hobi = input("Masukkan Hobi ke-"+str(count)+":")
            count += 1
        daftar_hobi.append(hobi)
        prestasi = input('Masukkan Prestasi Anda:')
        data = {nama:[]}
        biodata = list() 
        biodata.append({'Hobi': daftar_hobi}) 
        biodata.append({'Prestasi':prestasi}) 
        data[nama].append({'Biodata':biodata}) 
        print("=== Data berhasil ditambahkan ===\n")

