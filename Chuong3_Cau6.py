#Cau6
so=int(input("Moi nhap vao so co 2 chu so: "))
if 10<=so<=99:
    chuc=so//10
    donvi=so%10
    tong=chuc+donvi
    tich=chuc*donvi
    if chuc==1: print('Muoi ')
    elif chuc==2: print('Hai muoi ')
    elif chuc==3: print('Ba muoi ')
    elif chuc==4: print('Bon muoi ')
    elif chuc==5: print('Nam muoi ')
    elif chuc==6: print('Sau muoi ')
    elif chuc==7: print('Bay muoi ')
    elif chuc==8: print('Tam muoi ')
    elif chuc==9: print('Chin muoi ')
    
    if(donvi==1): print('Mot ')
    elif(donvi==2): print('Hai ')
    elif(donvi==3): print('Ba ')
    elif(donvi==4): print('Bon ')
    elif(donvi==5): print('Lam ')
    elif (donvi==6): print('Sau ')
    elif (donvi==7): print('Bay ')
    elif (donvi==8): print('Tam ')
    elif (donvi==9): print('Chin ')