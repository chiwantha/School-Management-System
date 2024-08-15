from tkinter import *
from tkinter import messagebox
import winreg
import mysql.connector
import Access
import os

current = os.path.dirname(os.path.realpath(__file__))


def About(frame):
    about_frame = Frame(frame, height=651, width=1185)
    about_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.application/.about/About.png")
    Background = Label(about_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)


def Help():
    messagebox.askokcancel("Contact", "Just go to Contact tab and Contact Developer")


def Contact(frame):
    contact_frame = Frame(frame, width=1185, height=651)
    contact_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.application/.contact/contact.png")
    Background = Label(contact_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)


def database(frame):
    data = Frame(frame, width=1185, height=651)
    data.pack()

    back = PhotoImage(file=current+"/.ux/padma/.application/.database/Database Settings.png")
    Background = Label(data, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def check():
        if ac.get() == "padmak-chord":
            d_host_entry.config(state="normal")
            d_user_entry.config(state="normal")
            d_pass_entry.config(state="normal")
            con_btn.config(state="normal")
        else:
            d_host_entry.config(state="disabled")
            d_user_entry.config(state="disabled")
            d_pass_entry.config(state="disabled")
            con_btn.config(state="disabled")

    fonts = ("Candara", 12)
    ac = Entry(data, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff", show="*")
    ac.place(x=75, y=532, width=291, height=34)
    ac.insert(0, " enter access key code ......")
    ac.bind("<KeyRelease>", lambda event: check())

    data_frame = Frame(data, width=477, height=508)
    data_frame.place(x=625, y=71)

    back = PhotoImage(file=current+"/.ux/login/.frame/Database_form.png")
    Background = Label(data_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    status = Label(data_frame, text=Access.stu, font=("Candara", 15), background="white", foreground="#1b2d52")
    status.place(x=258, y=433)

    # Entries
    fonts = ("Candara", 15)
    d_host_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff")
    d_host_entry.place(x=93, y=227, width=291, height=34)
    d_host_entry.insert(0, " Host")
    d_host_entry.config(state="disabled")

    d_user_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff")
    d_user_entry.place(x=93, y=275, width=291, height=34)
    d_user_entry.insert(0, " User")
    d_user_entry.config(state="disabled")

    d_pass_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff", show="*")
    d_pass_entry.place(x=93, y=323, width=291, height=34)
    d_pass_entry.insert(0, " Password")
    d_pass_entry.config(state="disabled")

    # noinspection PyBroadException
    def connect():
        mkey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
        winreg.SetValueEx(mkey, "Host", 0, winreg.REG_SZ, d_host_entry.get())
        winreg.SetValueEx(mkey, "User", 1, winreg.REG_SZ, d_user_entry.get())
        winreg.SetValueEx(mkey, "Pass", 2, winreg.REG_SZ, d_pass_entry.get())
        winreg.CloseKey(mkey)

        Key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
        Host = winreg.QueryValueEx(Key, "Host")[0]
        User = winreg.QueryValueEx(Key, "User")[0]
        Password = winreg.QueryValueEx(Key, "Pass")[0]
        winreg.CloseKey(Key)

        try:
            conn = mysql.connector.connect(host=Host,
                                           user=User,
                                           password=Password)
            conn.close()
            status.config(text="online")

        except:
            status.config(text="offline")

            messagebox.showerror("ERROR", "Connection Failed")

    # Buttons
    fonts = ("Candara", 15, "bold")
    con_btn = Button(data_frame, bg="#3b3086", fg="white", text="CONNECT", font=fonts, command=connect, bd=0
                     , state="disabled")
    con_btn.place(x=135, y=380, width=159, height=48)

    back_btn = Button(data_frame, bg="#ce4912", fg="white", text="↻", font=fonts, bd=0, state="disabled")
    back_btn.place(x=294, y=380, width=48, height=48)
