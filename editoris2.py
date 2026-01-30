#!/home/udoindra/udovenv/udovenv/bin/python
#fileops.py
# W-A-R(Write-Append-Read) Practice
from datetime import datetime

def clear_screen():
    # \033[H  -> Memindahkan kursor ke posisi home (0,0)
    # \033[2J -> Membersihkan seluruh layar
    print("\033[H\033[2J", end="")

def clear():
    print("\n"*30)
    
def bukafile():
    namakan=""
    clear_screen()
    while namakan == "":
        namakan = input("Masukkan nama file: ")
    clear()
    return(namakan)

def karya(namafile):
    #deklarasi variabel local
    paragraf=[]
    konten=[]
    teks = " "
    #tampilan pengguna
    clear_screen()
    print(f"************** {namafile} ****************")
    isi = tampilkan(namafile)
    konter = len(isi)
    #mulai menulis
    while teks != "":
        konter += 1
        teks = input(f"{konter:<3}" + ": ")
        if teks != "" and teks != ":tgl":
            paragraf.append(teks)
        if teks == ":tgl":
            teks = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            paragraf.append(teks)

    konten = [isi + "\n" for isi in paragraf]
    print("******************************")
    return(konten)
    
def simpan_file(namafile, naskah, mode="a"):
    """
    mode = "a" untuk append
    mode = "w" untuk overwrite
    """
    with open(namafile, mode) as file:
        file.writelines(naskah)
    
def tampilkan(namafile):
    clear_screen()
    print(f"************** {namafile} ****************")    
    cx=0
    konten=[]
    #variabel cx berguna untuk looping angka paragraf
    try:
        with open(namafile, "r") as file:
            for baris in file:
                cx += 1
                konten.append(baris)
                print(f"{str(cx):<3}" + ": " + baris, end="")
        print("******************************", end="")
        input()
        # kembalikan list yg sudah terisi
        return(konten)
    except FileNotFoundError:
        print("File belum ada. Silakan menulis dulu.")
        input("Tekan Enter...")
        return []

def handle_input_baris(prompt="Masukkan nomor baris"):
    def decorator(func):
        def wrapper(namafile, *args, **kwargs):
            tulisan = tampilkan(namafile)
            if not tulisan:
                return

            try:
                baris = int(input(f"{prompt}: "))
                if baris < 1 or baris > len(tulisan):
                    print("Nomor baris tidak valid")
                    return
            except ValueError:
                print("Masukkan angka!")
                return

            return func(namafile, tulisan, baris, *args, **kwargs)
        return wrapper
    return decorator

@handle_input_baris(prompt="Mo edit baris berapa")
def sunting(namafile, tulisan, baris):
    print("Teks lama: ", tulisan[baris-1])
    ganti = input("ketikkan teks pengganti: ")
    tulisan[baris-1] = ganti + "\n"
    simpan_file(namafile, tulisan, mode="w")

@handle_input_baris(prompt="Mo hapus baris berapa")
def hapus_baris(namafile, tulisan, baris):
    print("****")
    tulisan.pop(baris-1)
    simpan_file(namafile, tulisan, mode="w")

@handle_input_baris(prompt="Mo edit baris berapa")
def sunting_kata(namafile, tulisan, baris):
    perkata = tulisan[baris-1].split()
    for i, kata in enumerate(perkata, start=1):
        print(f"[{i}]{kata}", end = " ")
    print()
    try:
        ubah=int(input("Ganti kata nomor: "))
        if ubah < 1 or ubah > len(perkata):
            print("nomor tidak valid")
            return
    except ValueError:
        print("masukkan angka!")
        return
    print(f"{perkata[ubah-1]} jadi: ", end="")
    kata_baru =  input()
    perkata[ubah-1]=kata_baru
    kalimat = " ".join(perkata)
    #gabungkan kembali jadi tulisan
    tulisan[baris-1] = kalimat + "\n"
    simpan_file(namafile, tulisan, mode="w")

#Program Utama memanggil fungsi-fungsi
if __name__ == "__main__":
    namafile = bukafile() 
    while True:
        print("============================")
        print("------- EDITOR BARIS -------")
        print("============================")
        print("       1. Membaca")
        print("       2. Menulis")
        print("       3. Sunting Baris")
        print("       4. Sunting Kata")
        print("       5. Hapus Baris")
        print("       6. Keluar")
        print()    
        pilih = input("Pilih: ")
    
        if pilih == "1":
            tampilkan(namafile)
        elif pilih == "2":
            tulisan = karya(namafile)
            simpan_file(namafile, tulisan)
        elif pilih == "3":
            sunting(namafile)
        elif pilih == "4":
            sunting_kata(namafile)
        elif pilih == "5":
            hapus_baris(namafile)
        elif pilih == "6":    
            print(f"\nKeluar dari Program.")
            break  # Berhenti paksa dari loop
        else:
            print("Menu tidak tersedia.")
