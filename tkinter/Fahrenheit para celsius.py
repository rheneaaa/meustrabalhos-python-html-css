from tkinter import *

# Funções
def calcular():
    F = float(textbox1.get())
    C = (F - 32) * 5/6
    final.set(str(round(C, 1)) + " graus Celsius")

root = Tk()
root.title("App")

final = StringVar()

# Widgets
label1 = Label(root, text="Graus Fahrenheit")
textbox1 = Entry(root)
button1 = Button(root, text="Calcular", command=calcular)
label_resultado = Label(root, textvariable=final)

# Layout
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()



root.mainloop()
