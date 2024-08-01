# print(3+6)
# b = olma, banan, uzim = 'qizil', 'sariq', 'qora'
# print(b)  
# x=y=z='olma'
# print(x,y,z)
# print('shirin', x)




# python operatorlar:
# firt_var, two_var = 45, 55
# print(firt_var)
# print(two_var)
# s = 'salom olam'
# s.split (' ')
# print(s.split(' '))

# s = 'salom olam'
# a, b = s.split(' ')
# print(a)
# print (b)
from tkinter import *

oyna = Tk()
oyna.title("Kalkulyator")

Yigindi = StringVar()
def hisobla() :
    Yigindi.set(int(birinchi_son.get()) + int(ikkinchi_son.get()))

text_1 = Label(oyna, text="Birinchi son: ")
text_1.grid(row=0)

text_2 = Label(oyna, text="Ikkinchi son: ")
text_2.grid(row=1)

birinchi_son = Entry(oyna)
birinchi_son.grid(row=0, column=1)

ikkinchi_son = Entry(oyna)
ikkinchi_son.grid(row=1, column=1)
tugma = Button(oyna, text = "Hisoblash", command=hisobla).grid(row=3, column=0, columnspan=2)

natija = Label(oyna, text="0", fg="red", font="Arial 15", textvariable=Yigindi).grid(rowspan=2, column=2, row=0)



mainloop()