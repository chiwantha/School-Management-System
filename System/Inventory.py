from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import winreg
import mysql.connector
from datetime import date
from fpdf import FPDF
from tkinter import filedialog
import os
from tkcalendar import DateEntry

Today = date.today()
Today = Today.strftime("%Y/%m/%d")
current = os.path.dirname(os.path.realpath(__file__))


def Add_Inventory(frame):
    In_add_frame = Frame(frame, height=651, width=1185)
    In_add_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.create/New Inventory.png")
    Background = Label(In_add_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def non_enter():
        In_Date.select_range(0, END)

    def non_leave():
        pass

    fonts = ("Candara", 13)
    In_Date = DateEntry(In_add_frame, selectmode="day", date_pattern="yyyy/mm/dd")
    In_Date.place(x=97, y=277, width=421, height=34)
    In_Date.bind("<FocusIn>", lambda event: non_enter())
    In_Date.bind("<FocusOut>", lambda event: non_leave())

    # In_Date.insert(0, " NIC")

    def naon_enter():
        In_ID.select_range(0, END)

    def naon_leave():
        get = In_ID.get()
        if get == "":
            In_ID.insert(0, " Inventory_ID (optional)")

    In_ID = Entry(In_add_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
    In_ID.place(x=97, y=362, width=421, height=34)
    In_ID.insert(0, " Inventory_ID (optional)")
    In_ID.bind("<FocusIn>", lambda event: naon_enter())
    In_ID.bind("<FocusOut>", lambda event: naon_leave())

    def pon_enter():
        In_Name.select_range(0, END)

    def pon_leave():
        get = In_Name.get()
        if get == "":
            In_Name.insert(0, " Inventory Name")

    In_Name = Entry(In_add_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
    In_Name.place(x=97, y=448, width=421, height=34)
    In_Name.insert(0, " Inventory Name")
    In_Name.bind("<FocusIn>", lambda event: pon_enter())
    In_Name.bind("<FocusOut>", lambda event: pon_leave())

    def puon_enter():
        In_purpose.select_range(0, END)

    def puon_leave():
        get = In_purpose.get()
        if get == "":
            In_purpose.insert(0, " Inventory Purpose")

    In_purpose = Entry(In_add_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
    In_purpose.place(x=97, y=538, width=421, height=34)
    In_purpose.insert(0, " Inventory Purpose")
    In_purpose.bind("<FocusIn>", lambda event: puon_enter())
    In_purpose.bind("<FocusOut>", lambda event: puon_leave())

    def add_inventory():
        if In_Date.get() == "" or \
                In_Name.get() == "" or \
                In_Name.get() == "Inventory Name" or \
                In_ID.get() == " Inventory_ID (optional)" or \
                In_ID.get() == "":
            messagebox.showerror("Error", "Name & Date Should Be Full-filled")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "CREATE TABLE inventory(date DATE, inventory_id varchar(50)," \
                        "name varchar(100), purpose varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from inventory where inventory_id=%s"
            parameters = [In_ID.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                messagebox.showerror("Error", "Inventory Id Already Exist")
            else:
                query = "insert into inventory values (%s,%s,%s,%s)"
                parameters = [In_Date.get(), In_ID.get(), In_Name.get(), In_purpose.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Data Added Successfully")

            con.close()

    def clear():
        In_ID.delete(0, END)
        In_ID.insert(0, " Inventory_ID (optional)")

        In_Name.delete(0, END)
        In_Name.insert(0, " Inventory Name")

        In_purpose.delete(0, END)
        In_purpose.insert(0, " Inventory Purpose")

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_add_frame, bg="#ce4912", fg="white", text="SUBMIT", font=fonts, bd=0, command=add_inventory)
    Submit_btn.place(x=578, y=277, width=159, height=48)
    Update_btn = Button(In_add_frame, bg="#3b3086", fg="white", text="UPDATE", font=fonts, bd=0)
    Update_btn.place(x=578, y=340, width=159, height=48)
    Clear_btn = Button(In_add_frame, bg="#3b3086", fg="white", text="CLEAR", font=fonts, bd=0, command=clear)
    Clear_btn.place(x=578, y=403, width=159, height=48)

    # disable(In_add_frame)


def Add_Books(frame):
    In_book_frame = Frame(frame, height=651, width=1185)
    In_book_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.create_books/aDD bOOKS.png")
    Background = Label(In_book_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    try:
        def ao():
            Date.select_range(0, END)

        def al():
            pass

        fonts = ("Candara", 13)
        Date = DateEntry(In_book_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Date.place(x=84, y=272, width=223, height=34)
        Date.bind("<FocusIn>", lambda event: ao())
        Date.bind("<FocusOut>", lambda event: al())

        def bo():
            Inventory_id.select_range(0, END)

        def bl():
            get = Inventory_id.get()
            if get == "":
                Inventory_id.insert(0, " Enter Inventory Id")

        Inventory_id = Entry(In_book_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Inventory_id.place(x=84, y=350, width=187, height=34)
        Inventory_id.insert(0, " Enter Inventory Id")
        Inventory_id.bind("<FocusIn>", lambda event: bo())
        Inventory_id.bind("<FocusOut>", lambda event: bl())
        Inventory_id.bind("<KeyRelease>", lambda event: (get_name(), collect()))

        def get_name():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "CREATE TABLE inventory(date DATE, inventory_id varchar(50)," \
                        "name varchar(50), purpose varchar(50))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from inventory where inventory_id = %s"
            parameters = [Inventory_id.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                Inventory_name.configure(text=result[2])
            else:
                Inventory_name.configure(text=" Inventory Name")

        Inventory_name = Label(In_book_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff", text=" Inventory Name"
                               , anchor=W)
        Inventory_name.place(x=362, y=350, width=319, height=34)

        def co():
            Book_id.select_range(0, END)

        def cl():
            get = Book_id.get()
            if get == "":
                Book_id.insert(0, " Enter Book Id (optional)")

        Book_id = Entry(In_book_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Book_id.place(x=84, y=431, width=223, height=34)
        Book_id.insert(0, " Enter Book Id (optional)")
        Book_id.bind("<FocusIn>", lambda event: co())
        Book_id.bind("<FocusOut>", lambda event: cl())

        def do():
            Book_name.select_range(0, END)

        def dl():
            get = Book_name.get()
            if get == "":
                Book_name.insert(0, " Enter Book Name")

        Book_name = Entry(In_book_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Book_name.place(x=362, y=431, width=319, height=34)
        Book_name.insert(0, " Enter Book Name")
        Book_name.bind("<FocusIn>", lambda event: do())
        Book_name.bind("<FocusOut>", lambda event: dl())

        def eo():
            Book_Note.select_range(0, END)

        def el():
            get = Book_Note.get()
            if get == "":
                Book_Note.insert(0, " Enter Book Description")

        Book_Note = Entry(In_book_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Book_Note.place(x=84, y=515, width=595, height=34)
        Book_Note.insert(0, " Enter Book Description")
        Book_Note.bind("<FocusIn>", lambda event: eo())
        Book_Note.bind("<FocusOut>", lambda event: el())
    except:
        pass

    view = ttk.Treeview(In_book_frame)
    view.place(x=741, y=276, height=304, width=339)

    view["columns"] = ("Date", "Book Id", "Book Name")
    view["show"] = "headings"

    view.column("Date", minwidth=40, width=40)
    view.column("Book Id", minwidth=15, width=30, anchor=CENTER)
    view.column("Book Name", minwidth=100, width=150)
    view.heading("Date", text="Created Date")
    view.heading("Book Id", text="Book ID")
    view.heading("Book Name", text="Book Name")

    def add_data():
        if Date.get() == "" or \
                Inventory_id.get() == "" or Inventory_id.get() == " Enter Inventory Id" or \
                Book_id.get() == "" or Book_id.get() == " Enter Book Id (optional)" or \
                Book_name.get() == "" or Book_name.get() == " Enter Book Name":
            messagebox.showerror("Error", "Add Data Required ( Note is Optional )")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                        "book_name varchar(100), book_note varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from inventory where inventory_id = %s"
            parameters = [Inventory_id.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                query = "select * from inventory_book where inventory_id = %s and book_id = %s"
                parameters = [Inventory_id.get(), Book_id.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()

                if result is not None:
                    messagebox.showerror("Error", "This Book already Exist !")
                    con.close()
                else:
                    query = "insert into inventory_book values (%s,%s,%s,%s,%s)"
                    Name = Book_name.get()
                    Name = Name.upper()
                    parameters = [Date.get(), Inventory_id.get(), Book_id.get(), Name, Book_Note.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Data Added Successfully")
                    collect()
            else:
                messagebox.showerror("Error", "No Inventory Found with Id You Entered !")
            con.close()

    def delete():
        if Inventory_id.get() == "" or Inventory_id.get() == " Enter Inventory Id" or \
                Book_id.get() == "" or Book_id.get() == " Enter Book Id (optional)":
            messagebox.showerror("Error", "Inventory Id & Book Id Required")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select * from inventory_book where inventory_id=%s and book_id=%s"
            parameters = [Inventory_id.get(), Book_id.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                respond = messagebox.askyesno("Are Toy Sure ?", "This will Delete Your All Data In This Book !")
                if respond:
                    query = "delete from inventory_book where inventory_id=%s and book_id=%s"
                    parameters = [Inventory_id.get(), Book_id.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                else:
                    con.close()
                    pass
            else:
                messagebox.showerror("Error", "Invalid Index or No Book exist with id you entered !")
            con.close()
            collect()

    def collect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                    "book_name varchar(50), book_note varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from inventory_book where inventory_id = %s"
        parameters = [Inventory_id.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=1, iid=counter, text="", values=(row[0], row[2], row[3]))
        else:
            value = "No Data"
            view.insert(parent="", index=1, iid=1, text="", values=value)
        con.close()

    def clear():
        Inventory_id.delete(0, END)
        Book_id.delete(0, END)
        Book_name.delete(0, END)
        Book_Note.delete(0, END)

        Inventory_id.insert(0, " Enter Inventory Id")
        Book_id.insert(0, " Enter Book Id (optional)")
        Book_name.insert(0, " Enter Book Name")
        Book_Note.insert(0, " Enter Book Description")

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_book_frame, bg="#ce4912", fg="white", text="SUBMIT", font=fonts, bd=0, command=add_data)
    Submit_btn.place(x=81, y=587, width=172, height=34)
    Update_btn = Button(In_book_frame, bg="#3b3086", fg="white", text="DELETE", font=fonts, bd=0, command=delete)
    Update_btn.place(x=273, y=587, width=172, height=34)
    Clear_btn = Button(In_book_frame, bg="#3b3086", fg="white", text="CLEAR", font=fonts, bd=0, command=clear)
    Clear_btn.place(x=465, y=587, width=172, height=34)


def Receive(frame):
    In_Receive_frame = Frame(frame, height=651, width=1185)
    In_Receive_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.receive/Receive.png")
    Background = Label(In_Receive_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    # Support Classes
    def Book_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                    "book_name varchar(100), book_note varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select book_name from inventory_book where inventory_book.inventory_id=%s"
        parameters = [Inventory_ID.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Book.configure(values=value)
        else:
            pass

    def Item_category_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                    "book_name varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select item_category from category where book_name=%s"
        parameters = [Book.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Item_category.configure(values=value)
        else:
            pass

    def new_item_category():
        if Item_category.get() == "" or Item_category.get() == " Item Category":
            pass
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                        "book_name varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from category where item_category=%s and book_name=%s"
            item_cat = Item_category.get()
            item_cat = item_cat.upper()
            parameters = [item_cat, Book.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                pass
            else:
                query = "insert into category (item_category,book_name) values (%s,%s)"
                parameters = [item_cat, Book.get()]
                mycursor.execute(query, parameters)
                con.commit()
            con.close()
        Item_category_collect()

    def Item_model_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select item_model from model where item_category=%s"
            parameters = [Item_category.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Item_Model.configure(values=value)
            else:
                pass
        except:
            pass

    def new_item_model():
        if Item_Model.get() == "" or Item_Model.get() == " Item Model":
            pass
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table model(item_id int AUTO_INCREMENT PRIMARY KEY, item_model varchar(100)," \
                        "item_category varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from model where item_category=%s and item_model=%s"
            item_mod = Item_Model.get()
            item_mod = item_mod.upper()
            parameters = [Item_category.get(), Item_Model.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                pass
            else:
                query = "insert into model (item_category,item_model) values (%s,%s)"
                parameters = [Item_category.get(), item_mod]
                mycursor.execute(query, parameters)
                con.commit()
            con.close()
        Item_model_collect()

    def sponsor_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select name from sponsor"
            mycursor.execute(query)
            result = mycursor.fetchall()
            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                From.configure(values=value)
            else:
                pass
        except:
            pass

    def new_sponsor():
        if From.get() == "" or From.get() == " eg: Mr. Upali Gunarathne":
            pass
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table sponsor(id int AUTO_INCREMENT PRIMARY KEY, name varchar(200)," \
                        "item_id varchar(50), quantity varchar(10), telephone varchar(15),address varchar(200))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from sponsor where name=%s"
            wfrom = From.get()
            wfrom = wfrom.upper()
            parameters = [wfrom]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                pass
            else:
                query = "insert into sponsor (name) values (%s)"
                parameters = [wfrom]
                mycursor.execute(query, parameters)
                con.commit()
            con.close()
        sponsor_collect()

    # Entries
    try:
        fonts = ("Calibri", 12)
        Date = DateEntry(In_Receive_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Date.place(x=45, y=168, width=218, height=34)

        def bo():
            From.select_range(0, END)

        def bl():
            get = From.get()
            if get == "":
                From.insert(0, " eg: Mr. Upali Gunarathne")

        From = ttk.Combobox(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        From.place(x=295, y=168, width=284, height=34)
        sponsor_collect()
        From.insert(0, " eg: Mr. Upali Gunarathne")
        From.bind("<FocusIn>", lambda event: bo())
        From.bind("<FocusOut>", lambda event: bl())

        def io():
            Inventory_ID.select_range(0, END)

        def il():
            get = Inventory_ID.get()
            if get == "":
                Inventory_ID.insert(0, " eg: 01....")

        Inventory_ID = Entry(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Inventory_ID.place(x=610, y=168, width=165, height=34)
        Inventory_ID.insert(0, " eg: 01....")
        Inventory_ID.bind("<FocusIn>", lambda event: io())
        Inventory_ID.bind("<FocusOut>", lambda event: il())
        Inventory_ID.bind("<KeyRelease>", lambda event: Book_collect())

        def co():
            Quantity.select_range(0, END)

        def cl():
            get = Quantity.get()
            if get == "":
                Quantity.insert(0, " eg: 18")

        Quantity = Entry(In_Receive_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Quantity.place(x=805, y=168, width=120, height=34)
        Quantity.insert(0, " eg: 18")
        Quantity.bind("<FocusIn>", lambda event: co())
        Quantity.bind("<FocusOut>", lambda event: cl())

        def do():
            Book.select_range(0, END)

        def dl():
            get = Book.get()
            if get == "":
                Book.insert(0, " Book Name")

        Book = ttk.Combobox(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=45, y=249, width=218, height=34)
        Book.insert(0, " Book Name")
        Book.bind("<FocusIn>", lambda event: do())
        Book.bind("<FocusOut>", lambda event: dl())
        Book.bind("<KeyRelease>", lambda event: Item_category_collect())
        Book.bind("<<ComboboxSelected>>", lambda event: Item_category_collect())

        def eo():
            Item_Id.select_range(0, END)

        def el():
            get = Item_Id.get()
            if get == "":
                Item_Id.insert(0, " Item Id")

        Item_Id = Entry(In_Receive_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Item_Id.place(x=295, y=249, width=90, height=34)
        Item_Id.insert(0, " Auto")
        Item_Id.bind("<FocusIn>", lambda event: eo())
        Item_Id.bind("<FocusOut>", lambda event: el())
        Item_Id.configure(state="disabled")

        def fo():
            Item_category.select_range(0, END)

        def fl():
            get = Item_category.get()
            if get == "":
                Item_category.insert(0, " Item Category")

        Item_category = ttk.Combobox(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_category.place(x=415, y=249, width=165, height=34)
        Item_category.insert(0, " Item Category")
        Item_category.bind("<FocusIn>", lambda event: fo())
        Item_category.bind("<FocusOut>", lambda event: fl())
        Item_category.bind("<KeyRelease>", lambda event: Item_model_collect())
        Item_category.bind("<<ComboboxSelected>>", lambda event: Item_model_collect())

        def go():
            Item_Model.select_range(0, END)

        def gl():
            get = Item_Model.get()
            if get == "":
                Item_Model.insert(0, " Item Model")

        Item_Model = ttk.Combobox(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model.place(x=610, y=249, width=165, height=34)
        Item_Model.insert(0, " Item Model")
        Item_Model.bind("<FocusIn>", lambda event: go())
        Item_Model.bind("<FocusOut>", lambda event: gl())

        def ho():
            Item_Model_Diss.select_range(0, END)

        def hl():
            get = Item_Model_Diss.get()
            if get == "":
                Item_Model_Diss.insert(0, " Item Model Diss (optional)")

        Item_Model_Diss = ttk.Combobox(In_Receive_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model_Diss.place(x=805, y=249, width=273, height=34)
        Item_Model_Diss.insert(0, " Item Model Diss (optional)")
        Item_Model_Diss.bind("<FocusIn>", lambda event: ho())
        Item_Model_Diss.bind("<FocusOut>", lambda event: hl())
    except:
        pass

    view = ttk.Treeview(In_Receive_frame)
    view.place(x=26, y=340, width=1129, height=294)

    view["columns"] = ("Date", "From Whom", "Quantity", "Book", "ItemID", "Item", "Model", "Model Diss")
    view["show"] = "headings"

    view.column("Date", minwidth=20, width=20)
    view.column("From Whom", minwidth=75, width=150)
    view.column("Quantity", minwidth=10, width=10, anchor=CENTER)
    view.column("Book", minwidth=50, width=75)
    view.column("ItemID", minwidth=10, width=10, anchor=CENTER)
    view.column("Item", minwidth=20, width=50)
    view.column("Model", minwidth=20, width=50)
    view.column("Model Diss", minwidth=50, width=75)

    view.heading("Date", text="Date")
    view.heading("From Whom", text="From Whom")
    view.heading("Quantity", text="Quantity")
    view.heading("Book", text="Book")
    view.heading("ItemID", text="ItemID")
    view.heading("Item", text="Item")
    view.heading("Model", text="Model")
    view.heading("Model Diss", text="Model Diss")

    def collect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table receive(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from receive"
        mycursor.execute(query)
        result = mycursor.fetchall()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7]))
        else:
            pass

    collect()

    def submit_live():
        new_item_category()
        new_item_model()
        new_sponsor()

        if From.get() == "" or From.get() == " eg: Mr. Upali Gunarathne" or \
                Inventory_ID.get() == "" or Inventory_ID.get() == " eg: 01...." or \
                Quantity.get() == "" or Quantity.get() == " eg: 18" or \
                Book.get() == "" or Book.get() == " Book Name" or \
                Item_category.get() == "" or Item_category.get() == " Item Category" or \
                Item_Model.get() == "" or Item_Model.get() == " Item Model":
            messagebox.showerror("Error", "all data required (item diss is optional)")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                        "200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select quantity from live_inventory where book=%s and item_category=%s and item_model=%s"
            I_c = Item_category.get()
            I_c = I_c.upper()
            I_m = Item_Model.get()
            I_m = I_m.upper()
            parameters = [Book.get(), I_c, I_m]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                # print(result[0])
                quantity = int(result[0])
                new = Quantity.get()
                new = int(new)
                value = quantity + new
                I_c = Item_category.get()
                I_c = I_c.upper()
                I_m = Item_Model.get()
                I_m = I_m.upper()

                query = "update live_inventory set quantity=%s, date=%s where book=%s and item_category=%s and " \
                        "item_model=%s"
                parameters = [value, Today, Book.get(), I_c, I_m]
                mycursor.execute(query, parameters)
                con.commit()
            else:
                try:
                    query = "insert into live_inventory (date,whom,quantity,book,item_category,item_model,item_diss)" \
                            " values (%s,%s,%s,%s,%s,%s,%s)"
                    whom = From.get()
                    whom = whom.upper()
                    I_c = Item_category.get()
                    I_c = I_c.upper()
                    I_m = Item_Model.get()
                    I_m = I_m.upper()
                    parameters = [Date.get(), whom, Quantity.get(), Book.get(), I_c, I_m,
                                  Item_Model_Diss.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    # messagebox.showinfo("Success", "Data Added Successfully")
                except:
                    messagebox.showerror("Error", "Data Insert Unsuccessful")
                    con.close()
        collect()

    def submit():
        new_item_category()
        new_item_model()
        new_sponsor()

        if From.get() == "" or From.get() == " eg: Mr. Upali Gunarathne" or \
                Inventory_ID.get() == "" or Inventory_ID.get() == " eg: 01...." or \
                Quantity.get() == "" or Quantity.get() == " eg: 18" or \
                Book.get() == "" or Book.get() == " Book Name" or \
                Item_category.get() == "" or Item_category.get() == " Item Category" or \
                Item_Model.get() == "" or Item_Model.get() == " Item Model":
            messagebox.showerror("Error", "all data required (item diss is optional)")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            if Item_Model_Diss.get() == " Item Model Diss (optional)":
                Item_Model_Diss.delete(0, END)
            else:
                pass

            try:
                query = "create table receive(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                        "200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = "insert into receive (date,whom,quantity,book,item_category,item_model,item_diss)" \
                        " values (%s,%s,%s,%s,%s,%s,%s)"
                whom = From.get()
                whom = whom.upper()
                I_c = Item_category.get()
                I_c = I_c.upper()
                I_m = Item_Model.get()
                I_m = I_m.upper()
                parameters = [Date.get(), whom, Quantity.get(), Book.get(), I_c, I_m,
                              Item_Model_Diss.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                submit_live()
                messagebox.showinfo("Success", "Data Added Successfully")
            except:
                messagebox.showerror("Error", "Data Insert Unsuccessful")
                con.close()
        collect()

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_Receive_frame, bg="#ce4912", fg="white", text="+", font=fonts, bd=0, command=submit)
    Submit_btn.place(x=1085, y=249, width=34, height=34)


def Live(frame):
    In_Live_frame = Frame(frame, height=651, width=1185)
    In_Live_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.live/live_inventory.png")
    Background = Label(In_Live_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def switch():
        if onoff['bg'] == 'red':
            onoff['bg'] = 'green'
            onoff.configure(text="i")
            Inventory_ID.configure(state="normal")
            Book.configure(state="normal")
            Item_category.configure(state="normal")
            Item_Model.configure(state="normal")
            Datein.configure(state="normal")
            Dateout.configure(state="normal")

        else:
            onoff['bg'] = 'red'
            onoff.configure(text="o")
            Inventory_ID.configure(state="disabled")
            Book.configure(state="disabled")
            Item_category.configure(state="disabled")
            Item_Model.configure(state="disabled")
            Datein.configure(state="disabled")
            Dateout.configure(state="disabled")

    onoff = Button(In_Live_frame, text="o", background="red", bd=1, foreground="white", font=("Candara", 12, "bold"))
    onoff.configure(command=switch)
    onoff.place(x=1114, y=230, width=24, height=24)

    try:
        def make():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                        "200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
                con.close()
            except:
                pass
        make()

        def Min():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "SELECT min(date) FROM live_inventory"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result is not None:
                Datein.delete(0, END)
                Datein.set_date(result[0])

            con.close()

        def Max():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "SELECT max(date) FROM live_inventory"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result is not None:
                Dateout.delete(0, END)
                Dateout.set_date(result[0])

        def Book_collect():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                        "book_name varchar(100), book_note varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select book_name from inventory_book where inventory_book.inventory_id=%s"
            parameters = [Inventory_ID.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Book.configure(values=value)
            else:
                pass

        def Item_category_collect():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                        "book_name varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select item_category from category where book_name=%s"
            parameters = [Book.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Item_category.configure(values=value)
            else:
                pass

        def Item_model_collect():
            try:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                    host = winreg.QueryValueEx(key, "Host")[0]
                    user = winreg.QueryValueEx(key, "User")[0]
                    password = winreg.QueryValueEx(key, "Pass")[0]
                    winreg.CloseKey(key)

                    con = mysql.connector.connect(host=host,
                                                  user=user,
                                                  password=password,
                                                  database="pcc")
                    mycursor = con.cursor()
                    # print("connection ok !")
                except:
                    messagebox.showerror("Error", "DataBase Failed")
                    return

                query = "select item_model from model where item_category=%s"
                parameters = [Item_category.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchall()

                value = []
                if result is not None:
                    for row in result:
                        value.append(row[0].strip("{}\""))
                    Item_Model.configure(values=value)
                else:
                    pass
            except:
                pass

        def ao():
            # Datein.select_range(0, END)
            pass

        fonts = ("Calibri", 12)
        Datein = DateEntry(In_Live_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Datein.place(x=977, y=291, width=146, height=27)
        try:
            Min()
        except:
            pass
        Datein.configure(state="disabled")
        Datein.bind("<FocusIn>", lambda event: ao())

        def aoo():
            # Dateout.select_range(0, END)
            pass

        Dateout = DateEntry(In_Live_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Dateout.place(x=977, y=351, width=146, height=27)
        try:
            Max()
        except:
            pass
        Dateout.configure(state="disabled")
        Dateout.bind("<FocusIn>", lambda event: aoo())

        Datein.bind("<<DateEntrySelected>>", lambda event: filter_data())
        Dateout.bind("<<DateEntrySelected>>", lambda event: filter_data())

        def io():
            Inventory_ID.select_range(0, END)

        def il():
            get = Inventory_ID.get()
            if get == "":
                Inventory_ID.insert(0, " eg: 01....")

        Inventory_ID = Entry(In_Live_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Inventory_ID.place(x=977, y=411, width=131, height=27)
        Inventory_ID.insert(0, " eg: 01....")
        Inventory_ID.bind("<FocusIn>", lambda event: io())
        Inventory_ID.bind("<FocusOut>", lambda event: il())
        Inventory_ID.configure(state="disabled")
        Inventory_ID.bind("<KeyRelease>", lambda event: Book_collect())

        def do():
            Book.select_range(0, END)

        Book = ttk.Combobox(In_Live_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=977, y=471, width=146, height=27)
        Book.bind("<FocusIn>", lambda event: do())
        Book.configure(state="disabled")
        Book.bind("<KeyRelease>", lambda event: (Item_category_collect(), filter_data()))
        Book.bind("<<ComboboxSelected>>", lambda event: (Item_category_collect(), filter_data()))

        def fo():
            Item_category.select_range(0, END)

        Item_category = ttk.Combobox(In_Live_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_category.place(x=977, y=530, width=131, height=27)
        Item_category.bind("<FocusIn>", lambda event: fo())
        Item_category.configure(state="disabled")
        Item_category.bind("<KeyRelease>", lambda event: (Item_model_collect(), filter_data()))
        Item_category.bind("<<ComboboxSelected>>", lambda event: (Item_model_collect(), filter_data()))

        def go():
            Item_Model.select_range(0, END)

        Item_Model = ttk.Combobox(In_Live_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model.place(x=977, y=590, width=131, height=27)
        Item_Model.bind("<FocusIn>", lambda event: go())
        Item_Model.configure(state="disabled")
        Item_Model.bind("<KeyRelease>", lambda event: filter_data())
        Item_Model.bind("<<ComboboxSelected>>", lambda event: filter_data())
    except:
        pass

    def filter_data():
        for item in view_live.get_children():
            view_live.delete(item)

        query = "select * from live_inventory"
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if Book is not None and Book.get():
            if ext == "":
                ext = "where book like '%" + Book.get() + "%'"
            else:
                ext += " and book like '%" + Book.get() + "%'"

        if Item_category is not None and Item_category.get():
            if ext == "":
                ext = "where item_category like '%" + Item_category.get() + "%'"
            else:
                ext += " and item_category like '%" + Item_category.get() + "%'"

        if Item_Model is not None and Item_Model.get():
            if ext == "":
                ext = "where item_model like '%" + Item_Model.get() + "%'"
            else:
                ext += " and item_model like '%" + Item_Model.get() + "%'"

        filtered = query + " " + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        mycursor.execute(filtered)
        result = mycursor.fetchall()
        con.close()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view_live.insert(parent="", index=0, iid=counter, text="",
                                 values=(row[1], row[0], row[4], row[3], row[5],
                                         row[6], row[7]))
        else:
            pass

    def collect():
        for item in view_live.get_children():
            view_live.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                    "200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from live_inventory"
        mycursor.execute(query)
        result = mycursor.fetchall()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view_live.insert(parent="", index=0, iid=counter, text="",
                                 values=(row[1], row[0], row[4], row[3], row[5],
                                         row[6], row[7]))
        else:
            pass
        con.close()

    view_live = ttk.Treeview(In_Live_frame)
    view_live.place(x=21, y=124, width=914, height=508)

    collect()

    view_live["columns"] = ("Date", "ItemID", "Book", "Quantity", "Item", "Model", "Model Diss")
    view_live["show"] = "headings"

    view_live.column("Date", minwidth=20, width=20, anchor=CENTER)
    view_live.column("ItemID", minwidth=10, width=10, anchor=CENTER)
    view_live.column("Book", minwidth=50, width=50)
    view_live.column("Quantity", minwidth=10, width=10, anchor=CENTER)
    view_live.column("Item", minwidth=50, width=50)
    view_live.column("Model", minwidth=50, width=75)
    view_live.column("Model Diss", minwidth=75, width=100)

    view_live.heading("Date", text="Last Update Date")
    view_live.heading("ItemID", text="ItemID")
    view_live.heading("Book", text="Book")
    view_live.heading("Quantity", text="Quantity")
    view_live.heading("Item", text="Item")
    view_live.heading("Model", text="Model")
    view_live.heading("Model Diss", text="Model Diss")

    def export():
        query = "select * from live_inventory"
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if Book is not None and Book.get():
            if ext == "":
                ext = "where book like '%" + Book.get() + "%'"
            else:
                ext += " and book like '%" + Book.get() + "%'"

        if Item_category is not None and Item_category.get():
            if ext == "":
                ext = "where item_category like '%" + Item_category.get() + "%'"
            else:
                ext += " and item_category like '%" + Item_category.get() + "%'"

        if Item_Model is not None and Item_Model.get():
            if ext == "":
                ext = "where item_model like '%" + Item_Model.get() + "%'"
            else:
                ext += " and item_model like '%" + Item_Model.get() + "%'"

        filtered = query + " " + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            cursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        cursor.execute(filtered)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Live Inventory", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        con.close()

    fonts = ("Candara", 15, "bold")
    BTN = Button(In_Live_frame, text="Export", command=export, bg="#ce4912", fg="white", font=fonts)
    BTN.place(x=959, y=169, width=194, height=27)


def receive_view(frame):
    In_r_frame = Frame(frame, height=651, width=1185)
    In_r_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.receive_view/Receive Viewer.png")
    Background = Label(In_r_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def make():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table receive(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100))"
            mycursor.execute(query)
            con.commit()
            con.close()
        except:
            pass

    make()

    def Min():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT min(date) FROM receive"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result is not None:
            Datein.delete(0, END)
            Datein.insert(0, result[0])

        con.close()

    def Max():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT max(date) FROM receive"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result is not None:
            Dateout.delete(0, END)
            Dateout.insert(0, result[0])

    def Book_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                    "book_name varchar(100), book_note varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select book_name from inventory_book where inventory_book.inventory_id=%s"
        parameters = [Inventory_ID.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Book.configure(values=value)
        else:
            pass

    def Item_category_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                    "book_name varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select item_category from category where book_name=%s"
        parameters = [Book.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Item_category.configure(values=value)
        else:
            pass

    def Item_model_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select item_model from model where item_category=%s"
            parameters = [Item_category.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Item_Model.configure(values=value)
            else:
                pass
        except:
            pass

    def sponsor_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select name from sponsor"
            mycursor.execute(query)
            result = mycursor.fetchall()
            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                From.configure(values=value)
            else:
                pass
        except:
            pass

    try:
        fonts = ("Calibri", 12)
        Datein = DateEntry(In_r_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Datein.place(x=44, y=156, width=142, height=29)
        try:
            Min()
        except:
            pass

        Dateout = DateEntry(In_r_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Dateout.place(x=205, y=156, width=142, height=29)
        try:
            Max()
        except:
            pass

        Datein.bind("<<DateEntrySelected>>", lambda event: filter_data())
        Dateout.bind("<<DateEntrySelected>>", lambda event: filter_data())

        def bo():
            From.select_range(0, END)

        From = ttk.Combobox(In_r_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        From.place(x=365, y=156, width=202, height=29)
        sponsor_collect()
        From.bind("<FocusIn>", lambda event: bo())
        From.bind("<KeyRelease>", lambda event: filter_data())
        From.bind("<<ComboboxSelected>>", lambda event: filter_data())

        def io():
            Inventory_ID.select_range(0, END)

        Inventory_ID = Entry(In_r_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Inventory_ID.place(x=587, y=156, width=44, height=29)
        Inventory_ID.insert(0, "0")
        Inventory_ID.bind("<FocusIn>", lambda event: io())
        Inventory_ID.bind("<KeyRelease>", lambda event: Book_collect())

        def do():
            Book.select_range(0, END)

        Book = ttk.Combobox(In_r_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=649, y=156, width=138, height=29)
        Book.bind("<FocusIn>", lambda event: do())
        Book.bind("<KeyRelease>", lambda event: (Item_category_collect(), filter_data()))
        Book.bind("<<ComboboxSelected>>", lambda event: (Item_category_collect(), filter_data()))
        Book_collect()

        def fo():
            Item_category.select_range(0, END)

        Item_category = ttk.Combobox(In_r_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_category.place(x=804, y=156, width=130, height=29)
        Item_category.bind("<FocusIn>", lambda event: fo())
        Item_category.bind("<KeyRelease>", lambda event: (Item_model_collect(), filter_data()))
        Item_category.bind("<<ComboboxSelected>>", lambda event: (Item_model_collect(), filter_data()))

        def go():
            Item_Model.select_range(0, END)

        Item_Model = ttk.Combobox(In_r_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model.place(x=954, y=156, width=182, height=29)
        Item_Model.bind("<FocusIn>", lambda event: go())
        Item_Model.bind("<KeyRelease>", lambda event: filter_data())
        Item_Model.bind("<<ComboboxSelected>>", lambda event: filter_data())
    except:
        pass

    def filter_data():
        for item in view.get_children():
            view.delete(item)

        query = "select * from receive "
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if From.get() is not None:
            if ext != "":
                ext += " AND whom like '%" + From.get() + "%'"
            else:
                ext = "WHERE whom like '%" + From.get() + "%'"

        if Book.get() is not None:
            if ext != "":
                ext += " AND book like '%" + Book.get() + "%'"
            else:
                ext = "WHERE book like '%" + Book.get() + "%'"

        if Item_category.get() is not None:
            if ext != "":
                ext += " AND item_category like '%" + Item_category.get() + "%'"
            else:
                ext = "WHERE item_category like '%" + Item_category.get() + "%'"

        if Item_Model.get() is not None:
            if ext != "":
                ext += " AND item_model like '%" + Item_Model.get() + "%'"
            else:
                ext = "WHERE item_model like '%" + Item_Model.get() + "%'"

        filtered = query + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        mycursor.execute(filtered)
        result = mycursor.fetchall()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7]))
        else:
            pass
        con.close()

    view = ttk.Treeview(In_r_frame)
    view.place(x=26, y=232, width=1129, height=402)

    view["columns"] = ("Date", "From Whom", "Quantity", "Book", "ItemID", "Item", "Model", "Model Diss")
    view["show"] = "headings"

    view.column("Date", minwidth=20, width=20)
    view.column("From Whom", minwidth=75, width=150)
    view.column("Quantity", minwidth=10, width=10, anchor=CENTER)
    view.column("Book", minwidth=50, width=75)
    view.column("ItemID", minwidth=10, width=10, anchor=CENTER)
    view.column("Item", minwidth=20, width=50)
    view.column("Model", minwidth=20, width=50)
    view.column("Model Diss", minwidth=50, width=75)

    view.heading("Date", text="Date")
    view.heading("From Whom", text="From Whom")
    view.heading("Quantity", text="Quantity")
    view.heading("Book", text="Book")
    view.heading("ItemID", text="ItemID")
    view.heading("Item", text="Item")
    view.heading("Model", text="Model")
    view.heading("Model Diss", text="Model Diss")

    def collect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table receive(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from receive"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7]))
        else:
            pass

    collect()

    def export():
        query = "select * from receive "
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if From.get() is not None:
            if ext != "":
                ext += " AND whom like '%" + From.get() + "%'"
            else:
                ext = "WHERE whom like '%" + From.get() + "%'"

        if Book.get() is not None:
            if ext != "":
                ext += " AND book like '%" + Book.get() + "%'"
            else:
                ext = "WHERE book like '%" + Book.get() + "%'"

        if Item_category.get() is not None:
            if ext != "":
                ext += " AND item_category like '%" + Item_category.get() + "%'"
            else:
                ext = "WHERE item_category like '%" + Item_category.get() + "%'"

        if Item_Model.get() is not None:
            if ext != "":
                ext += " AND item_model like '%" + Item_Model.get() + "%'"
            else:
                ext = "WHERE item_model like '%" + Item_Model.get() + "%'"

        filtered = query + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            cursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        cursor.execute(filtered)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Inventory Receive", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        con.close()

    fonts = ("Candara", 15, "bold")
    BTN = Button(In_r_frame, text="Export", command=export, bg="#ce4912", fg="white", font=fonts)
    BTN.place(x=1091, y=8, width=84, height=27)


def expend_view(frame):
    In_e_frame = Frame(frame, height=651, width=1185)
    In_e_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.expend_view/Expend Viewer.png")
    Background = Label(In_e_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def make():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table expend(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100), status varchar(50))"
            mycursor.execute(query)
            con.commit()
            con.close()
        except:
            pass

    make()

    def Min():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT min(date) FROM expend"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result is not None:
            Datein.delete(0, END)
            Datein.insert(0, result[0])

        con.close()

    def Max():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT max(date) FROM expend"
        mycursor.execute(query)
        result = mycursor.fetchone()
        if result is not None:
            Dateout.delete(0, END)
            Dateout.insert(0, result[0])

    def Book_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table inventory_book(date DATE, inventory_id varchar(50), book_id varchar(30)," \
                    "book_name varchar(100), book_note varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select book_name from inventory_book where inventory_book.inventory_id=%s"
        parameters = [Inventory_ID.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Book.configure(values=value)
        else:
            pass

    def Item_category_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                    "book_name varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select item_category from category where book_name=%s"
        parameters = [Book.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Item_category.configure(values=value)
        else:
            pass

    def Item_model_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select item_model from model where item_category=%s"
            parameters = [Item_category.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Item_Model.configure(values=value)
            else:
                pass
        except:
            pass

    def expender_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select name from expender"
            mycursor.execute(query)
            result = mycursor.fetchall()
            con.close()
            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                From.configure(values=value)
            else:
                pass
        except:
            pass

    try:
        fonts = ("Calibri", 12)
        Datein = DateEntry(In_e_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Datein.place(x=44, y=156, width=142, height=29)
        try:
            Min()
        except:
            pass

        Dateout = DateEntry(In_e_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Dateout.place(x=205, y=156, width=142, height=29)
        try:
            Max()
        except:
            pass

        Datein.bind("<<DateEntrySelected>>", lambda event: filter_data())
        Dateout.bind("<<DateEntrySelected>>", lambda event: filter_data())

        def bo():
            From.select_range(0, END)

        From = ttk.Combobox(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        From.place(x=365, y=156, width=202, height=29)
        expender_collect()
        From.bind("<FocusIn>", lambda event: bo())
        From.bind("<KeyRelease>", lambda event: filter_data())
        From.bind("<<ComboboxSelected>>", lambda event: filter_data())

        def io():
            Inventory_ID.select_range(0, END)

        Inventory_ID = Entry(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Inventory_ID.place(x=587, y=156, width=44, height=29)
        Inventory_ID.insert(0, "0")
        Inventory_ID.bind("<FocusIn>", lambda event: io())
        Inventory_ID.bind("<KeyRelease>", lambda event: Book_collect())

        def do():
            Book.select_range(0, END)

        Book = ttk.Combobox(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=649, y=156, width=138, height=29)
        Book.bind("<FocusIn>", lambda event: do())
        Book.bind("<KeyRelease>", lambda event: (Item_category_collect(), filter_data()))
        Book.bind("<<ComboboxSelected>>", lambda event: (Item_category_collect(), filter_data()))
        Book_collect()

        def fo():
            Item_category.select_range(0, END)

        Item_category = ttk.Combobox(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_category.place(x=804, y=156, width=130, height=29)
        Item_category.bind("<FocusIn>", lambda event: fo())
        Item_category.bind("<KeyRelease>", lambda event: (Item_model_collect(), filter_data()))
        Item_category.bind("<<ComboboxSelected>>", lambda event: (Item_model_collect(), filter_data()))

        def go():
            Item_Model.select_range(0, END)

        Item_Model = ttk.Combobox(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model.place(x=954, y=156, width=182, height=29)
        Item_Model.bind("<FocusIn>", lambda event: go())
        Item_Model.bind("<KeyRelease>", lambda event: filter_data())
        Item_Model.bind("<<ComboboxSelected>>", lambda event: filter_data())

        def eo():
            Status.select_range(0, END)

        values = ["REPAIR", "DESTROY", "AUCTION", "TRANSFER"]
        Status = ttk.Combobox(In_e_frame, foreground="#1b2d52", font=fonts, background="#f8fbff", values=values)
        Status.place(x=1004, y=90, width=130, height=29)
        Status.bind("<FocusIn>", lambda event: eo())
        Status.bind("<KeyRelease>", lambda event: filter_data())
        Status.bind("<<ComboboxSelected>>", lambda event: filter_data())
    except:
        pass

    def filter_data():
        for item in view.get_children():
            view.delete(item)

        query = "select * from expend "
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if From.get() is not None:
            if ext != "":
                ext += " AND whom like '%" + From.get() + "%'"
            else:
                ext = "WHERE whom like '%" + From.get() + "%'"

        if Book.get() is not None:
            if ext != "":
                ext += " AND book like '%" + Book.get() + "%'"
            else:
                ext = "WHERE book like '%" + Book.get() + "%'"

        if Item_category.get() is not None:
            if ext != "":
                ext += " AND item_category like '%" + Item_category.get() + "%'"
            else:
                ext = "WHERE item_category like '%" + Item_category.get() + "%'"

        if Item_Model.get() is not None:
            if ext != "":
                ext += " AND item_model like '%" + Item_Model.get() + "%'"
            else:
                ext = "WHERE item_model like '%" + Item_Model.get() + "%'"

        if Status.get() is not None:
            if ext != "":
                ext += " AND status like '%" + Status.get() + "%'"
            else:
                ext = "WHERE status like '%" + Status.get() + "%'"

        filtered = query + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        mycursor.execute(filtered)
        result = mycursor.fetchall()
        con.close()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7], row[8]))
        else:
            pass

    view = ttk.Treeview(In_e_frame)
    view.place(x=26, y=232, width=1129, height=402)

    view["columns"] = ("Date", "From Whom", "Quantity", "Book", "ItemID", "Item", "Model", "Model Diss", "Status")
    view["show"] = "headings"

    view.column("Date", minwidth=20, width=20)
    view.column("From Whom", minwidth=75, width=150)
    view.column("Quantity", minwidth=10, width=10, anchor=CENTER)
    view.column("Book", minwidth=50, width=75)
    view.column("ItemID", minwidth=10, width=10, anchor=CENTER)
    view.column("Item", minwidth=20, width=50)
    view.column("Model", minwidth=20, width=50)
    view.column("Model Diss", minwidth=50, width=75)
    view.column("Status", minwidth=50, width=75)

    view.heading("Date", text="Date")
    view.heading("From Whom", text="From Whom")
    view.heading("Quantity", text="Quantity")
    view.heading("Book", text="Book")
    view.heading("ItemID", text="ItemID")
    view.heading("Item", text="Item")
    view.heading("Model", text="Model")
    view.heading("Model Diss", text="Model Diss")
    view.heading("Status", text="Status")

    def collect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table expend(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100), status varchar(50))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from expend"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7], row[8]))
        else:
            pass

    collect()

    def export():
        query = "select * from expend "
        ext = ""

        if Datein.get() is not None and Dateout.get() is not None:
            if ext != "":
                ext += " AND date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"
            else:
                ext = "WHERE date BETWEEN '" + Datein.get() + "' AND '" + Dateout.get() + "'"

        if From.get() is not None:
            if ext != "":
                ext += " AND whom like '%" + From.get() + "%'"
            else:
                ext = "WHERE whom like '%" + From.get() + "%'"

        if Book.get() is not None:
            if ext != "":
                ext += " AND book like '%" + Book.get() + "%'"
            else:
                ext = "WHERE book like '%" + Book.get() + "%'"

        if Item_category.get() is not None:
            if ext != "":
                ext += " AND item_category like '%" + Item_category.get() + "%'"
            else:
                ext = "WHERE item_category like '%" + Item_category.get() + "%'"

        if Item_Model.get() is not None:
            if ext != "":
                ext += " AND item_model like '%" + Item_Model.get() + "%'"
            else:
                ext = "WHERE item_model like '%" + Item_Model.get() + "%'"

        if Status.get() is not None:
            if ext != "":
                ext += " AND status like '%" + Status.get() + "%'"
            else:
                ext = "WHERE status like '%" + Status.get() + "%'"

        filtered = query + ext

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            cursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        cursor.execute(filtered)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Inventory Expend", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        con.close()

    fonts = ("Candara", 15, "bold")
    BTN = Button(In_e_frame, text="Export", command=export, bg="#ce4912", fg="white", font=fonts)
    BTN.place(x=1091, y=8, width=84, height=27)


def Expend(frame):
    In_Expend_frame = Frame(frame, height=651, width=1185)
    In_Expend_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.expend/expend.png")
    Background = Label(In_Expend_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def Book_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "select book_name from inventory_book where inventory_book.inventory_id=%s"
        parameters = [Inventory_ID.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Book.configure(values=value)
        else:
            pass

    def Item_category_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table category(item_id int AUTO_INCREMENT PRIMARY KEY, item_category varchar(100)," \
                    "book_name varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select item_category from category where book_name=%s"
        parameters = [Book.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Item_category.configure(values=value)
        else:
            pass

    def Item_model_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select item_model from model where item_category=%s"
            parameters = [Item_category.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()

            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Item_Model.configure(values=value)
            else:
                pass
        except:
            pass

    def expender_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select name from expender"
            mycursor.execute(query)
            result = mycursor.fetchall()
            con.close()
            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                Tow.configure(values=value)
            else:
                pass
        except:
            pass

    def new_expender():
        if Tow.get() == "" or Tow.get() == " eg: Mr. Upali Gunarathne":
            pass
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table expender(id int AUTO_INCREMENT PRIMARY KEY, name varchar(50))"

                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from expender where name=%s"
            wfrom = Tow.get()
            wfrom = wfrom.upper()
            parameters = [wfrom]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                pass
            else:
                query = "insert into expender (name) values (%s)"
                parameters = [wfrom]
                mycursor.execute(query, parameters)
                con.commit()
            con.close()
        expender_collect()

    try:
        fonts = ("Calibri", 12)
        Date = DateEntry(In_Expend_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Date.place(x=45, y=168, width=218, height=34)

        def bo():
            Tow.select_range(0, END)

        def bl():
            get = Tow.get()
            if get == "":
                Tow.insert(0, " eg: Mr. Upali Gunarathne")

        Tow = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Tow.place(x=295, y=168, width=284, height=34)
        expender_collect()
        Tow.insert(0, " eg: Mr. Upali Gunarathne")
        Tow.bind("<FocusIn>", lambda event: bo())
        Tow.bind("<FocusOut>", lambda event: bl())

        def io():
            Inventory_ID.select_range(0, END)

        def il():
            get = Inventory_ID.get()
            if get == "":
                Inventory_ID.insert(0, " eg: 01....")

        Inventory_ID = Entry(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Inventory_ID.place(x=610, y=168, width=165, height=34)
        Inventory_ID.insert(0, " eg: 01....")
        Inventory_ID.bind("<FocusIn>", lambda event: io())
        Inventory_ID.bind("<FocusOut>", lambda event: il())
        Inventory_ID.bind("<KeyRelease>", lambda event: Book_collect())

        def co():
            Quantity.select_range(0, END)

        def cl():
            get = Quantity.get()
            if get == "":
                Quantity.insert(0, " eg: 18")

        Quantity = Entry(In_Expend_frame, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
        Quantity.place(x=805, y=168, width=120, height=34)
        Quantity.insert(0, " eg: 18")
        Quantity.bind("<FocusIn>", lambda event: co())
        Quantity.bind("<FocusOut>", lambda event: cl())

        def do():
            Book.select_range(0, END)

        def dl():
            get = Book.get()
            if get == "":
                Book.insert(0, " Book Name")

        Book = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=45, y=249, width=218, height=34)
        Book.insert(0, " Book Name")
        Book.bind("<FocusIn>", lambda event: do())
        Book.bind("<FocusOut>", lambda event: dl())
        Book.bind("<KeyRelease>", lambda event: Item_category_collect())
        Book.bind("<<ComboboxSelected>>", lambda event: Item_category_collect())

        def eo():
            Status.select_range(0, END)

        def el():
            get = Status.get()
            if get == "":
                Status.set(values[0])
        values = ["INUSE", "REPAIR", "DESTROY", "AUCTION", "TRANSFER"]
        Status = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff", values=values)
        Status.place(x=295, y=249, width=90, height=34)
        Status.set(values[0])
        Status.bind("<FocusIn>", lambda event: eo())
        Status.bind("<FocusOut>", lambda event: el())

        def fo():
            Item_category.select_range(0, END)

        def fl():
            get = Item_category.get()
            if get == "":
                Item_category.insert(0, " Item Category")

        Item_category = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_category.place(x=415, y=249, width=165, height=34)
        Item_category.insert(0, " Item Category")
        Item_category.bind("<FocusIn>", lambda event: fo())
        Item_category.bind("<FocusOut>", lambda event: fl())
        Item_category.bind("<KeyRelease>", lambda event: Item_model_collect())
        Item_category.bind("<<ComboboxSelected>>", lambda event: Item_model_collect())

        def go():
            Item_Model.select_range(0, END)

        def gl():
            get = Item_Model.get()
            if get == "":
                Item_Model.insert(0, " Item Model")

        Item_Model = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model.place(x=610, y=249, width=165, height=34)
        Item_Model.insert(0, " Item Model")
        Item_Model.bind("<FocusIn>", lambda event: go())
        Item_Model.bind("<FocusOut>", lambda event: gl())

        def ho():
            Item_Model_Diss.select_range(0, END)

        def hl():
            get = Item_Model_Diss.get()
            if get == "":
                Item_Model_Diss.insert(0, " Item Model Diss (optional)")

        Item_Model_Diss = ttk.Combobox(In_Expend_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Item_Model_Diss.place(x=805, y=249, width=273, height=34)
        Item_Model_Diss.insert(0, " Item Model Diss (optional)")
        Item_Model_Diss.bind("<FocusIn>", lambda event: ho())
        Item_Model_Diss.bind("<FocusOut>", lambda event: hl())
    except:
        pass

    view = ttk.Treeview(In_Expend_frame)
    view.place(x=26, y=340, width=1129, height=294)

    view["columns"] = ("Date", "From Whom", "Quantity", "Book", "ItemID", "Item", "Model", "Model Diss", "Status")
    view["show"] = "headings"

    view.column("Date", minwidth=20, width=20)
    view.column("From Whom", minwidth=75, width=150)
    view.column("Quantity", minwidth=10, width=10, anchor=CENTER)
    view.column("Book", minwidth=50, width=75)
    view.column("ItemID", minwidth=10, width=10, anchor=CENTER)
    view.column("Item", minwidth=20, width=50)
    view.column("Model", minwidth=20, width=50)
    view.column("Model Diss", minwidth=50, width=75)
    view.column("Status", minwidth=50, width=75)

    view.heading("Date", text="Date")
    view.heading("From Whom", text="From Whom")
    view.heading("Quantity", text="Quantity")
    view.heading("Book", text="Book")
    view.heading("ItemID", text="ItemID")
    view.heading("Item", text="Item")
    view.heading("Model", text="Model")
    view.heading("Model Diss", text="Model Diss")
    view.heading("Status", text="Status")

    def collect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table expend(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                    "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                    "item_diss varchar(100), status varchar(50))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from expend"
        mycursor.execute(query)
        result = mycursor.fetchall()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[1], row[2], row[3], row[4], row[0],
                                                                              row[5], row[6], row[7], row[8]))
        else:
            pass

    collect()

    def submit_live():
        if Tow.get() == "" or Tow.get() == " eg: Mr. Upali Gunarathne" or \
                Inventory_ID.get() == "" or Inventory_ID.get() == " eg: 01...." or \
                Quantity.get() == "" or Quantity.get() == " eg: 18" or \
                Book.get() == "" or Book.get() == " Book Name" or \
                Item_category.get() == "" or Item_category.get() == " Item Category" or \
                Item_Model.get() == "" or Item_Model.get() == " Item Model":
            messagebox.showerror("Error", "all data required (item diss is optional)")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                        "200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select quantity from live_inventory where book=%s and item_category=%s and item_model=%s"
            I_c = Item_category.get()
            I_c = I_c.upper()
            I_m = Item_Model.get()
            I_m = I_m.upper()
            parameters = [Book.get(), I_c, I_m]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                # print(result[0])
                quantity = int(result[0])
                new = Quantity.get()
                new = int(new)
                value = quantity - new
                I_c = Item_category.get()
                I_c = I_c.upper()
                I_m = Item_Model.get()
                I_m = I_m.upper()

                query = "update live_inventory set quantity=%s, date=%s where book=%s and item_category=%s and " \
                        "item_model=%s"
                parameters = [value, Today, Book.get(), I_c, I_m]
                mycursor.execute(query, parameters)
                con.commit()
            else:
                try:
                    query = "insert into live_inventory (date,whom,quantity,book,item_category,item_model,item_diss)" \
                            " values (%s,%s,%s,%s,%s,%s,%s)"
                    whom = Tow.get()
                    whom = whom.upper()
                    I_c = Item_category.get()
                    I_c = I_c.upper()
                    I_m = Item_Model.get()
                    I_m = I_m.upper()
                    parameters = [Date.get(), whom, Quantity.get(), Book.get(), I_c, I_m,
                                  Item_Model_Diss.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    # messagebox.showinfo("Success", "Data Added Successfully")
                except:
                    messagebox.showerror("Error", "Data Insert Unsuccessful")
                    con.close()
        collect()

    def submit():
        if Tow.get() == "" or Tow.get() == " eg: Mr. Upali Gunarathne" or \
                Inventory_ID.get() == "" or Inventory_ID.get() == " eg: 01...." or \
                Quantity.get() == "" or Quantity.get() == " eg: 18" or \
                Book.get() == "" or Book.get() == " Book Name" or \
                Item_category.get() == "" or Item_category.get() == " Item Category" or \
                Item_Model.get() == "" or Item_Model.get() == " Item Model":
            messagebox.showerror("Error", "all data required (item diss is optional)")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            if Item_Model_Diss.get() == " Item Model Diss (optional)":
                Item_Model_Diss.delete(0, END)
            else:
                pass

            try:
                query = "create table expend(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100), status varchar(50))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = "create table live_inventory(item_id int AUTO_INCREMENT PRIMARY KEY, date DATE, whom varchar(" \
                        "200)," \
                        "quantity int(4), book varchar(100), item_category varchar(100), item_model varchar(100)," \
                        "item_diss varchar(100))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = "insert into expend (date,whom,quantity,book,item_category,item_model,item_diss,status)" \
                        " values (%s,%s,%s,%s,%s,%s,%s,%s)"
                whom = Tow.get()
                whom = whom.upper()
                I_c = Item_category.get()
                I_c = I_c.upper()
                I_m = Item_Model.get()
                I_m = I_m.upper()
                parameters = [Date.get(), whom, Quantity.get(), Book.get(), I_c, I_m,
                              Item_Model_Diss.get(), Status.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                submit_live()
                messagebox.showinfo("Success", "Data Added Successfully")
            except:
                messagebox.showerror("Error", "Data Insert Unsuccessful")
                con.close()
        new_expender()
        collect()

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_Expend_frame, bg="#ce4912", fg="white", text="+", font=fonts, bd=0, command=submit)
    Submit_btn.place(x=1085, y=249, width=34, height=34)


def Sponsor(frame):
    In_sponsor_frame = Frame(frame, height=651, width=1185)
    In_sponsor_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.sponsor/inventory sponsor.png")
    Background = Label(In_sponsor_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def sponsor_collect():
        try:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select name from sponsor"
            mycursor.execute(query)
            result = mycursor.fetchall()
            value = []
            if result is not None:
                for row in result:
                    value.append(row[0].strip("{}\""))
                name.configure(values=value)
            else:
                pass
        except:
            pass

    try:
        fonts = ("Calibri", 12)

        def bo():
            name.select_range(0, END)

        def bl():
            get = name.get()
            if get == "":
                name.insert(0, " Choose your Sponsor Here..")

        name = ttk.Combobox(In_sponsor_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        name.place(x=33, y=133, width=247, height=34)
        sponsor_collect()
        name.insert(0, " Choose your Sponsor Here..")
        name.config(state="readonly")
        name.bind("<FocusIn>", lambda event: bo())
        name.bind("<FocusOut>", lambda event: bl())

        def io():
            contact.select_range(0, END)

        def il():
            get = contact.get()
            if get == "":
                contact.insert(0, " Contact..")

        def validate_entry(text):
            if len(text) > 10:
                return False
            return True

        validate_command = In_sponsor_frame.register(validate_entry)

        contact = Entry(In_sponsor_frame, foreground="#1b2d52", font=fonts, background="#f8fbff", validate="key",
                        validatecommand=(validate_command, "%P"))
        contact.place(x=338, y=133, width=146, height=34)
        contact.insert(0, " Contact..")
        contact.bind("<FocusIn>", lambda event: io())
        contact.bind("<FocusOut>", lambda event: il())

        def ko():
            address.select_range(0, END)

        def kl():
            get = address.get()
            if get == "":
                address.insert(0, " Address (line one)")

        address = Entry(In_sponsor_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        address.place(x=506, y=133, width=209, height=34)
        address.insert(0, " Address (line one)")
        address.bind("<FocusIn>", lambda event: ko())
        address.bind("<FocusOut>", lambda event: kl())

        def vo():
            line2.select_range(0, END)

        def vl():
            get = line2.get()
            if get == "":
                line2.insert(0, " Line 2 (Optional)")

        line2 = Entry(In_sponsor_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        line2.place(x=737, y=133, width=190, height=34)
        line2.insert(0, " Line 2 (Optional)")
        line2.bind("<FocusIn>", lambda event: vo())
        line2.bind("<FocusOut>", lambda event: vl())
    except:
        pass

    def collect():
        for item in view.get_children():
            view.delete(item)

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table sponsor(id int AUTO_INCREMENT PRIMARY KEY, name varchar(50)," \
                    "item_id varchar(50), quantity varchar(10), telephone varchar(15),address varchar(100))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from sponsor"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        if result is not None:
            for result in result:
                count += 1
                view.insert(parent="", index=1, iid=count, values=(result[0], result[1], "Null", "Null"
                                                                   , result[4], result[5]))
        else:
            pass

    def update_data():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "select * from sponsor where name=%s"
        parameters = [name.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()

        if result is not None:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "update sponsor set telephone=%s , address=%s where name=%s"

            if line2.get() == " Line 2 (Optional)" or line2.get() == "":
                adl = address.get()
            else:
                adl = address.get()+", "+line2.get()

            parameters = [contact.get(), adl, name.get()]
            mycursor.execute(query, parameters)
            con.commit()
            con.close()
            collect()
        else:
            messagebox.showerror("Error", "Sponsor not found !, please choose from the list !")
            con.close()

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_sponsor_frame, bg="#ce4912", fg="white", text="+", font=fonts, bd=0, command=update_data)
    Submit_btn.place(x=284, y=133, width=34, height=34)

    def add():
        messagebox.showerror("Error", "You Can't add Sponsor Directly !")

    add_btn = Button(In_sponsor_frame, bg="#3b3086", fg="white", text="Add New", font=fonts, bd=0, command=add)
    add_btn.place(x=590, y=187, width=159, height=38)

    def remove():
        respond = messagebox.askyesno("confirm", "Are You Sure ?")
        if respond:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor()
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select * from sponsor where name=%s"
            parameters = [name.get()]
            mycursor.execute(query, parameters)
            res = mycursor.fetchone()

            if res is not None:
                query = "delete from sponsor where name=%s"
                parameters = [name.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                collect()
            else:
                messagebox.showerror("Error", "Sponsor Not Found !")

    re_btn = Button(In_sponsor_frame, bg="#ce4912", fg="white", text="Remove", font=fonts, bd=0, command=remove)
    re_btn.place(x=768, y=187, width=159, height=38)

    view = ttk.Treeview(In_sponsor_frame)
    view.place(x=33, y=242, width=1119, height=379)

    view["columns"] = ("id", "name", "iid", "quantity", "contact", "address")
    view["show"] = "headings"

    collect()

    view.column("id", minwidth=10, width=20, anchor=CENTER)
    view.column("name", minwidth=100, width=150)
    view.column("iid", minwidth=20, width=50, anchor=CENTER)
    view.column("quantity", minwidth=10, width=15, anchor=CENTER)
    view.column("contact", minwidth=30, width=50)
    view.column("address", minwidth=75, width=100)

    view.heading("id", text="ID")
    view.heading("name", text="Name")
    view.heading("iid", text="Item_ID")
    view.heading("quantity", text="Quantity")
    view.heading("contact", text="Contact")
    view.heading("address", text="Address")


def About(frame):
    In_about_frame = Frame(frame, height=651, width=1185)
    In_about_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.about/about inventory.png")
    Background = Label(In_about_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)


def Report(frame):
    In_report_frame = Frame(frame, height=651, width=1185)
    In_report_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.report/inventory report.png")
    Background = Label(In_report_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def live_report():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           database="pcc")
            cursor = conn.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT * FROM live_inventory"
        cursor.execute(query)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Live Inventory", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        conn.close()

    def receive_report():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           database="pcc")
            cursor = conn.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT * FROM receive"
        cursor.execute(query)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Inventory Receive", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        conn.close()

    def expend_report():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           database="pcc")
            cursor = conn.cursor(buffered=True)
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "SELECT * FROM expend"
        cursor.execute(query)
        results = cursor.fetchall()

        pdf = FPDF(orientation='L', unit='mm')
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Arial", size=30, style='B')
        pdf.add_page()

        title_x = 20
        title_y = 10
        pdf.set_xy(title_x, title_y)
        pdf.cell(0, 10, "Padmawathie National Collage - Inventory Expend", ln=True, align='L')

        subtitle_x = 50
        subtitle_y = title_y + 15
        pdf.set_xy(subtitle_x, subtitle_y)
        pdf.set_font("Arial", size=0, style='I')
        pdf.cell(0, 10, "", ln=True, align='L')

        # Set font and font size for table content
        pdf.set_font("Arial", size=8)
        # Calculate column widths
        header = [i[0] for i in cursor.description]  # Get column names from cursor
        column_widths = [pdf.get_string_width(str(header[i])) for i in range(len(header))]

        # Iterate over the results and update column widths
        for row in results:
            for i in range(len(row)):
                width = pdf.get_string_width(str(row[i]))
                if width > column_widths[i]:
                    column_widths[i] = width

        # Calculate total table width
        table_width = sum(column_widths)

        # Calculate starting position to fit the table from side to side
        start_x = (pdf.w - table_width) / 12

        # Set column widths and display the table
        pdf.set_x(start_x)
        margin = 2  # Define the margin value

        # Add the table headings
        for header_name, width in zip(header, column_widths):
            pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False, align='C')  # Adjusted cell width

        pdf.ln()

        for row in results:
            # Check if adding a new row will exceed the page height
            if pdf.get_y() + 10 > pdf.h - 10:
                pdf.add_page()  # Add a new page
                pdf.set_xy(start_x, 10)  # Set position for the table on the new page

                # Add the column headers
                for header_name, width in zip(header, column_widths):
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

                pdf.ln()

            # Display the row
            pdf.set_x(start_x)
            for i in range(len(row)):
                pdf.cell(column_widths[i] + 2 * margin, 10, str(row[i]), border=1, ln=False,
                         align='C')  # Adjusted cell width
            pdf.ln()

        save_location = filedialog.asksaveasfilename(
            title="Select a file",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("PDF", "*.pdf")],
            defaultextension=".pdf"
        )
        if save_location == "":
            pass
        else:
            pdf.output(save_location)

        cursor.close()
        conn.close()

    fonts = ("Candara", 15, "bold")

    res_btn = Button(In_report_frame, bg="#3b3086", fg="white", text="Generate", font=fonts, bd=0
                     , command=receive_report)
    res_btn.place(x=134, y=566, width=159, height=38)

    exp_btn = Button(In_report_frame, bg="#3b3086", fg="white", text="Generate", font=fonts, bd=0
                     , command=expend_report)
    exp_btn.place(x=517, y=566, width=159, height=38)

    liv_btn = Button(In_report_frame, bg="#ce4912", fg="white", text="Generate", font=fonts, bd=0
                     , command=live_report)
    liv_btn.place(x=891, y=566, width=159, height=38)


def Guardian(frame):
    In_guardian_frame = Frame(frame, height=651, width=1185)
    In_guardian_frame.pack()

    back = PhotoImage(file=current+"/.ux/inventory/.guardian/Book Guardian.png")
    Background = Label(In_guardian_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def Book_collect():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        query = "select book_name from inventory_book"
        mycursor.execute(query)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0].strip("{}\""))
            Book.configure(values=value)
        else:
            pass

    def collect_teacher(text):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "CREATE TABLE teacher(" \
                    "id VARCHAR(100),nic VARCHAR(100), family_name VARCHAR(100), first_name VARCHAR(100)," \
                    "last_name VARCHAR(100),full_name varchar(200),gender VARCHAR(10),e_mail VARCHAR(100)," \
                    "pone_number VARCHAR(10)," \
                    "sub1 VARCHAR(100),sub2 VARCHAR(100), dob Date,address VARCHAR(100),address_line VARCHAR(100)," \
                    "city VARCHAR(50))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select full_name from teacher where nic"\
                " like '%" + text + "%' or full_name like '%" + text + "%'"
        mycursor.execute(query)
        result = mycursor.fetchall()

        value = []
        if result is not None:
            for row in result:
                value.append(row[0])
            Teacher.configure(values=value)
        else:
            pass

    try:
        fonts = ("Calibri", 12)

        def bo():
            Teacher.select_range(0, END)

        def bl():
            get = Teacher.get()
            if get == "":
                Teacher.insert(0, " Guardian (Nic or Name)")

        Teacher = ttk.Combobox(In_guardian_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Teacher.place(x=34, y=163, width=247, height=34)
        Teacher.insert(0, " Guardian (Nic or Name)")
        Teacher.bind("<FocusIn>", lambda event: bo())
        Teacher.bind("<FocusOut>", lambda event: bl())
        Teacher.bind("<KeyRelease>", lambda event: collect_teacher(Teacher.get()))

        def io():
            Book.select_range(0, END)

        def il():
            get = Book.get()
            if get == "":
                Book.insert(0, " Book")

        Book = ttk.Combobox(In_guardian_frame, foreground="#1b2d52", font=fonts, background="#f8fbff")
        Book.place(x=347, y=163, width=196, height=34)
        Book.insert(0, " Book")
        Book.bind("<FocusIn>", lambda event: io())
        Book.bind("<FocusOut>", lambda event: il())
        Book_collect()
        Book.configure(state="readonly")

        Start = DateEntry(In_guardian_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        Start.place(x=560, y=163, width=179, height=34)

        End = DateEntry(In_guardian_frame, selectmode="day", date_pattern="dd/mm/yyyy")
        End.place(x=753, y=163, width=179, height=34)
    except:
        pass

    def coollect():
        for item in view.get_children():
            view.delete(item)
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host,
                                          user=user,
                                          password=password,
                                          database="pcc")
            mycursor = con.cursor()
            # print("connection ok !")
        except:
            messagebox.showerror("Error", "DataBase Failed")
            return

        try:
            query = "create table guardian(teacher varchar(200),book varchar(100),start_date DATE,"\
                    "end_date varchar(15))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from guardian"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            count += 1
            view.insert(parent="", index=0, iid=count, text="", values=(row[0], row[1], row[2], row[3]))

    def update_data():
        if Teacher.get() == " Guardian (Nic or Name)" or Teacher.get() == "" or Book.get() == "" \
                or Book.get() == " Book" or Start.get() == "" or Start.get() == " Start Date":
            messagebox.showerror("Error", "Make sure all fields are full-filled")
        else:
            if End.get() == "End Date" or End.get() == "":
                end_date = ""
            else:
                end_date = End.get()

            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host,
                                              user=user,
                                              password=password,
                                              database="pcc")
                mycursor = con.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "create table guardian(teacher varchar(200),book varchar(100),start_date DATE,"\
                        "end_date varchar(15))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select full_name from teacher where full_name=%s"
            parameter = [Teacher.get()]
            mycursor.execute(query, parameter)
            res = mycursor.fetchone()

            if res is not None:
                query = "select * from guardian where teacher=%s and book=%s"
                parameters = [Teacher.get(), Book.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()

                if result is not None:
                    query = "update guardian set book=%s, start_date=%s, end_date=%s where teacher=%s"
                    parameters = [Book.get(), Start.get(), end_date, Teacher.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    messagebox.showinfo("success", "Data Updated")
                else:
                    query = "insert into guardian values (%s,%s,%s,%s)"
                    parameters = [Teacher.get(), Book.get(), Start.get(), end_date]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    messagebox.showinfo("success", "Data added")
            else:
                messagebox.showinfo("Error", "Teacher Not Found !")
            con.close()
        coollect()

    fonts = ("Candara", 15, "bold")
    Submit_btn = Button(In_guardian_frame, bg="#ce4912", fg="white", text="+", font=fonts, bd=0, command=update_data)
    Submit_btn.place(x=287, y=163, width=51, height=34)

    view = ttk.Treeview(In_guardian_frame)
    view.place(x=33, y=255, width=1119, height=366)

    coollect()

    view["columns"] = ("t", "b", "s", "e")
    view["show"] = "headings"

    view.column("t", minwidth=100, width=150)
    view.column("b", minwidth=50, width=100)
    view.column("s", minwidth=30, width=50, anchor=CENTER)
    view.column("e", minwidth=30, width=50, anchor=CENTER)

    view.heading("t", text="Teacher/Guardian Name")
    view.heading("b", text="Book Name")
    view.heading("s", text="Start Date")
    view.heading("e", text="End Date")
