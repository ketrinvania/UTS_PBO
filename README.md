# UTS_PBO
# Nama	: Ketrin Vani Andini
# NIM	: 20210801348


Dengan menggunakan Bahasa pemrograman python buatlah

1.	Jelaskan narasi singkat tentang paradigma Pemrograman dan apakah yang dimaksud
dengan pemograman berorientasi objek?

  Jawab : 

    -	Paradigma pemrograman merupakan sebuah pendekatan atau konsep dalam menstrukturisasi suatu kode program.
    -	Pemrograman Berorientasi Objek adalah paradigma pemrograman yang berorientasikan kepada objek yang merupakan suatu metode dalam pembuatan program, dengan tujuan  untuk menyelesaikan kompleksnya berbagai masalah program yang terus meningkat.
    
2. Buatlah program seperti dibawah ini sesuaikan dengan nim dan nama anda !

  Jawab : 
  
        def header():
          print("=======================")
          print ("PROGRAM QUIZ")
          print("=======================")
        header()
        
        def data_diri():
          input("Masukkan Nama \t: ")
          input("Masukkan NIM  \t: ")
        data_diri()

        Output :
        
        =======================
        PROGRAM QUIZ
        =======================
        Masukkan Nama : Ketrin Vani Andini
        Masukkan NIM : 20210801348
        
3. Jelaskan perbedaan looping dengan continue dan break dari codingan di bawah ini 
          
          for val in "bahasa": 
              if val == "h": 
                continue 
                #break
              print (val) 
          print ("selesai")
          
   Jawab :
   
          Menurut saya perbedaan nya adalah jika looping dengan continue pada saat kondisi val == h maka huruf h dari kata “Bahasa” akan di skip(h tidak akan dicetak) dan dilanjut ke huruf selanjutnya.
          Sedangkan looping dengan break pada saat kondisi val == h, setelah looping menemukan huruf h proses akan berhenti (h tidak akan dicetak) dan tidak melanjutkan ke huruf selanjutnya
          
4. Buatlah program sederhana seperti dibawah ini dengan rumus ppn 10/100 dari total harga input :

   Jawab :
   
           def data_diri():
              print("Nama \t: Ketrin Vani Andini")
              print("NIM  \t: 20210801348")
           data_diri()

            pilihan = {'minuman ':['Capucino','Teh']}
            
            while True: pil = input('''
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
                harga = int(input("Masukkan Harga : "))
                ppn = harga_awal * 0.1
                total = ppn + harga_awal
                print(int(total))

            else:
                print("PROGRAM FINISH")
                break
                
            OUTPUT :
            
            
            Nama    : Ketrin Vani Andini
            NIM     : 20210801348

            Menu:
            1. Capucino
            2. Teh
            3. Exit

            Masukkan Pilihan : 1
            Memilih Capucino
            Masukkan Harga : 3000
            3300


           Menu:
           1. Capucino
           2. Teh
           3. Exit

           Masukkan Pilihan : 2
           Memilih teh
           Masukkan Harga : 3000
           3300


           Menu:
           1. Capucino
           2. Teh
           3. Exit

          Masukkan Pilihan : 3
          PROGRAM FINISH

5. Buatlah dengan class dan definition terkait inputan jam, menit, detik yang dimana jam hanya bisa 24, menit 60, detik 60 !

   Jawab :
   
          class Waktu:

              def __init__(self, jam, menit, detik):
                  self.jam = jam
                  self.menit = menit
                  self.detik = detik
    
              def getJam(self):
                   return self.jam
                   
              def getMenit(self):
                   return self.menit
    
              def getDetik(self):
                   return self.detik
    
              def info(self):
                    if self.jam <= 24 and self.menit <= 60 and self.detik <= 60:
                          print(f"Time \t\t: {jam} : {menit} : {detik}")
                    else :
                          print ("error ! format yang anda masukkan salah!")
    
          jam = int(input("Masukkan jam \t: "))
          menit = int(input("Masukkan menit \t: "))
          detik = int(input("Masukkan detik \t: "))

          time = Waktu(jam, menit, detik)
          print(time.info())
          
          
          OUTPUT :
          
          Masukkan jam    : 12
          Masukkan menit  : 12
          Masukkan detik  : 12
          Time            : 12 : 12 : 12
          
          
          Masukkan jam    : 40
          Masukkan menit  : 90
          Masukkan detik  : 90
          error ! format yang anda masukkan salah!
          


#STRUKTUR FOLDER
📦UTS_PBO
 ┣ 📜README..md
 ┣ 📜jawaban1.py
 ┣ 📜jawaban2.py
 ┣ 📜jawaban3.py
 ┣ 📜jawaban4.py
 ┗ 📜jawaban5.py
