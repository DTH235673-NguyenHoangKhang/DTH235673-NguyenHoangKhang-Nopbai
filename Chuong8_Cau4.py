from tkinter import *
root=Tk()
entry_kq=Entry(root,width=20)
entry_kq.grid(row=0,column=0)
def btn_Click(number):
    entry_kq.insert(END,str(number))
def btn_Click_kq():
    kq=eval(entry_kq.get())
    entry_kq.insert(END,'=')
    entry_kq.delete(0,END)
    entry_kq.insert(0,str(kq))

frame_button=Frame(root)
for i in range(1,10):
    btn=Button(frame_button,text=str(i),command=lambda x=i:btn_Click(x),width=5)
    btn.grid(row=(i-1)//3,column=(i-1)%3)
btn_=Button(frame_button,text='-',command=lambda:btn_Click('-'),width=5).grid(row=3,column=0)
btn_0=Button(frame_button,text='0',command=lambda:btn_Click(0),width=5).grid(row=3,column=1)
btn_Cham=Button(frame_button,text='.',command=lambda:btn_Click('.'),width=5).grid(row=3,column=2)
frame_button.grid(row=1,column=0)

frame_Pheptinh=Frame(root)
btncong=Button(frame_Pheptinh,text='+',command=lambda:btn_Click('+'),width=3).grid(row=0,column=0)
btntru=Button(frame_Pheptinh,text='-',command=lambda:btn_Click('-'),width=3).grid(row=0,column=1)
btnnhan=Button(frame_Pheptinh,text='*',command=lambda:btn_Click('*'),width=3).grid(row=0,column=2)
btnchia=Button(frame_Pheptinh,text='/',command=lambda:btn_Click('/'),width=3).grid(row=0,column=3)
btnbang=Button(frame_Pheptinh,text='=',command=btn_Click_kq,width=3).grid(row=0,column=4)
frame_Pheptinh.grid(row=2,column=0)

frame_clr=Frame(root)
btnClr=Button(frame_clr,text='Clr',command=lambda:entry_kq.delete(0,END),width=15).grid(row=0,column=0)
frame_clr.grid(row=3,column=0)




root.mainloop()
