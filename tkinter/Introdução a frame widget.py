from tkinter import *

root = Tk()
root.title("App")

# widgets
frame_login = Frame(root)

label_usuario = Label(frame_login, text="Usuário:")
label_password = Label(frame_login, text="Password:")
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar = Button(frame_login, text="Entrar")

# Layout
label_usuario.grid(row=0, column=0)
label_password.grid(row=1, column=0)
text_usuario.grid(row=0, column=1)
text_password.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=1)

frame_login.grid()

root.mainloop()
