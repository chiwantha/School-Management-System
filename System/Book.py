from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import winreg
import mysql.connector
import Library
import os

today = datetime.today()
today = today.strftime("%Y/%m/%d")
current_path = os.path.dirname(os.path.realpath(__file__))


def Book_Menu(frame):
    BM = Frame(frame, height=651, width=1185)
    BM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.menu/Libbook Menu.png")
    Background = Label(BM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    change = Frame(BM, height=552, width=684)
    change.place(x=501, y=99)

    back = PhotoImage(file=current_path + "/.ux./library/.book/.mc/mc.png")
    Background = Label(change, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def clear():
        for item in change.winfo_children():
            item.destroy()

    new_btn = Button(BM, text="New", activeforeground="gray", font=("Impact", 15), bd=0
                     , bg="#302f3f", activebackground="#302f3f", fg="White"
                     , command=lambda: (clear(), New(change)))
    new_btn.place(x=191, y=264, width=175, height=31)

    edit_btn = Button(BM, text="Search", activeforeground="gray", font=("Impact", 15), bd=0
                      , bg="#302f3f", activebackground="#302f3f", fg="White"
                      , command=lambda: (clear(), Edit(change)))
    edit_btn.place(x=191, y=310, width=175, height=31)

    in_btn = Button(BM, text="Inventory", activeforeground="gray", font=("Impact", 15), bd=0
                    , bg="#302f3f", activebackground="#302f3f", fg="White"
                    , command=lambda: (clear(), Inventory(change)))
    in_btn.place(x=191, y=356, width=175, height=31)

    author_btn = Button(BM, text="Author", activeforeground="gray", font=("Impact", 15), bd=0
                        , bg="#302f3f", activebackground="#302f3f", fg="White"
                        , command=lambda: (clear(), author(change)))
    author_btn.place(x=191, y=403, width=175, height=31)

    search_btn = Button(BM, text="Other", activeforeground="gray", font=("Impact", 15), bd=0
                        , bg="#302f3f", activebackground="#302f3f", fg="White"
                        , command=lambda: (clear(), search(change)))
    search_btn.place(x=191, y=450, width=175, height=31)

    home_btn = Button(BM, text="Home", activeforeground="gray", font=("Impact", 15), bd=0
                      , bg="#ce4912", activebackground="#ce4912", fg="White"
                      , command=lambda: (BM.destroy(), Library.Library_management(frame)))
    home_btn.place(x=191, y=496, width=175, height=31)


def New(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.add/new book.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def collect(text):
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
        except:
            messagebox.showerror("Error", "Database Error")
            return

        try:
            query = "select author_id, name from authors where name like '%" + text + "%'"
            mycursor.execute(query)
            result = mycursor.fetchall()
            con.close()
        except:
            return

        list.place(x=169, y=271)
        list.delete(0, END)
        for row in result:
            iid = str(row[0])
            list.insert(END, iid + " , " + row[1])

    def select():
        selected_suggestion = list.get(list.curselection()[0])
        selected_suggestion = selected_suggestion.split()
        iid = selected_suggestion[0]

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
        except:
            messagebox.showerror("Error", "Database Error")
            return

        query = "select name from authors where author_id=%s"
        para = [iid]
        mycursor.execute(query, para)
        result = mycursor.fetchone()
        con.close()

        author_name.delete(0, END)
        author_name.insert(0, result[0])

        list.place_forget()

    try:
        fonte = ("Gabriola", 15)
        fg = "#302f3f"

        def isbn_in():
            isbn.select_range(0, END)

        def isbn_out():
            if isbn.get() == "":
                isbn.insert(0, "isbn number")

        isbn = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        isbn.place(x=167, y=143, width=140, height=29)
        isbn.insert(0, "isbn number")
        isbn.bind("<FocusIn>", lambda e: isbn_in())
        isbn.bind("<FocusOut>", lambda e: isbn_out())

        date = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        date.place(x=347, y=143, width=140, height=29)
        date.insert(0, today)
        date.config(state="readonly")

        def book_in():
            book_name.select_range(0, END)

        def book_out():
            if book_name.get() == "":
                book_name.insert(0, "book name")

        book_name = Entry(NBM, font=fonte, fg="#ebebeb", bd=0, bg="#302f3f", insertbackground="#ebebeb")
        book_name.place(x=167, y=191, width=320, height=29)
        book_name.insert(0, "book name")
        book_name.bind("<FocusIn>", lambda e: book_in())
        book_name.bind("<FocusOut>", lambda e: book_out())

        def author_in():
            author_name.select_range(0, END)

        def author_out():
            if author_name.get() == "":
                author_name.insert(0, "author name")

        author_name = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        author_name.place(x=167, y=238, width=299, height=29)
        author_name.insert(0, "author name")
        author_name.bind("<FocusIn>", lambda e: author_in())
        author_name.bind("<FocusOut>", lambda e: author_out())
        author_name.bind("<KeyRelease>", lambda e: collect(author_name.get()))

        def show():
            if list.winfo_ismapped():
                list.place_forget()
            else:
                list.place(x=169, y=271)

        drop_btn = Button(NBM, text="⇅", bg="#302f3f", font=("Candara", 15, "bold"), bd=0, command=show, fg="#ebebeb",
                          activebackground="#302f3f", activeforeground="#ebebeb")
        drop_btn.place(x=472, y=242, width=21, height=21)

        def category_in():
            category.select_range(0, END)

        def category_out():
            if category.get() == "":
                category.insert(0, "category")

        category = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        category.place(x=167, y=285, width=320, height=29)
        category.insert(0, "category")
        category.bind("<FocusIn>", lambda e: category_in())
        category.bind("<FocusOut>", lambda e: category_out())

        def Quantity_in():
            quantity.select_range(0, END)

        def Quantity_out():
            if quantity.get() == "":
                quantity.insert(0, "Quantity")

        quantity = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        quantity.place(x=167, y=332, width=140, height=29)
        quantity.insert(0, "Quantity")
        quantity.bind("<FocusIn>", lambda e: Quantity_in())
        quantity.bind("<FocusOut>", lambda e: Quantity_out())

        def price_in():
            price.select_range(0, END)

        def price_out():
            if price.get() == "":
                price.insert(0, "price")

        price = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        price.place(x=347, y=332, width=140, height=29)
        price.insert(0, "price")
        price.bind("<FocusIn>", lambda e: price_in())
        price.bind("<FocusOut>", lambda e: price_out())

        list = Listbox(NBM, height=10, width=52, bd=1, bg="#ebebeb")
        list.bind("<Double-Button-1>", lambda event: select())
    except:
        pass

    def add():
        if isbn.get() == "" or isbn.get() == "isbn number" or \
                book_name.get() == "" or book_name.get() == "book name" or \
                author_name.get() == "" or author_name.get() == "author name" or \
                category.get() == "" or category.get() == "category" or \
                quantity.get() == "" or quantity.get() == "Quantity" or \
                price.get() == "" or price.get() == "price":
            messagebox.showerror("error", "add fields required !")
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
                mycursor = con.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = """
                        CREATE TABLE books (
                        isbn VARCHAR(50),
                        name VARCHAR(100),
                        author VARCHAR(100),
                        category VARCHAR(50),
                        quantity VARCHAR(5),
                        price VARCHAR(10))
                        """
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select isbn from books where isbn=%s"
            parameter = [isbn.get()]
            mycursor.execute(query, parameter)
            result = mycursor.fetchone()

            if result is not None:
                messagebox.showerror("error", "Isbn Is Already Available, if yuo want to edit Go to edit !")
                con.close()
            else:
                query = "INSERT INTO books (isbn, name, author, category, quantity, price)" \
                        "VALUES (%s,%s,%s,%s,%s,%s)"
                parameter = [isbn.get(), book_name.get(), author_name.get()
                    , category.get(), quantity.get(), price.get()]
                mycursor.execute(query, parameter)
                con.commit()
                con.close()
                add_author()
                messagebox.showinfo("success", "book added successfully")

    def add_author():
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
            query = """
                    CREATE TABLE authors (
                    author_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    nationality VARCHAR(50),
                    publisher VARCHAR(50),
                    category VARCHAR(100),
                    gender VARCHAR(10),
                    dob DATE
                    )
                    """
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "SELECT author_id FROM authors WHERE name = %s"
        parameter = (author_name.get(),)
        mycursor.execute(query, parameter)
        result = mycursor.fetchone()

        if result is None:
            query = "INSERT INTO authors (name) VALUES (%s)"
            mycursor.execute(query, parameter)
            con.commit()
            con.close()
            messagebox.showinfo("ok", "Okay")

        con.close()

    new_btn = Button(NBM, text="ADD", activeforeground="gray", font=("Impact", 15), bd=0
                     , bg="#302f3f", activebackground="#302f3f", fg="White", command=add)
    new_btn.place(x=167, y=405, width=140, height=29)

    clear_btn = Button(NBM, text="Clear", activeforeground="gray", font=("Impact", 15), bd=0
                       , bg="#302f3f", activebackground="#302f3f", fg="White")
    clear_btn.place(x=347, y=405, width=140, height=29)


def Edit(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.edit/edit book.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def collect(text):
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
        except:
            messagebox.showerror("Error", "Database Error")
            return

        try:
            query = """
                CREATE TABLE books (
                isbn VARCHAR(50),
                name VARCHAR(100),
                author VARCHAR(100),
                category VARCHAR(50),
                quantity VARCHAR(5),
                price VARCHAR(10))
                """
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select isbn,name from books where isbn like '%" + text + "%' or name like '%" + text + "%'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        Drop.place(x=169, y=223)
        Drop.delete(0, END)
        for row in result:
            Drop.insert(END, row[0] + " , " + row[1])

    def select():
        selected_suggestion = Drop.get(Drop.curselection()[0])
        selected_suggestion = selected_suggestion.split()
        Key = selected_suggestion[0]

        isbn.delete(0, END)
        isbn.insert(0, Key)

        Drop.place_forget()
        find()

    def find():
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
        except:
            messagebox.showerror("Error", "Database Error")
            return

        query = "select * from books where isbn=%s"
        parameters = [isbn.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()
        con.close()

        if result is not None:
            book_name.delete(0, END)
            author_name.delete(0, END)
            category.delete(0, END)
            quantity.delete(0, END)
            price.delete(0, END)

            book_name.insert(0, result[1])
            author_name.insert(0, result[2])
            category.insert(0, result[3])
            quantity.insert(0, result[4])
            price.insert(0, result[5])
        else:
            pass

    try:
        fonte = ("Gabriola", 15)
        fg = "#302f3f"

        def isbn_in():
            isbn.select_range(0, END)

        def isbn_out():
            # Drop.place_forget()
            if isbn.get() == "":
                isbn.insert(0, "isbn number")

        isbn = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        isbn.place(x=167, y=143, width=140, height=29)
        isbn.insert(0, "isbn number")
        isbn.bind("<FocusIn>", lambda e: isbn_in())
        isbn.bind("<FocusOut>", lambda e: isbn_out())
        isbn.bind("<KeyRelease>", lambda event: collect(isbn.get()))

        date = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        date.place(x=347, y=143, width=140, height=29)
        date.insert(0, today)
        date.config(state="readonly")

        def book_in():
            book_name.select_range(0, END)

        def book_out():
            if book_name.get() == "":
                book_name.insert(0, "book name")

        book_name = Entry(NBM, font=fonte, fg="#ebebeb", bd=0, bg="#302f3f", insertbackground="#ebebeb")
        book_name.place(x=167, y=191, width=299, height=29)
        book_name.insert(0, "book name")
        book_name.bind("<FocusIn>", lambda e: book_in())
        book_name.bind("<FocusOut>", lambda e: book_out())

        def show():
            if Drop.winfo_ismapped():
                Drop.place_forget()
            else:
                Drop.place(x=169, y=223)

        drop_btn = Button(NBM, text="⇅", bg="#ebebeb", font=("Candara", 15, "bold"), bd=0, command=show, fg=fg,
                          activebackground="#ebebeb", activeforeground=fg)
        drop_btn.place(x=472, y=195, width=21, height=21)

        def author_in():
            author_name.select_range(0, END)

        def author_out():
            if author_name.get() == "":
                author_name.insert(0, "author name")

        author_name = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        author_name.place(x=167, y=238, width=320, height=29)
        author_name.insert(0, "author name")
        author_name.bind("<FocusIn>", lambda e: author_in())
        author_name.bind("<FocusOut>", lambda e: author_out())

        def category_in():
            category.select_range(0, END)

        def category_out():
            if category.get() == "":
                category.insert(0, "category")

        category = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        category.place(x=167, y=285, width=320, height=29)
        category.insert(0, "category")
        category.bind("<FocusIn>", lambda e: category_in())
        category.bind("<FocusOut>", lambda e: category_out())

        def Quantity_in():
            quantity.select_range(0, END)

        def Quantity_out():
            if quantity.get() == "":
                quantity.insert(0, "Quantity")

        quantity = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        quantity.place(x=167, y=332, width=140, height=29)
        quantity.insert(0, "Quantity")
        quantity.bind("<FocusIn>", lambda e: Quantity_in())
        quantity.bind("<FocusOut>", lambda e: Quantity_out())

        def price_in():
            price.select_range(0, END)

        def price_out():
            if price.get() == "":
                price.insert(0, "price")

        price = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        price.place(x=347, y=332, width=140, height=29)
        price.insert(0, "price")
        price.bind("<FocusIn>", lambda e: price_in())
        price.bind("<FocusOut>", lambda e: price_out())

        Drop = Listbox(NBM, height=10, width=52, bd=1, bg="#ebebeb")
        Drop.bind("<Double-Button-1>", lambda event: select())
    except:
        pass

    new_btn = Button(NBM, text="Search", activeforeground="gray", font=("Impact", 15), bd=0
                     , bg="#302f3f", activebackground="#302f3f", fg="White")
    new_btn.place(x=167, y=406, width=140, height=29)

    clear_btn = Button(NBM, text="Edit & Save", activeforeground="gray", font=("Impact", 15), bd=0
                       , bg="#302f3f", activebackground="#302f3f", fg="White")
    clear_btn.place(x=347, y=406, width=140, height=29)


def Inventory(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.inventory/Lib inventory.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

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
            mycursor = con.cursor(buffered=True)
        except:
            messagebox.showerror("Error", "Database Error")
            return

        try:
            query = """
                CREATE TABLE books (
                isbn VARCHAR(50),
                name VARCHAR(100),
                author VARCHAR(100),
                category VARCHAR(50),
                quantity VARCHAR(5),
                price VARCHAR(10))
                """
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select isbn,name from books"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        if result is not None:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[0], row[1]))
        else:
            pass

    try:
        fonte = ("Gabriola", 15)
        fg = "#302f3f"

        def author_in():
            author_name.select_range(0, END)

        def author_out():
            if author_name.get() == "":
                author_name.insert(0, "author name")

        author_name = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        author_name.place(x=167, y=110, width=140, height=29)
        author_name.insert(0, "author name")
        author_name.bind("<FocusIn>", lambda e: author_in())
        author_name.bind("<FocusOut>", lambda e: author_out())

        def category_in():
            category.select_range(0, END)

        def category_out():
            if category.get() == "":
                category.insert(0, "category")

        category = Entry(NBM, font=fonte, fg=fg, bd=0, bg="#ebebeb")
        category.place(x=347, y=110, width=140, height=29)
        category.insert(0, "category")
        category.bind("<FocusIn>", lambda e: category_in())
        category.bind("<FocusOut>", lambda e: category_out())
    except:
        pass

    try:
        view = ttk.Treeview(NBM)
        view.place(x=158, y=155, height=237, width=340)

        view["columns"] = ("0", "1")
        view["show"] = "headings"

        view.column("0", minwidth=10, width=20)
        view.column("1", minwidth=150, width=20)

        view.heading("0", text="ISBN")
        view.heading("1", text="Book Name")
    except:
        pass

    collect()


def author(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.author/Author.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    new_btn = Button(NBM, text="New", activeforeground="gray", font=("Impact", 15), bd=0
                     , bg="#302f3f", activebackground="#302f3f", fg="White"
                     , command=lambda: (NBM.destroy(), new_author(frame)))
    new_btn.place(x=169, y=407, width=145, height=25)

    edit_btn = Button(NBM, text="Edit", activeforeground="gray", font=("Impact", 15), bd=0
                      , bg="#302f3f", activebackground="#302f3f", fg="White"
                      , command=lambda: (NBM.destroy(), edit_author(frame)))
    edit_btn.place(x=347, y=407, width=145, height=25)


def new_author(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.new_author/new Author.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)


def edit_author(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.edit_author/edit Author.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)


def search(frame):
    NBM = Frame(frame, height=552, width=684)
    NBM.pack()

    back = PhotoImage(file=current_path + "/.ux./library/.book/.search/search book.png")
    Background = Label(NBM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)
