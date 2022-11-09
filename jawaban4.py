# Nama  : Ketrin Vani Andini
# NIM   : 20210801348
# UTS PBO

# NOMER 4

def data_diri():
    print("Nama \t: Ketrin Vani Andini")
    print("NIM  \t: 20210801348")

data_diri()

pilihan = {'minuman ':['Capucino','Teh']}

while True:
    pil = input('''

 Menu:
1. Capucino
2. Teh
3. Exit

Masukkan Pilihan : ''')

    if pil == '1':
        print("Memilih Capucino")
        harga_awal = int(input("Masukkan Harga : "))
        ppn = harga_awal * 0.1
        total = ppn + harga_awal
        print(int(total))
    
    elif pil == '2':
        print("Memilih teh")
        harga_awal = int(input("Masukkan Harga : "))
        ppn = harga_awal * 0.1
        total = ppn + harga_awal
        print(int(total))

    else:
        print("PROGRAM FINISH")
        break





    





