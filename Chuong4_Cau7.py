#Cau7
class ToaDo:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def Nhap(self):
        self.x=float(input("Nhap x:"))
        self.y=float(input("Nhap y:"))
    def In(self):
        print(f"({self.x},{self.y})")
    def KhoangCach(self,td):
        return sqrt((self.x-td.x)**2+(self.y-td.y)**2)
td1=ToaDo()
td2=ToaDo()
print("Nhap toa do diem 1:")
td1.Nhap()
td1.In()
print("Nhap toa do diem 2:")
td2.Nhap()
td2.In()
print("Khoang cach giua 2 diem la:",td1.KhoangCach(td2))