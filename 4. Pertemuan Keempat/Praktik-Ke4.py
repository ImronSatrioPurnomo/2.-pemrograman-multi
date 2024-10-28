class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang+self.lebar)
    def luas(self):
        return self.panjang*self.lebar
    def str(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    

try:
    panjang = float(input("Masukan Panjang :"))
    lebar = float(input("Masukan Lebar :"))
    
    if panjang <= 0 or lebar <= 0:
        print("Nilai panjang dan lebar harus positif")
    
    else:
        PP=PersegiPanjang(panjang, lebar)
        print(PP)
        print("Keliling:", PP.keliling(), "cm")
        print("Luas:", PP.luas(), "cm^2")
    
except ValueError:
    print("input gak valid bang, masukin angka dong.")
    