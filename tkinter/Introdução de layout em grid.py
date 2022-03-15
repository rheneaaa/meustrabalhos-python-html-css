from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Rhene")
#menu_inicial.geometry("500x500")

label1 = Label(menu_inicial, text="label 1", font="Arial 20", bg="red")
label2 = Label(menu_inicial, text="label 2", font="Arial 20", bg="green")
label3 = Label(menu_inicial, text="label 3", font="Times 20", bg="blue")

btn1 = Button(menu_inicial, text="Click1")
btn2 = Button(menu_inicial, text="Click2")
btn3 = Button(menu_inicial, text="Click2")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

menu_inicial.mainloop()
