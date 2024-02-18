                                                                                             #Capstone Project   : Module 1
                                                                                             #Case Study         : Data Karyawan Perusahaan
                                                                                             #Nama               : Christin Widiana
                                                                                             #Kelas              : JCDSOL-013-2-Online

#Data Daftar Karyawan PT.ABC -> menggunakan list of dictionary 

daftar_karyawan = [
    {'ID' : 'ABC001',
     'Nama' : 'Della',
     'Gender' : 'Perempuan',
     'Alamat' : 'Dago',
     'Email' : 'della@gmail.com',
     'Jabatan' : 'Staff',
     },
    {'ID' : 'ABC002',
     'Nama' : 'Galih',
     'Gender' : 'Laki-laki',
     'Alamat' : 'Cibaduyut',
     'Email' : 'galih@gmail.com',
     'Jabatan' : 'SPV',
     },
    {'ID' : 'ABC003',
     'Nama' : 'Erni',
     'Gender' : 'Perempuan',
     'Alamat' : 'Buah Batu',
     'Email' : 'erni@gmail.com',
     'Jabatan' : 'Manager',
     },
]

#function untuk menampilkan data karyawan secara keseluruhan
def tampilkan_data_karyawan (daftar_karyawan):
    print ('Daftar Data Karyawan PT.ABC') #judul tabel

    #cetak bagian header tabel
    print (f"{'ID':<8} | {'Nama':<10} | {'Gender':<10} | {'Alamat':<20} | {'Email' :<20} | {'Jabatan':<10}")
    print ("_" *95)

    #cetak bagian isi tabel
    for karyawan in (daftar_karyawan):
        print(f"{karyawan['ID']:<8} | {karyawan['Nama']:<10} | {karyawan['Gender']:<10} | {karyawan['Alamat']:<20} | {karyawan['Email'] :<20} | {karyawan['Jabatan']:<10}")

#function untuk mencari data karyawan dengan menggunakan ID Karyawan tertentu 
def cari_karyawan(daftar_karyawan,cari_id): #fungsi cari_karyawan dng menggunakan 2 parameter yt daftar_karyawan & cari_id
    for karyawan in daftar_karyawan: #akan ditelusuri apakan id yg dicari terdapat pada daftar karyawan
        if karyawan['ID']== cari_id:
            return karyawan #mengembalikan nilai ke karyawan apabila data yang dicari ditemukan
    return None #mengembalikan nilai kosong jika data yang dicari tidak ditemukan
    
#function untuk menampilkan data karyawan berhasil ditemukan
def data_berhasil_ditemukan (hasil_cari):
    if hasil_cari:
        print ("Data karyawan berhasil ditemukan")
        #cetak bagian header tabel
        print (f"{'ID':<8} | {'Nama':<10} | {'Gender':<10} | {'Alamat':<20} | {'Email':<20} | {'Jabatan':<10}")
        print ("_" *95)
        #cetak bagian isi tabel
        #for karyawan in (daftar_karyawan):
        print(f"{hasil_cari['ID']:<8} | {hasil_cari['Nama']:<10} | {hasil_cari['Gender']:<10} | {hasil_cari['Alamat']:<20} | {hasil_cari['Email']:<20} | {hasil_cari['Jabatan']:<10}")
    else:
        print(" ID karyawan tidak ditemukan")

#sub menu 1 menampilkan tabel data karyawan
def sub_menu1():
    while True:
        print(''' 
_______________________________________________________________________________________________
Sub Menu Menampilkan Data Karyawan PT.ABC:
1. Tampilkan Data Karyawan
2. Mencari Data Karyawan
3. Kembali Ke Main Menu
_______________________________________________________________________________________________
''')
        pilihan_submenu1 = input('Silakan pilih menu yang akan dijalankan [1-3] : ')
        if pilihan_submenu1 == '1': #menu untuk menampilkan keseluruhan data karyawan yang ada
            tampilkan_data_karyawan (daftar_karyawan)
        elif pilihan_submenu1 == '2': #untuk menampilkan data karyawan secara spesifik berdasarkan id karyawan yang ingin ditampilkan
            if len(daftar_karyawan) == 0: #jika kondisi data karyawan kosong
                print('Data karyawan tidak ditemukan')
            else:
                tampilkan_data_karyawan(daftar_karyawan)
                id_karyawan =input('Silakan input ID Karyawan yang dicari [ex : ABC001] : ')
                hasil_cari = cari_karyawan (daftar_karyawan,id_karyawan)
                data_berhasil_ditemukan (hasil_cari)
       
        elif pilihan_submenu1 == '3':
            break #keluar dr loop dan kembali ke main menu
        else:
            print('Silakan pilih menu dari 1-3')

#function untuk menambah data karyawan baru
def tambah_karyawan(daftar_karyawan):
    while True :
        id_baru=input('Masukkan ID Karyawan Baru [ABC001]: ') # meminta input dari user untuk memasukkan id karyawan baru sebanyak 6 digit
        
        #cek apakah id yang diinput memenuhi syarat 6 digit
        if(len(id_baru)!=6):
           print('ID Karyawan Wajib 6 Digit. Silakan coba input ID baru')
           continue #skip prose lain didalam loop lsg minta ID baru

        #cek apakah ada duplikasi ID
        if any (karyawan['ID'] == id_baru for karyawan in daftar_karyawan):
           print('ID tersebut sudah terpakai. Silakan coba input ID lain')
           continue #skip proses lain didalam loop lsg minta ID baru

        #jika ID sudah memenuhi syarat (dipastikan sudah 6 digit dan tdk ada duplikasi) maka lanjut keproses input data lainnya
        nama = input ('Input Nama Karyawan Baru :').capitalize()
        gender = input ('Input Gender Karyawan Baru [Perempuan / Laki-laki] : ').capitalize()
        alamat = input ('Input Alamat Karyawan Baru : ').capitalize()
        email = input ('Input Email Karyawan Baru : ')
        jabatan = input ('Input Jabatan Karyawan Baru : ').capitalize()

        konfirmasi = input ('Apakah data akan disimpan [Y/N] : ').capitalize()

        if konfirmasi=='Y' :
            # Data karyawan baru tersebut akan digabungkan menjadi sebuah dictionary
            data_baru={
                'ID':id_baru,
                'Nama':nama,
                'Gender':gender,
                'Alamat':alamat,
                'Email':email,
                'Jabatan':jabatan
            }

            #menambahkan data tersebut kedalam list
            daftar_karyawan.append(data_baru)
            print ('Data karyawan berhasil ditambahkan')
            break #keluar dari loop setelah berhasil menambahkan data karyawann baru
        else:
            print ('Data baru tidak jadi disimpan. Silakan input data baru kembali.')

#function update data karyawan
def update_karyawan (daftar_karyawan):
    while True:
        id_karyawan = input ('Input ID karyawan yang akan diupate : ')

        #mencari data karyawan berdasarkan ID yang diinput
        #keluarkan nilai none jika tidak ditemukan
        karyawan = next((k for k in daftar_karyawan if k['ID']==id_karyawan),None)

        if not karyawan :
            print('ID karyawan tersebut tidak ditemukan')
            continue #skip proses lainnya yang dan meminta user input ID karyawan lagi
        else:
            break #keluar dari loop jika data ditemukan
    while True:
        print('Silakan pilih data yang akan diupdate : ID,Nama,Gender,Alamat,Email atau Jabatan')
        key = input ('Input atribut yang akan diupdate : ')

        #cek apakah atribut yang diinput bener
        if key not in karyawan :
            print(f"Atribut '{key}' tidak ditemukan")
            continue #skip proses lainnya dan meminta masukkan atribut kembali
        else :
            break #keluar dari loop jika atribut benar

    #minta data baru untuk atribut tersebut
    nilai_baru = input(f"Input data baru untuk {key} :")

    #update data
    karyawan [key] = nilai_baru
    print(f'Data {key} sudah diupdate menjadi {nilai_baru}')

# Function untuk menghapus data
def hapus_karyawan(daftar_karyawan):
    while True:
        id_karyawan=input('Masukkan ID Karyawan yang akan dihapus : ')
        karyawan_ditemukan=False
        
        # Cari data karyawan
        for i,karyawan in enumerate(daftar_karyawan) :
            if karyawan['ID']==id_karyawan :
                karyawan_ditemukan=True
                # ID karyawan berhasil ditemukan
                # Meminta konfirmasi penghapusan ke user
                konfirmasi=input(f"Apakah Anda yakin ingin menghapus data karyawan {id_karyawan} [Y/N]: ").capitalize()
                
                if konfirmasi=='Y':
                    del daftar_karyawan[i]
                    print(f"Data karyawan dengan ID {id_karyawan} telah dihapus")
                    return # keluar dari function setelah menghapus data
                else :
                    print("Penghapusan data dibatalkan")
                    break # keluar dari loop for
            
        # Bila ID tidak ditemukan/ salahh input maka akan menanyakan kembali ke user apakah ingin mencoba lagi atau tidak
        if not karyawan_ditemukan:
            print ("Karyawan dengan ID tersebut tidak ditemukan")
        pilihan = input("Apakah Anda ingin mencoba lagi [Y/N]: ").capitalize()
        if pilihan!='Y' :
            print("Penghapusan data dibatalkan")
            return # keluar dari function
        
#main menu
def main_menu () :
    while True:
        print(''' 
_______________________________________________________________________________________________
Main Menu Menampilkan Data Karyawan PT.ABC:
1. Tampilkan Data Karyawan
2. Menambahkan Data Karyawan
3. Mengubah Data Karyawan
4. Menghapus Data Karyawan
5. Exit
_______________________________________________________________________________________________
''')
        #select main menu
        select_menu = input ('Silakan pilihan menu yang akan dijalankan [1-5] : ')
        if select_menu == '1':
            sub_menu1()
        elif select_menu == '2':
            tambah_karyawan(daftar_karyawan)
        elif select_menu == '3':
            update_karyawan(daftar_karyawan)
        elif select_menu == '4':
            hapus_karyawan(daftar_karyawan)
        elif select_menu == '5' :
            print('Terima kasih, sampai jumpa kembali')
            break #untuk keluar dari loop
        else :
            print('Menu yang dipilih tidak valid, silakan pilih lagi')

main_menu()


