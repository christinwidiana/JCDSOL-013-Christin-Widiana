
#Capstone Project   : Module 1
#Case Study         : Data Karyawan Perusahaan
#Nama               : Christin Widiana
#Kelas              : JCDSOL-013-2-Online

import os
import colorama
from colorama import init, Fore,Back,Style
from tabulate import tabulate

# Inisialisasi colorama
init(autoreset=True)

# Untuk membersihkan layar
os.system('cls')

# Inisialisasi daftar_karyawan  - dengan membuat list kosong
daftar_karyawan = []

# Function untuk menampilkan data karyawan secara keseluruhan
def tampilkan_data_karyawan (daftar_karyawan):
    # Cek jika daftar karyawan kosong
    if not daftar_karyawan :
        print(Fore.RED +'Daftar karyawan kosong.')
        return # keluar dari fungsi
    
    # Jika daftar karyawan tidak kosong
    print (Back.BLUE +'Daftar Data Karyawan PT.ABC') #judul tabel

    # Menampung header dari kunci data karyawan
    headers=daftar_karyawan[0].keys()

    # Menampung semua nilai dari data karyawan
    data=[karyawan.values() for karyawan in daftar_karyawan]

    # Menampilkan tabel data karyawan dengan menggunakan format grid
    print(tabulate(data, headers=headers, tablefmt="grid"))

# Fungsi untuk menampilkan data key tertentu
def tampilkan_data_key_tertentu(daftar_karyawan):
    # Cek jika daftar karyawan kosong
    if not daftar_karyawan: 
        print(Fore.RED + "Daftar karyawan kosong.")
        return
    
# Jika isi tidak kosong, maka akan meminta input key
    while True:
        # Meminta user memasukkan key yang diinginkan
        key_dipilih = input("Masukkan key data karyawan yang ingin ditampilkan (ID, Nama, Gender, Alamat, Email, Jabatan)' \n atau ketik 'Batal' untuk membatalkan: ").capitalize()
        
        # Jika user memilih opsi untuk membatalkan
        if key_dipilih == 'Batal':
            print(Fore.RED + "Operasi dibatalkan.")
            return
        
        # Memeriksa apakah key ada di daftar_karyawan
        if key_dipilih in daftar_karyawan[0]:

            # Mengumpulkan data berdasarkan key yang dipilih
            data = [[karyawan.get(key_dipilih, "N/A")] for karyawan in daftar_karyawan]
            
            # Menampilkan data karyawan dengan tabulate
            print(tabulate(data, headers=[key_dipilih], tablefmt="grid"))
            break
        else:
            print(Fore.RED + "Key yang dimasukkan tidak valid.\nSilakan coba lagi atau ketik 'Batal' untuk membatalkan.")

# Function untuk menampilkan data karyawan berdasarkan filter yang dipilih
def filter_data_karyawan(daftar_karyawan):
    # Cek jika daftar karyawan kosong
    if not daftar_karyawan:
        print(Fore.RED +"Daftar karyawan kosong.")
        return
    
  
    while True:
        key_dipilih = input("Masukkan key data karyawan yang ingin ditampilkan (ID, Nama, Gender, Alamat, Email, Jabatan)'\natau ketik 'Batal' untuk membatalkan: ").capitalize()
    
        # Jika user memilih opsi untuk membatalkan
        if key_dipilih == 'Batal':
            print(Fore.RED + "Operasi dibatalkan.")
            return # Keluar dari fungsi
         
        # Memeriksa apakah key ada di daftar_karyawan
        if key_dipilih in daftar_karyawan[0]: # Jika key valid
 
            # Meminta input untuk nilai berdasarkan key yang dipilih
            value_dipilih = input(f"Masukkan value dari {key_dipilih} : ").lower()
    
            # Mencari karyawan yang sesuai dengan kriteria
            hasil_kriteria = [karyawan for karyawan in daftar_karyawan if karyawan.get(key_dipilih).lower() == value_dipilih]
    
            # Jika data data karyawan ditemukan berdasarkan kriteria tsb
            if hasil_kriteria:

                # Mengumpulkan data untuk ditampilkan
                data = [[karyawan[key] for key in karyawan] for karyawan in hasil_kriteria]
                headers = hasil_kriteria[0].keys()
        
                # Menampilkan data dengan tabulate
                print(f"Menampilkan karyawan dengan {key_dipilih} = {value_dipilih}:")
                print(tabulate(data, headers=headers, tablefmt="grid"))
                break
            else:
                print(Fore.RED + f"Tidak ada karyawan dengan {key_dipilih} = {value_dipilih}.")
        
        else:
            print(Fore.RED + "Key yang dimasukkan tidak valid.\nSilakan coba lagi atau ketik 'Batal' untuk membatalkan.")
    

# sub menu 1 menampilkan tabel data karyawan
def sub_menu1():
    while True:
        print(''' 
_______________________________________________________________________________________________
Sub Menu Menampilkan Data Karyawan PT.ABC:
1. Menampilkan Seluruh Data Karyawan
2. Menampilkan Data Key tertentu
3. Memfilter Data Karyawan
4. Kembali Ke Main Menu
_______________________________________________________________________________________________
''')
        pilihan_submenu1 = input(Style.RESET_ALL +'Silakan pilih sub menu yang akan dijalankan [1-4] : ')
        if pilihan_submenu1 == '1': # Menu untuk menampilkan keseluruhan data karyawan yang ada
            tampilkan_data_karyawan (daftar_karyawan)
        elif pilihan_submenu1 == '2': # Menu untuk menampilkan data sesuai dengan atribut 
            tampilkan_data_key_tertentu(daftar_karyawan)
        elif pilihan_submenu1 == '3': # Menu untuk menampilkan filter data karyawan 
            filter_data_karyawan(daftar_karyawan) 
        elif pilihan_submenu1 == '4':
            break # Keluar dr loop dan kembali ke main menu
        else:
            print(Fore.RED + 'Sub menu tidak valid.\nSilakan pilih menu dari [1-4]')

# Function untuk menambah data karyawan baru
def tambah_karyawan(daftar_karyawan):
    while True :
        # meminta input dari user untuk memasukkan id karyawan baru sebanyak 6 digit
        id_baru=input(Fore.GREEN + 'Masukkan ID Karyawan Baru [ABC001]: ').upper() 
        
        # Cek apakah id yang diinput memenuhi syarat 6 digit
        if(len(id_baru)!=6):
           print(Fore.RED + Style.BRIGHT +'ID Karyawan Wajib 6 Digit.\nSilakan coba input ID baru')
           continue # Skip proses lain didalam loop lsg minta ID baru

        # Cek apakah ada duplikasi ID
        if any (karyawan['ID'] == id_baru for karyawan in daftar_karyawan):
           print(Fore.RED + Style.BRIGHT + 'ID tersebut sudah terpakai.\nSilakan coba input ID lain')
           continue # Skip proses lain didalam loop lsg minta ID baru

        # Jika ID sudah memenuhi syarat maka lanjut keproses input data lainnya
        nama = input ('Input Nama Karyawan Baru :').capitalize()
        gender = input ('Input Gender Karyawan Baru [Perempuan / Laki-laki] : ').capitalize()
        alamat = input ('Input Alamat Karyawan Baru : ').capitalize()
        email = input ('Input Email Karyawan Baru : ')
        jabatan = input ('Input Jabatan Karyawan Baru : ').capitalize()

        konfirmasi = input (Fore.YELLOW + Style.BRIGHT +'Apakah data akan disimpan [Y/N] : ').capitalize()

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

            # Menambahkan data tersebut kedalam list
            daftar_karyawan.append(data_baru)
            print (Fore.GREEN + Style.BRIGHT +'Data karyawan berhasil ditambahkan')
            break # Keluar dari loop setelah berhasil menambahkan data karyawann baru
        else:
            print (Fore.RED + Style.BRIGHT + 'Data baru tidak jadi disimpan.\nSilakan input data baru kembali.')

# Function update data karyawan
def update_karyawan (daftar_karyawan):
    # Memeriksa apakah daftar karyawan kosong
    if not daftar_karyawan:
        print('Daftar karyawan kosong')
        return
    
    # Jika daftar karyawan tidak kosong
    while True:
        id_karyawan = input ('Input ID karyawan yang akan diupate : ')

        # Mencari data karyawan berdasarkan ID yang diinput
        # Jika ID tidak ditemukan, maka karyawan akan menjadi none
        karyawan = next((k for k in daftar_karyawan if k['ID']==id_karyawan),None)

        if not karyawan :
            print(Fore.RED + Style.BRIGHT + 'ID karyawan tersebut tidak ditemukan')
            continue # Skip proses lainnya yang dan meminta user input ID karyawan lagi
        else:
            break # Keluar dari loop jika data ditemukan
    while True:
        print('Silakan pilih data yang akan diupdate \n[ex : ID,Nama,Gender,Alamat,Email atau Jabatan')
        key = input ('Input atribut yang akan diupdate : ').capitalize()

        # Cek apakah atribut yang diinput bener
        if key not in karyawan :
            print(Fore.RED + f"Atribut '{key}' tidak ditemukan")
            continue # Skip proses lainnya dan meminta masukkan atribut kembali
        else :
            break # Keluar dari loop jika atribut benar

    # Minta data baru untuk atribut tersebut
    nilai_baru = input('Sialakn input nilai baru = ').capitalize()

    # Update data
    karyawan [key] = nilai_baru
    print(f'Data {key} sudah diupdate menjadi {nilai_baru}')

# Function untuk menghapus data
def hapus_karyawan(daftar_karyawan):

    # Memeriksa apakah daftar karyawan kosong
    if not daftar_karyawan:
        print(Fore.RED +'Daftar karyawan kosong')
        return
    
    # Jika daftar karyawan tidak kosong
    while True:
        id_karyawan=input(Fore.YELLOW + Style.BRIGHT + 'Masukkan ID Karyawan yang akan dihapus : ')
        karyawan_ditemukan=False
        
        # Cari data karyawan
        for i,karyawan in enumerate(daftar_karyawan) :
            if karyawan['ID']==id_karyawan :
                karyawan_ditemukan=True

                # ID karyawan berhasil ditemukan
                # Meminta konfirmasi penghapusan ke user
                konfirmasi=input(Fore.YELLOW + Style.BRIGHT + f"Apakah Anda yakin ingin menghapus data karyawan {id_karyawan} [Y/N]: ").capitalize()
                
                if konfirmasi=='Y':
                    del daftar_karyawan[i]
                    print(Fore.GREEN + Style.BRIGHT + f"Data karyawan dengan ID {id_karyawan} telah dihapus")
                    return # Keluar dari function setelah menghapus data
                else :
                    print(Fore.RED + Style.BRIGHT + "Penghapusan data dibatalkan")
                    break # Keluar dari loop for
            
        # Bila ID tidak ditemukan/salah input maka akan menanyakan kembali ke user 
        # Apakah user ingin mencoba lagi atau tidak
        if not karyawan_ditemukan:
            print (Fore.RED + Style.BRIGHT + "Karyawan dengan ID tersebut tidak ditemukan")
        pilihan = input(Fore.YELLOW + Style.BRIGHT +"Apakah Anda ingin mencoba lagi [Y/N]: ").capitalize()
        if pilihan!='Y' :
            print(Fore.RED + Style.BRIGHT + "Penghapusan data dibatalkan")
            return # Keluar dari function
        
# Main Menu
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
        # Select main menu
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
            break # Untuk keluar dari loop
        else :
            print(Fore.RED + Style.BRIGHT + 'Menu yang dipilih tidak valid.\nSilakan pilih menu [1-5]')    
main_menu()


