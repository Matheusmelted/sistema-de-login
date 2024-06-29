from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()
janela.title("DP systems - login/cadrs")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
#
logo = PhotoImage(file="icons/logo.png")
#
LeftFrame = Frame(janela, width=200, height=300, bg="purple", relief="raise")
LeftFrame.pack(side=LEFT)
#
RightFrame = Frame(janela, width=395, height=300, bg="purple", relief="raise")
RightFrame.pack(side=RIGHT)
#
LogoLabel = Label(LeftFrame, image=logo, bg="purple")
LogoLabel.place(x=50, y=100)
#
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="purple", fg="white")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)
#
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="purple", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=30)
PassEntry.place(x=150, y=160)
#
LoginButton = ttk.Button(RightFrame, text="Login", width=30)
LoginButton.place(x=150, y=225)
#
RegisterButton = ttk.Button(RightFrame, text="Register", width=20)
RegisterButton.place(x=180, y=260)



janela.mainloop()
