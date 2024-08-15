from tkinter import *
import winreg
from tkinter import messagebox
import mysql.connector
import os
import customtkinter

stu = "offline"
bt_status = "normal"


def acc():
    root = Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 954
    window_height = 508
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # root.geometry(geo)
    root.title("K-CHORD SOLUTIONS")
    root.iconbitmap("pad.ico")
    root.resizable(False, False)

    Mainframe = Frame(root, width=954, height=508)
    Mainframe.pack()

    current = os.path.dirname(os.path.realpath(__file__))
    a_back = PhotoImage(file=current + "/.ux/login/Access Back.png")
    a_Background = Label(Mainframe, image=a_back)
    a_Background.image = a_back
    a_Background.place(x=0, y=0, relheight=1, relwidth=1)

    def access(master):
        start_frame = Frame(master, width=477, height=508)
        start_frame.place(x=477)

        back = PhotoImage(file=current + "/.ux/login/.frame/Start_form.png")
        Background = Label(start_frame, image=back)
        Background.image = back
        Background.place(x=0, y=0, relheight=1, relwidth=1)

        global statuss
        statuss = Label(start_frame, text=stu, font=("Candara", 15), background="white", foreground="#1b2d52")
        statuss.place(x=265, y=386)

        fonts = ("Candara", 15, "bold")

        def log():
            start_frame.destroy()
            login(Mainframe)

        Start_btn = Button(start_frame, bg="#3b3086", fg="white", text="START", font=fonts, bd=0, command=log)
        Start_btn.place(x=83, y=325, width=159, height=48)
        root.bind("<Return>", lambda event=None: log())

        def load():
            start_frame.destroy()
            db(Mainframe)

        Db_btn = Button(start_frame, bg="#ce4912", fg="white", text="DATABASE", font=fonts, bd=0, command=load)
        Db_btn.place(x=249, y=325, width=159, height=48)
        Db_btn.config(state=bt_status)

    def db(master):
        data_frame = Frame(master, width=477, height=508)
        data_frame.place(x=477)

        back = PhotoImage(file=current + "/.ux/login/.frame/Database_form.png")
        Background = Label(data_frame, image=back)
        Background.image = back
        Background.place(x=0, y=0, relheight=1, relwidth=1)

        status = Label(data_frame, text=stu, font=("Candara", 15), background="white", foreground="#1b2d52")
        status.place(x=258, y=433)

        # Entries
        fonts = ("Candara", 15)
        d_host_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff")
        d_host_entry.place(x=93, y=227, width=291, height=34)
        d_host_entry.insert(0, " Host")

        d_user_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff")
        d_user_entry.place(x=93, y=275, width=291, height=34)
        d_user_entry.insert(0, " User")

        d_pass_entry = Entry(data_frame, fg="#1b2d52", font=fonts, bd=0, background="#f8fbff", show="*")
        d_pass_entry.place(x=93, y=323, width=291, height=34)
        d_pass_entry.insert(0, " Password")

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
        con_btn = Button(data_frame, bg="#3b3086", fg="white", text="CONNECT", font=fonts, command=connect, bd=0)
        con_btn.place(x=135, y=380, width=159, height=48)

        def back():
            root.destroy()
            import Splash
            Splash.er = 0

        back_btn = Button(data_frame, bg="#ce4912", fg="white", text="↻", font=fonts, bd=0, command=back)
        back_btn.place(x=294, y=380, width=48, height=48)

    def login(master):
        login_frame = Frame(master, width=477, height=508)
        login_frame.place(x=477)

        back = PhotoImage(file=current + "/.ux/login/.frame/Login_from.png")
        Background = Label(login_frame, image=back)
        Background.image = back
        Background.place(x=0, y=0, relheight=1, relwidth=1)

        def Signup():
            login_frame.destroy()
            signup(Mainframe)

        def Login():
            if switch.get() == "on":
                if login_nic_entry.get() == " Nic Number" or \
                        login_password_entry.get() == "" or login_nic_entry.get() == "":
                    messagebox.showerror("Error", "All Fields Required")
                else:
                    try:
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                        host = winreg.QueryValueEx(key, "Host")[0]
                        user = winreg.QueryValueEx(key, "User")[0]
                        password = winreg.QueryValueEx(key, "Pass")[0]
                        winreg.CloseKey(key)

                        con = mysql.connector.connect(host=host,
                                                      user=user,
                                                      password=password)
                        mycursor = con.cursor()
                        mycursor.execute("use pcc")
                    except:
                        messagebox.showerror("Error", "Database Fail")
                        return

                    query = "select * from admin where NIC=%s and Password=%s"
                    parameters = [login_nic_entry.get(), login_password_entry.get()]
                    mycursor.execute(query, parameters)
                    result = mycursor.fetchone()
                    con.close()
                    admin_nic = login_nic_entry.get()

                    if result is not None:
                        root.destroy()
                        import Admin
                        Admin.admin_nic = admin_nic
                        Admin.admin_name = result[1]
                        Admin.admin_rank = result[3]
                        import Teachers
                        Teachers.admin_nic = admin_nic
                        Teachers.admin_name = result[1]
                        Teachers.admin_rank = result[3]
                        import UI_WIN
                        UI_WIN.who = "admin"
                        UI_WIN.ui()
                    else:
                        messagebox.showerror("Error", "Incorrect Nic or Password")
                        forgot = Button(login_frame, text="forgot password ?", fg="#3b3086", bg="white", bd=0
                                        , activeforeground="red", activebackground="white", command=rp)
                        forgot.place(x=280, y=386)
            elif switch.get() == "off":
                if login_nic_entry.get() == " Nic Number" or \
                        login_password_entry.get() == "" or login_nic_entry.get() == "":
                    messagebox.showerror("Error", "All Fields Required")
                else:
                    try:
                        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                        host = winreg.QueryValueEx(key, "Host")[0]
                        user = winreg.QueryValueEx(key, "User")[0]
                        password = winreg.QueryValueEx(key, "Pass")[0]
                        winreg.CloseKey(key)

                        con = mysql.connector.connect(host=host,
                                                      user=user,
                                                      password=password)
                        mycursor = con.cursor()
                        mycursor.execute("use pcc")
                    except:
                        messagebox.showerror("Error", "Database Fail")
                        return

                    query = "select nic from grader where NIC=%s and pass=%s"
                    parameters = [login_nic_entry.get(), login_password_entry.get()]
                    mycursor.execute(query, parameters)
                    result = mycursor.fetchone()
                    con.close()

                    if result is not None:
                        x_n = login_nic_entry.get()
                        root.destroy()
                        """import Admin
                        Admin.admin_nic = admin_nic
                        Admin.admin_name = result[1]
                        Admin.admin_rank = result[3]
                        import Teachers
                        Teachers.admin_nic = admin_nic
                        Teachers.admin_name = result[1]
                        Teachers.admin_rank = result[3]"""
                        import UI_WIN
                        import Teachers
                        UI_WIN.who = "user"
                        UI_WIN.nic = x_n
                        Teachers.nic = x_n
                        Teachers.control = "normal"
                        UI_WIN.ui()
                    else:
                        messagebox.showerror("Error", "Incorrect Nic or Password")
                        forgot = Button(login_frame, text="forgot password ?", fg="#3b3086", bg="white", bd=0
                                        , activeforeground="red", activebackground="white", command=rp)
                        forgot.place(x=280, y=386)
            else:
                pass

        def rp():
            import Teachers
            Teachers.reset()

        # Entries
        def on_enter():
            login_nic_entry.select_range(0, END)

        def on_leave():
            var = login_nic_entry.get()
            if var == "":
                login_nic_entry.insert(0, " Nic Number")

        fonts = ("Candara", 12)
        login_nic_entry = Entry(login_frame, fg="#1b2d52", font=fonts, background="#f8fbff", bd=0)
        login_nic_entry.place(x=93, y=213, width=291, height=34)
        login_nic_entry.insert(0, " Nic Number")
        login_nic_entry.bind("<FocusIn>", lambda event: on_enter())
        login_nic_entry.bind("<FocusOut>", lambda event: on_leave())

        def pon_enter():
            login_password_entry.select_range(0, END)

        def pon_leave():
            var = login_password_entry.get()
            if var == "":
                login_password_entry.insert(0, " Password")

        login_password_entry = Entry(login_frame, fg="#1b2d52", font=fonts, background="#f8fbff", bd=0, show="*")
        login_password_entry.place(x=93, y=280, width=291, height=34)
        login_password_entry.insert(0, " Password")
        login_password_entry.bind("<FocusIn>", lambda event: pon_enter())
        login_password_entry.bind("<FocusOut>", lambda event: pon_leave())

        # Buttons
        fonts = ("Candara", 15, "bold")
        Login_btn = Button(login_frame, bg="#3b3086", fg="white", text="LOGIN", font=fonts, command=Login, bd=0)
        Login_btn.place(x=93, y=334, width=146, height=48)
        root.bind("<Return>", lambda event: Login())
        sign_btn = Button(login_frame, bg="#ce4912", fg="white", text="SIGN UP", font=fonts, command=Signup, bd=0)
        sign_btn.place(x=239, y=334, width=146, height=48)

        switch = customtkinter.CTkSwitch(login_frame, switch_width=44, switch_height=20, button_color="#3b3086",
                                         onvalue="on", offvalue="off", text="", bg_color="white"
                                         , progress_color="#ce4912", command=None)
        switch.place(x=340, y=176)

    def signup(master):
        sign_frame = Frame(master, width=477, height=508)
        sign_frame.place(x=477)

        back = PhotoImage(file=current + "/.ux/login/.frame/sign_from.png")
        Background = Label(sign_frame, image=back)
        Background.image = back
        Background.place(x=0, y=0, relheight=1, relwidth=1)

        def naon_enter():
            chord.select_range(0, END)

        def naon_leave():
            get = chord.get()
            if get == "":
                chord.insert(0, " enter access key code ......")

        def check():
            if chord.get() == "padmak-chord":
                signup_nic_entry.config(state="normal")
                signup_password_entry.config(state="normal")
            else:
                signup_nic_entry.config(state="disabled")
                signup_password_entry.config(state="disabled")

        fonts = ("Candara", 12)
        chord = Entry(sign_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff", show="*")
        chord.place(x=93, y=188, width=291, height=34)
        chord.insert(0, " enter access key code ......")
        chord.bind("<FocusIn>", lambda event: naon_enter())
        chord.bind("<FocusOut>", lambda event: naon_leave())
        chord.bind("<KeyRelease>", lambda event: check())

        def non_enter():
            signup_nic_entry.select_range(0, END)

        def non_leave():
            get = signup_nic_entry.get()
            if get == "":
                signup_nic_entry.insert(0, " Nic Number")

        signup_nic_entry = Entry(sign_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        signup_nic_entry.place(x=93, y=255, width=291, height=34)
        signup_nic_entry.insert(0, " Nic Number")
        signup_nic_entry.config(state="disabled")
        signup_nic_entry.bind("<FocusIn>", lambda event: non_enter())
        signup_nic_entry.bind("<FocusOut>", lambda event: non_leave())

        # signup_nic_entry.insert(0, " NIC")

        def pon_enter():
            signup_password_entry.select_range(0, END)

        def pon_leave():
            get = signup_password_entry.get()
            if get == "":
                signup_password_entry.insert(0, " Password")

        signup_password_entry = Entry(sign_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        signup_password_entry.place(x=93, y=323, width=291, height=34)
        signup_password_entry.insert(0, " Password")
        signup_password_entry.config(state="disabled")
        signup_password_entry.bind("<FocusIn>", lambda event: pon_enter())
        signup_password_entry.bind("<FocusOut>", lambda event: pon_leave())

        def add_data():
            if (signup_nic_entry.get() == " Nic Number" or signup_nic_entry.get() == "" or
                    signup_password_entry.get() == " Password" or signup_password_entry.get() == ""):
                messagebox.showerror("Error", "All Fields Required")
            else:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                    host = winreg.QueryValueEx(key, "Host")[0]
                    user = winreg.QueryValueEx(key, "User")[0]
                    password = winreg.QueryValueEx(key, "Pass")[0]
                    winreg.CloseKey(key)

                    con = mysql.connector.connect(host=host,
                                                  user=user,
                                                  password=password)
                    mycursor = con.cursor()
                except:
                    messagebox.showerror("Error", "Database Fail")
                    return
                try:
                    query = "create database pcc"
                    mycursor.execute(query)
                    query = "use pcc"
                    mycursor.execute(query)
                    query = "CREATE TABLE admin(NIC VARCHAR(100),Name VARCHAR(100),Password VARCHAR(100)" \
                            ",AdminRank VARCHAR(100))"
                    mycursor.execute(query)
                    con.commit()
                    print("ok")
                except:
                    mycursor.execute("use pcc")

                query = "select * from admin where NIC=%s"
                parameters = [signup_nic_entry.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()
                if result is not None:
                    messagebox.showerror("Error", "Already Have an Account, Please Login !")
                else:
                    print("ok")
                    query = "Insert into admin(NIC,Password) Values (%s,%s)"
                    parameters = [signup_nic_entry.get(), signup_password_entry.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS", "Admin Registered, Ahead To Login")

        def back():
            sign_frame.destroy()
            login(Mainframe)

        # Buttons
        fonts = ("Candara", 15, "bold")
        signup_btn = Button(sign_frame, bg="#3b3086", fg="white", text="SIGN UP", font=fonts, command=add_data, bd=0)
        signup_btn.place(x=135, y=380, width=159, height=48)
        sign_frame.bind("<Return>", lambda event=None: add_data())
        back_btn = Button(sign_frame, bg="#ce4912", fg="white", text="❮", font=fonts, command=back, bd=0)
        back_btn.place(x=294, y=380, width=48, height=48)
        sign_frame.bind("<Escape>", lambda event=None: back())

    access(Mainframe)

    root.mainloop()

# acc()
