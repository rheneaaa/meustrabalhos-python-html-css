from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Rhene")
menu_inicial.geometry("500x500")

label2 = Label(menu_inicial)
label2['text'] = "Texto da label2"
label2['font'] = "Arial 20"
label2['bd'] = 1
label2['relief'] = "solid"
label2.pack()

for item in label2.keys():
    print(item, ": ", label2[item])


menu_inicial.mainloop()
