## Main Menu

from tabulate import tabulate


data1 = [ {"Nama Pasien" : "Budi",  "ID Pasien": "IDP-00001" ,"Umur" : 30, "Gender": "Pria", "Pekerjaan" : "Teknisi Pabrik", "Pendidikan Terakhir": "S1"
         , "Subjective": "Sesak Nafas dan Batuk jangka panjang ", "Objective": "Tekanan Darah : 145/100, Nadi : 85/m, Temperatur : 37°C"}
         ,{"Nama Pasien" : "Citra", "ID Pasien": "IDP-00002" ,"Umur" : 29, "Gender": "Wanita", "Pekerjaan" : "Guru", "Pendidikan Terakhir": "S1"  
         , "Subjective": "Sakit di bagian dada, tidak ada kesusahan bernafas ", "Objective": "Tekanan Darah : 120/80, Nadi : 76/m, Temperatur : 35°C"}
         ]

def choice1():
    while True:
        global data1
        print()
        print()
        print("| ========= Menu Data Pasien ========= |")
        print()
        print("1. Tampilkan Seluruh Data Pasien")
        print("2. Tampilkan Data Pasien Spesifik")
        print("3. Membuat Data Pasien Baru")
        print("4. Update Data Pasien")
        print("5. Hapus Data Pasien")
        print("6. Kembali ke Menu Utama")

        inputChoice1 = input("Masukkan pilihan : ")

        try:
            Input = int(inputChoice1)
            if Input == 1:
                print()
                print()
                print(tabulate(data1, headers="keys", tablefmt="grid"))
                print()
                print()
            elif Input == 2:
                print()
                print("| ========= Akses Data Pasien Spesifik ========= |")
                print()
                while True:
                    input1 = input("Masukkan Nama pasien : ")
                    input2 = input("Masukkan ID pasien : ")
                    hasil1 = [i for i in data1 if i["Nama Pasien"] == input1 and i["ID Pasien"] == input2]
                    if hasil1:
                        print(tabulate(hasil1, headers="keys", tablefmt="grid"))
                        break
                    else:
                        print("Data Pasien tidak ditemukan!")
                        break
            elif Input == 3:
                choice2()
                return
            elif Input == 4:
                choice3()
                return
            elif Input == 5:
                choice4()
                return
            elif Input == 6:
                return
            else:
                print("Mohon Memasukkan Angka 1 sampai 6")
        except:
            print ("Mohon memasukkan input yang benar")


def choice2():
    while True:
        global data1
        print()
        print()
        print("| ====== Menu Create Data Pasien ====== |")
        print()
        print("1. Menampilkan Seluruh Data Pasien")
        print("2. Membuat Data Pasien Baru")
        print("3. Kembali ke Menu Utama")


        inputChoice2 = input("Masukkan pilihan : ")


        Input = int(inputChoice2)
        if Input == 1:
            print()
            print()
            print(tabulate(data1, headers="keys", tablefmt="grid"))
            print()
            print()
        elif Input == 2:
            while True:
                input21 = input("Masukkan Nama Pasien : ")
                if input21.isalpha():
                    break
                else:
                    print("Mohon hanya memasukkan karakter di alfabet")
            while True:
                input22 = input ("Masukkan ID Pasien : ")

                duplicate = any(input22 == i["ID Pasien"] for i in data1)

                if duplicate:
                    print("Pasien ID sudah ada, mohon input yang berbeda")
                    continue

                if not input22[3] == "-":
                    print("Format ID pasien salah, format harus mengikuti IDP-xxxxx")
                elif len(input22) != 9:
                    print("Format ID pasien salah, format harus mengikuti IDP-xxxxx")
                elif not input22[0:3] == "IDP":
                    print("Format ID pasien salah, format harus mengikuti IDP-xxxxx")
                else:
                    break
            while True:
                input23 = input("Masukkan Umur Pasien : ")
                if input23.isnumeric():
                    break
                else:
                    print("Mohon hanya memasukkan angka")
            while True:
                input24 = input("Masukkan Gender Pasien : ")
                if input24 == "Pria":
                    break
                elif input24 == "Wanita":
                    break
                else:
                    print("Mohon hanya memasukkan (Pria) atau (Wanita)")
            input25 = input("Masukkan Pekerjaan Pasien : ")
            input26 = input("Masukkan Pendidikan Terakhir Pasien : ")
            input27 = input("Masukkan Informasi Subjective Pasien : ")
            input28 = input("Masukkan Informasi Objective Pasien : ")

            inputCreate = {"Nama Pasien" : (input21),  "ID Pasien": (input22) ,"Umur" : (input23), "Gender": (input24), "Pekerjaan" : (input25), "Pendidikan Terakhir": (input26)
                            , "Subjective": (input27), "Objective": (input28)}
            
            data1.append(inputCreate)

            print(tabulate(data1, headers="keys", tablefmt="grid"))
        else:
            return

def choice3():
    while True:
        global data1
        print()
        print()
        print("| ====== Menu Update Data Pasien ====== |")
        print()
        print("1. Menampilkan Seluruh Data Pasien")
        print("2. Mengupdate Data Pasien Spesifik")
        print("3. Kembali ke Menu Utama")


        inputChoice3 = input("Masukkan pilihan : ")


        Input = int(inputChoice3)
        if Input == 1:
            print()
            print()
            print(tabulate(data1, headers="keys", tablefmt="grid"))
            print()
            print()
        elif Input == 2:
            while True:
                input32 = input ("Masukkan ID Pasien : ")

                duplicate = any(input32 == i["ID Pasien"] for i in data1)

                if duplicate:
                    print()
                    print(" ================ Data Lama ================ ")
                    data3 = [i for i in data1 if i["ID Pasien"] == input32]
                    print(tabulate(data3, headers="keys", tablefmt="grid"))
                    while True:
                        input31 = input("Masukkan (Updated) Nama Pasien : ")
                        if input31.isalpha():
                            break
                        else:
                            print("Mohon hanya memasukkan karakter di alfabet")
                            break
                    while True:
                        input33 = input("Masukkan (Updated) Umur Pasien : ")
                        if input33.isnumeric():
                            break
                        else:
                            print("Mohon hanya memasukkan angka")
                    while True:
                        input34 = input("Masukkan (Updated) Gender Pasien : ")
                        if input34 == "Pria":
                            break
                        elif input34 == "Wanita":
                            break
                        else:
                            print("Mohon hanya memasukkan (Pria) atau (Wanita)")
                    input35 = input("Masukkan (Updated) Pekerjaan Pasien : ")
                    input36 = input("Masukkan (Updated) Pendidikan Terakhir Pasien : ")
                    input37 = input("Masukkan (Updated) Informasi Subjective Pasien : ")
                    input38 = input("Masukkan (Updated) Informasi Objective Pasien : ")

                    inputUpdate = {"Nama Pasien" : (input31),  "ID Pasien": (input32) ,"Umur" : (input33), "Gender": (input34), "Pekerjaan" : (input35), "Pendidikan Terakhir": (input36)
                                    , "Subjective": (input37), "Objective": (input38)}
                    
                    for i, j in enumerate(data1):
                        if j["ID Pasien"] == input32:
                            data1[i] = inputUpdate
                            print(" ================ Data berhasil diperbarui! ================ ")
                            break
                else:
                    print("Data tidak ditemukan! mohon input ID Pasien yang benar")
                    continue
                return     
        else:
            return

def choice4():
    while True:
        global data1
        print()
        print()
        print("| ====== Menu Delete Data Pasien ====== |")
        print()
        print("1. Menampilkan Seluruh Data Pasien")
        print("2. Menghapus Data Pasien Spesifik")
        print("3. Kembali ke Menu Utama")


        inputChoice4 = input("Masukkan pilihan : ")


        Input = int(inputChoice4)
        if Input == 1:
            print()
            print()
            print(tabulate(data1, headers="keys", tablefmt="grid"))
            print()
            print()
        elif Input == 2:
            while True:
                input42 = input ("Masukkan ID Pasien : ")

                duplicate = any(input42 == i["ID Pasien"] for i in data1)

                if duplicate:
                    print()
                    for i, j in enumerate(data1):
                        if j["ID Pasien"] == input42:
                            while True:
                                print("Data yang akan dihapus : ")
                                print(tabulate([j], headers="keys", tablefmt="grid"))
                                confirm = input("Apakah Anda yakin ingin menghapus data ini? (Y/N): ")
                                if confirm.upper() == "Y":
                                    del data1[i]
                                    print(" ================ Data berhasil dihapus! ================ ")
                                elif confirm.upper() == "N":
                                    print(" ================ Penghapusan dibatalkan ================ ")
                                else:
                                    print("Mohon hanya mengisi Y/N")
                                    continue
                                break
                else:
                    print("Data tidak ditemukan! mohon input ID Pasien yang benar")
                    continue
                return     
        else:
            return



def main_menu():
    while True:
        print()
        print()
        print("| ============ Menu Utama ============ |")
        print("| ========== Data Pasien RS =========  |")
        print()
        print("1. Tampilkan Data Pasien")
        print("2. Membuat Data Pasien Baru")
        print("3. Mengupdate Data Pasien")
        print("4. Menghapus Data Pasien")
        print("5. Tampilkan Penjelasan Kolom Data Pasien")
        print("6. Keluar")

        
        inputMain_Menu = input("Masukkan pilihan : ")

        try:
            Input = int(inputMain_Menu)
            if isinstance(Input, int):
                if Input == 1:
                    choice1()
                elif Input == 2:
                    choice2()
                elif Input == 3:
                    choice3()
                elif Input == 4:
                    choice4()
                elif Input == 5:
                    print()
                    print()
                    print(" ================ Informasi Tabel ================ ")
                    print()
                    print("Nama                 ---> Nama Pasien")
                    print("ID Pasien            ---> Kode unik per pasien")
                    print("Umur                 ---> Umur Pasien")
                    print("Gender               ---> Gender Pasien (Pria/Wanita)")
                    print("Pekerjaan            ---> Pekerjaan Pasien saat ini")
                    print("Pendidikan Terakhir  ---> Pendidikan Formal Terakhir Pasien")
                    print("Subjective           ---> Informasi Subjektif Pasien (Sumber Informasi : Pasien sendiri, Penjaga Pasien, dll.)")
                    print("Objective            ---> Informasi Objektif Pasien (Sumber Informasi : Dokter, Perawat, Laporan Medis, dll.) ")
                elif Input == 6:
                    print("Terimakasih!")
                    break
                else:
                    print("Mohon hanya memasukkan angka 1 sampai 6")
            else:
                print("Mohon hanya memasukkan angka")
        except:
            print ("Mohon hanya memasukkan angka")

main_menu()


