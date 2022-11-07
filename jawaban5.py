#  Nama : Ketrin Vani Andini
#  NIM  : 20210801348
#  UTS PBO

# NOMER 5

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


