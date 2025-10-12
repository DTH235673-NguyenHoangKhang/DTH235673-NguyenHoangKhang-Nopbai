#Cau5

s="a; B; c; 9; e; @; "
arr=s.split(';')
chuthuong=0
chuhoa=0
chuso=0
kytudacbiet=0
khoangtrang=0
nguyenam=0
phuam=0
for i in arr:
    word=i
    if len(word.strip())!=0:
        if word.strip().isalpha():
            if word.strip().islower():
                chuthuong+=1
            else:
                chuhoa+=1
            if word.strip().lower() in 'aeiou':
                nguyenam+=1
            elif word.strip().lower() in 'bcdfghjklmnpqrstvwxyz':
                phuam+=1
        elif word.strip().isdigit():
            chuso+=1
        else:
            kytudacbiet+=1
    else:
        khoangtrang+=1
   
print("Chữ thường =",chuthuong)
print("Chữ hoa =",chuhoa)
print("Chữ số =",chuso)
print("Ký tự đặc biệt =",kytudacbiet)   
print("Khoảng trắng =",khoangtrang)
print("Nguyên âm =",nguyenam)
print("Phụ âm =",phuam)
   