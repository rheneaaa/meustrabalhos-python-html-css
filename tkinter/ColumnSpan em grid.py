from tkinter import *

root = Tk()
root.title("Login")

Label(root, width=20, bg="red").grid(column=0)
Label(root, width=20, bg="green").grid(column=1)
Label(root, width=40, bg="blue").grid(columnspan=2, sticky='we')

root.mainloop()
