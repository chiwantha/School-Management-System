from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import winreg
import random
import string
import mysql.connector
from tkinter.filedialog import askopenfilename
import os
import tkinter as tk
import pandas as pd
import customtkinter
from tkcalendar import DateEntry

nic = ""
control = "disabled"
admin_nic = ""
admin_name = ""
admin_rank = ""

current = os.path.dirname(os.path.realpath(__file__))


def Enrollment(frame):
    enrollment_frame = Frame(frame, height=651, width=1185)
    enrollment_frame.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.enrollment/Teacher Add.png")
    Background = Label(enrollment_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Calibri", 12)
    fg = "#444444"

    try:
        def auto_id():
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
                mycursor = con.cursor(buffered=True)
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            try:
                query = "select max(id) from teacher"
                mycursor.execute(query)
                result = mycursor.fetchone()

                t_id.insert(0, int(result[0]) + 1)
            except:
                pass

        def id_tap():
            # t_id.delete(0, END)
            t_id.select_range(0, END)

        def id_dtap():
            if t_id.get() == "":
                t_id.insert(0, "Index")

        t_id = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_id.place(x=297, y=155, width=243, height=23)
        t_id.bind("<FocusIn>", lambda event: id_tap())
        t_id.bind("<FocusOut>", lambda event: id_dtap())
        auto_id()

        def nic_tap():
            t_nic.select_range(0, END)

        def nic_dtap():
            if t_nic.get() == "":
                t_nic.insert(0, "enter NIC")

        t_nic = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_nic.place(x=577, y=155, width=243, height=23)
        t_nic.insert(0, "enter NIC")
        t_nic.bind("<FocusIn>", lambda event: nic_tap())
        t_nic.bind("<FocusOut>", lambda event: nic_dtap())

        def fam_tap():
            t_family_name.select_range(0, END)

        def fam_dtap():
            if t_family_name.get() == "":
                t_family_name.insert(0, "family name")

        t_family_name = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_family_name.place(x=297, y=220, width=243, height=23)
        t_family_name.insert(0, "family name")
        t_family_name.bind("<FocusIn>", lambda event: fam_tap())
        t_family_name.bind("<FocusOut>", lambda event: fam_dtap())

        def fn_tap():
            t_first_name.select_range(0, END)

        def fn_dtap():
            if t_first_name.get() == "":
                t_first_name.insert(0, "first name")

        t_first_name = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_first_name.place(x=577, y=220, width=243, height=23)
        t_first_name.insert(0, "first name")
        t_first_name.bind("<FocusIn>", lambda event: fn_tap())
        t_first_name.bind("<FocusOut>", lambda event: fn_dtap())

        def ln_tap():
            t_last_name.select_range(0, END)

        def ln_dtap():
            if t_last_name.get() == "":
                t_last_name.insert(0, "last name")

        t_last_name = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_last_name.place(x=857, y=220, width=243, height=23)
        t_last_name.insert(0, "last name")
        t_last_name.bind("<FocusIn>", lambda event: ln_tap())
        t_last_name.bind("<FocusOut>", lambda event: ln_dtap())

        def fln_tap():
            t_ful_name.select_range(0, END)

        def fln_dtap():
            if t_ful_name.get() == "":
                t_ful_name.insert(0, "ful name with initials")

        t_ful_name = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_ful_name.place(x=298, y=284, width=521, height=23)
        t_ful_name.insert(0, "ful name with initials")
        t_ful_name.bind("<FocusIn>", lambda event: fln_tap())
        t_ful_name.bind("<FocusOut>", lambda event: fln_dtap())

        options = ["Male", "Female", "Other"]
        t_gender = ttk.Combobox(enrollment_frame, font=fonts, foreground=fg, values=options)
        t_gender.place(x=857, y=284, width=243, height=23)
        t_gender.set(options[0])

        def mail_tap():
            t_mail.select_range(0, END)

        def mail_dtap():
            if t_mail.get() == "":
                t_mail.insert(0, "e-email")

        t_mail = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_mail.place(x=297, y=347, width=243, height=23)
        t_mail.insert(0, "e-mail")
        t_mail.bind("<FocusIn>", lambda event: mail_tap())
        t_mail.bind("<FocusOut>", lambda event: mail_dtap())

        def pone_tap():
            t_pone.select_range(0, END)

        def pone_dtap():
            if t_pone.get() == "":
                t_pone.insert(0, "078 6.. ..")

        def validate_entry(text):
            if len(text) > 10:
                return False
            return True

        validate_command = enrollment_frame.register(validate_entry)

        t_pone = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg, validate="key",
                       validatecommand=(validate_command, "%P"))
        t_pone.place(x=577, y=347, width=243, height=23)
        t_pone.insert(0, "078 6.. ..")
        t_pone.bind("<FocusIn>", lambda event: pone_tap())
        t_pone.bind("<FocusOut>", lambda event: pone_dtap())

        def sub1_tap():
            t_subject_1.select_range(0, END)

        def sub1_dtap():
            if t_subject_1.get() == "":
                t_subject_1.insert(0, "main subject")

        t_subject_1 = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_subject_1.place(x=297, y=435, width=243, height=23)
        t_subject_1.insert(0, "main subject")
        t_subject_1.bind("<FocusIn>", lambda event: sub1_tap())
        t_subject_1.bind("<FocusOut>", lambda event: sub1_dtap())

        def sub2_tap():
            t_subject_2.select_range(0, END)

        def sub2_dtap():
            if t_subject_2.get() == "":
                t_subject_2.insert(0, "subject 2 ( optional )")

        t_subject_2 = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_subject_2.place(x=577, y=435, width=243, height=23)
        t_subject_2.insert(0, "subject 2 ( optional )")
        t_subject_2.bind("<FocusIn>", lambda event: sub2_tap())
        t_subject_2.bind("<FocusOut>", lambda event: sub2_dtap())

        t_dob = DateEntry(enrollment_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        t_dob.place(x=857, y=435, width=243, height=23)
        '''t_dob = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_dob.place(x=857, y=435, width=243, height=23)
        t_dob.insert(0, Date)'''

        def ad_tap():
            t_address.select_range(0, END)

        def ad_dtap():
            if t_address.get() == "":
                t_address.insert(0, "No. 361/A example,")

        t_address = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_address.place(x=297, y=497, width=243, height=23)
        t_address.insert(0, "No. 361/A example,")
        t_address.bind("<FocusIn>", lambda event: ad_tap())
        t_address.bind("<FocusOut>", lambda event: ad_dtap())

        def adl_tap():
            t_address_line.select_range(0, END)

        def adl_dtap():
            if t_address_line.get() == "":
                t_address_line.insert(0, "address line 2 ( optional )")

        t_address_line = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_address_line.place(x=577, y=497, width=243, height=23)
        t_address_line.insert(0, "address line 2 ( optional )")
        t_address_line.bind("<FocusIn>", lambda event: adl_tap())
        t_address_line.bind("<FocusOut>", lambda event: adl_dtap())

        def town_tap():
            t_town.select_range(0, END)

        def town_dtap():
            if t_town.get() == "":
                t_town.insert(0, "home town")

        t_town = Entry(enrollment_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_town.place(x=857, y=497, width=243, height=23)
        t_town.insert(0, "home town")
        t_town.bind("<FocusIn>", lambda event: town_tap())
        t_town.bind("<FocusOut>", lambda event: town_dtap())
    except:
        pass

    def add_data():
        if t_id.get() == "Index" or \
                t_nic.get() == "" or \
                t_family_name.get() == "" or \
                t_first_name.get() == "" or \
                t_last_name.get() == "" or \
                t_ful_name.get() == "" or \
                t_mail.get() == "" or \
                t_pone.get() == "" or \
                t_subject_1.get() == "" or \
                t_subject_2.get() == "" or \
                t_dob.get() == "" or \
                t_address.get() == "" or \
                t_address_line.get() == "" or \
                t_town.get() == "":
            messagebox.showerror("ERROR", "All Fields are Required !")
        else:
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
                mycursor = con.cursor(buffered=True)
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

            query = "select id from teacher where id = %s"
            parameters = [t_id.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                messagebox.showerror("ERROR", "Index is already exist")
            else:
                try:
                    query = "INSERT INTO teacher VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    parameters = [t_id.get(),
                                  t_nic.get(),
                                  t_family_name.get(),
                                  t_first_name.get(),
                                  t_last_name.get(),
                                  t_ful_name.get(),
                                  t_gender.get(),
                                  t_mail.get(),
                                  t_pone.get(),
                                  t_subject_1.get(),
                                  t_subject_2.get(),
                                  t_dob.get(),
                                  t_address.get(),
                                  t_address_line.get(),
                                  t_town.get()]
                    mycursor.execute(query, parameters)
                    messagebox.showinfo("SUCCESS", "Data Added Successfully !")
                    con.commit()
                except:
                    messagebox.showerror("ERROR", "Data Adding Failed !")
            con.close()

    fontl = ("Candara", 14, "bold")

    btn_teacher_add = Button(enrollment_frame, text="SUBMIT", bg="#ce4912", fg="white", font=fontl, command=add_data)
    btn_teacher_add.place(x=254, y=593, width=172, height=34)

    btn_teacher_update = Button(enrollment_frame, text="UPDATE", bg="#3b3086", fg="white", font=fontl)
    btn_teacher_update.place(x=446, y=593, width=172, height=34)
    btn_teacher_update.config(command=lambda: messagebox.showerror("error", "Cannot Update,Go to Edit !"))

    # noinspection PyBroadException
    def delete():
        pass

    btn_teacher_clear = Button(enrollment_frame, text="CLEAR", bg="#3b3086", fg="white", font=fontl, command=delete)
    btn_teacher_clear.place(x=638, y=593, width=172, height=34)

    def load():
        enrollment_frame.destroy()
        Find(frame)

    fontl = ("Candara", 14, "bold")

    search_teacher = Button(enrollment_frame, text="SEARCH", bg="#3b3086", fg="white", font=fontl, command=load)
    search_teacher.place(x=22, y=295, width=172, height=34)

    Bulk = Button(enrollment_frame, text="Import as Bulk", bg="#3b3086", fg="white", font=fontl, command=bulk)
    Bulk.place(x=22, y=350, width=172, height=34)


def Find(frame):
    find_frame = Frame(frame, height=651, width=1185)
    find_frame.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.search/Teacher Details.png")
    Background = Label(find_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Calibri", 12)

    try:
        background = "#e9edfa"

        t_id = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_id.place(x=297, y=155, width=243, height=23)

        t_nic = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_nic.place(x=577, y=155, width=243, height=23)

        t_family_name = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_family_name.place(x=297, y=220, width=243, height=23)

        t_first_name = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_first_name.place(x=577, y=220, width=243, height=23)

        t_last_name = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_last_name.place(x=857, y=220, width=243, height=23)

        t_full_name = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_full_name.place(x=297, y=284, width=523, height=23)

        t_gender = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_gender.place(x=857, y=284, width=243, height=23)

        t_mail = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_mail.place(x=297, y=347, width=243, height=23)

        t_pone = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_pone.place(x=577, y=347, width=243, height=23)

        background = "white"

        t_subject_1 = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_subject_1.place(x=297, y=435, width=243, height=23)

        t_subject_2 = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_subject_2.place(x=577, y=435, width=243, height=23)

        t_dob = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_dob.place(x=857, y=435, width=243, height=23)

        t_address = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_address.place(x=297, y=497, width=243, height=23)

        t_address_line = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_address_line.place(x=577, y=497, width=243, height=23)

        t_town = Label(find_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        t_town.place(x=857, y=497, width=243, height=23)
    except:
        pass

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
            query = "CREATE TABLE teacher(" \
                    "id int PRIMARY KEY,nic VARCHAR(20), family_name VARCHAR(50), first_name VARCHAR(20)," \
                    "last_name VARCHAR(20),full_name varchar(100),gender VARCHAR(10),e_mail VARCHAR(50)," \
                    "pone_number VARCHAR(20)," \
                    "sub1 VARCHAR(20),sub2 VARCHAR(50), dob Date,address VARCHAR(50),address_line VARCHAR(50)," \
                    "city VARCHAR(20))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select nic, full_name from teacher where full_name like '%" + text + "%' " \
                                                                                      "or nic like '%" + text + "%'"
        mycursor.execute(query)
        result = mycursor.fetchall()

        list.place(x=841, y=182)

        list.delete(0, END)
        for row in result:
            idd = str(row[0])
            list.insert(END, idd + " , " + row[1])

    def select():
        selected_suggestion = list.get(list.curselection()[0])
        selected_suggestion = selected_suggestion.split()
        global key_nic
        key_nic = selected_suggestion[0]

        search_box.delete(0, END)
        search_box.insert(0, " Search Bar")

        list.place_forget()
        find()

    def find():
        # noinspection PyBroadException
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
            except:
                messagebox.showerror("Error", "Database Error")
                return

            query = "select * from teacher where nic=%s"
            parameters = [key_nic]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()
            # print(result)

            t_id.config(text=result[0])
            t_nic.config(text=result[1])
            t_family_name.config(text=result[2])
            t_first_name.config(text=result[3])
            t_last_name.config(text=result[4])
            t_full_name.config(text=result[5])
            t_gender.config(text=result[6])
            t_mail.config(text=result[7])
            t_pone.config(text=result[8])
            t_subject_1.config(text=result[9])
            t_subject_2.config(text=result[10])
            t_dob.config(text=result[11])
            t_address.config(text=result[12])
            t_address_line.config(text=result[13])
            t_town.config(text=result[14])
            con.close()
        except:
            t_id.config(text="none")
            t_nic.config(text="none")
            t_family_name.config(text="none")
            t_first_name.config(text="none")
            t_last_name.config(text="none")
            t_full_name.config(text="none")
            t_gender.config(text="none")
            t_mail.config(text="none")
            t_pone.config(text="none")
            t_subject_1.config(text="none")
            t_subject_2.config(text="none")
            t_dob.config(text="none")
            t_address.config(text="none")
            t_address_line.config(text="none")
            t_town.config(text="none")

    def search_in():
        search_box.select_range(0, END)

    def search_out():
        if search_box.get() == "":
            search_box.insert(0, " Search Bar")

    search_box = Entry(find_frame, font=fonts, foreground="#1b2d52", bd=0)
    search_box.place(x=843, y=152, width=227, height=28)
    search_box.insert(0, " Search Bar")
    search_box.bind("<FocusIn>", lambda event: search_in())
    search_box.bind("<FocusOut>", lambda event: search_out())
    search_box.bind("<KeyRelease>", lambda event: collect(search_box.get()))

    def show():
        if list.winfo_ismapped():
            list.place_forget()
        else:
            list.place(x=841, y=182)

    drop_btn = Button(find_frame, text="⇅", bg="white", font=("Candara", 20, "bold"), bd=0, command=show)
    drop_btn.place(x=1070, y=152, width=28, height=28)

    list = Listbox(find_frame, height=10, width=43, bd=0)
    list.bind("<Double-Button-1>", lambda event: select())

    def load():
        find_frame.destroy()
        Enrollment(frame)

    fontl = ("Candara", 14, "bold")

    search_student = Button(find_frame, text="ENROLLMENT", bg="#3b3086", fg="white", font=fontl, command=load)
    search_student.place(x=22, y=295, width=172, height=34)


def Edit(frame):
    edit_frame = Frame(frame, height=651, width=1185)
    edit_frame.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.edit/Teacher Edit.png")
    Background = Label(edit_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fg = "#444444"
    fonts = ("Calibri", 12)

    try:
        def search_in():
            search_box.select_range(0, END)

        def search_out():
            if search_box.get() == "":
                search_box.insert(0, " Search Bar")

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
                query = "CREATE TABLE teacher(" \
                        "id int PRIMARY KEY,nic VARCHAR(20), family_name VARCHAR(50), first_name VARCHAR(20)," \
                        "last_name VARCHAR(20),full_name varchar(100),gender VARCHAR(10),e_mail VARCHAR(50)," \
                        "pone_number VARCHAR(20)," \
                        "sub1 VARCHAR(20),sub2 VARCHAR(50), dob Date,address VARCHAR(50),address_line VARCHAR(50)," \
                        "city VARCHAR(20))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select nic, full_name from teacher where full_name like '%" + text + "%' " \
                                                                                          "or nic like '%" + text + "%' or id like '%" + text + "%'"
            mycursor.execute(query)
            result = mycursor.fetchall()
            con.close()

            list.place(x=284, y=183)

            list.delete(0, END)
            for row in result:
                idd = str(row[0])
                list.insert(END, idd + " , " + row[1])

        def select():
            selected_suggestion = list.get(list.curselection()[0])
            selected_suggestion = selected_suggestion.split()
            global key_nic
            key_nic = selected_suggestion[0]

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

            query = "select id from teacher where nic=%s"
            parameter = [key_nic]
            mycursor.execute(query, parameter)
            Id_num = mycursor.fetchone()
            con.close()

            search_box.delete(0, END)
            search_box.insert(0, Id_num)

            list.place_forget()
            find()

        def find():
            # noinspection PyBroadException
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
                except:
                    messagebox.showerror("Error", "Database Error")
                    return

                query = "select * from teacher where nic=%s"
                parameters = [key_nic]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()
                # print(result)

                t_nic.delete(0, END)
                t_family_name.delete(0, END)
                t_first_name.delete(0, END)
                t_last_name.delete(0, END)
                t_ful_name.delete(0, END)
                t_gender.delete(0, END)
                t_mail.delete(0, END)
                t_pone.delete(0, END)
                t_subject_1.delete(0, END)
                t_subject_2.delete(0, END)
                t_dob.delete(0, END)
                t_address.delete(0, END)
                t_address_line.delete(0, END)
                t_town.delete(0, END)

                t_nic.insert(0, result[1])
                t_family_name.insert(0, result[2])
                t_first_name.insert(0, result[3])
                t_last_name.insert(0, result[4])
                t_ful_name.insert(0, result[5])
                t_gender.insert(0, result[6])
                t_mail.insert(0, result[7])
                t_pone.insert(0, result[8])
                t_subject_1.insert(0, result[9])
                t_subject_2.insert(0, result[10])
                t_dob.insert(0, result[11])
                t_address.insert(0, result[12])
                t_address_line.insert(0, result[13])
                t_town.insert(0, result[14])
                con.close()
            except:
                t_nic.insert(0, "None")
                t_family_name.insert(0, "None")
                t_first_name.insert(0, "None")
                t_last_name.insert(0, "None")
                t_ful_name.insert(0, "None")
                t_gender.insert(0, "None")
                t_mail.insert(0, "None")
                t_pone.insert(0, "None")
                t_subject_1.insert(0, "None")
                t_subject_2.insert(0, "None")
                t_dob.insert(0, "None")
                t_address.insert(0, "None")
                t_address_line.insert(0, "None")
                t_town.insert(0, "None")

        search_box = Entry(edit_frame, font=fonts, foreground="#1b2d52", bd=0)
        search_box.place(x=286, y=152, width=225, height=28)
        search_box.insert(0, " Search Bar")
        search_box.bind("<FocusIn>", lambda event: search_in())
        search_box.bind("<FocusOut>", lambda event: search_out())
        search_box.bind("<KeyRelease>", lambda event: collect(search_box.get()))

        def show():
            if list.winfo_ismapped():
                list.place_forget()
            else:
                list.place(x=284, y=183)

        drop_btn = Button(edit_frame, text="⇅", bg="white", font=("Candara", 20, "bold"), bd=0, command=show)
        drop_btn.place(x=513, y=152, width=28, height=28)

        def nic_tap():
            t_nic.select_range(0, END)

        def nic_dtap():
            if t_nic.get() == "":
                t_nic.insert(0, "enter NIC")

        t_nic = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_nic.place(x=577, y=155, width=243, height=23)
        t_nic.insert(0, "enter NIC")
        t_nic.bind("<FocusIn>", lambda event: nic_tap())
        t_nic.bind("<FocusOut>", lambda event: nic_dtap())

        def fam_tap():
            t_family_name.select_range(0, END)

        def fam_dtap():
            if t_family_name.get() == "":
                t_family_name.insert(0, "family name")

        t_family_name = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_family_name.place(x=297, y=220, width=243, height=23)
        t_family_name.insert(0, "family name")
        t_family_name.bind("<FocusIn>", lambda event: fam_tap())
        t_family_name.bind("<FocusOut>", lambda event: fam_dtap())

        def fn_tap():
            t_first_name.select_range(0, END)

        def fn_dtap():
            if t_first_name.get() == "":
                t_first_name.insert(0, "first name")

        t_first_name = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_first_name.place(x=577, y=220, width=243, height=23)
        t_first_name.insert(0, "first name")
        t_first_name.bind("<FocusIn>", lambda event: fn_tap())
        t_first_name.bind("<FocusOut>", lambda event: fn_dtap())

        def ln_tap():
            t_last_name.select_range(0, END)

        def ln_dtap():
            if t_last_name.get() == "":
                t_last_name.insert(0, "last name")

        t_last_name = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_last_name.place(x=857, y=220, width=243, height=23)
        t_last_name.insert(0, "last name")
        t_last_name.bind("<FocusIn>", lambda event: ln_tap())
        t_last_name.bind("<FocusOut>", lambda event: ln_dtap())

        def fln_tap():
            t_ful_name.select_range(0, END)

        def fln_dtap():
            if t_ful_name.get() == "":
                t_ful_name.insert(0, "ful name with initials")

        t_ful_name = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_ful_name.place(x=298, y=284, width=521, height=23)
        t_ful_name.insert(0, "ful name with initials")
        t_ful_name.bind("<FocusIn>", lambda event: fln_tap())
        t_ful_name.bind("<FocusOut>", lambda event: fln_dtap())

        options = ["Male", "Female", "Other"]
        t_gender = ttk.Combobox(edit_frame, font=fonts, foreground=fg, values=options)
        t_gender.place(x=857, y=284, width=243, height=23)
        t_gender.set(options[0])

        def mail_tap():
            t_mail.select_range(0, END)

        def mail_dtap():
            if t_mail.get() == "":
                t_mail.insert(0, "e-email")

        t_mail = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        t_mail.place(x=297, y=347, width=243, height=23)
        t_mail.insert(0, "e-mail")
        t_mail.bind("<FocusIn>", lambda event: mail_tap())
        t_mail.bind("<FocusOut>", lambda event: mail_dtap())

        def pone_tap():
            t_pone.select_range(0, END)

        def pone_dtap():
            if t_pone.get() == "":
                t_pone.insert(0, "078 6.. ..")

        def validate_entry(text):
            if len(text) > 10:
                return False
            return True

        validate_command = edit_frame.register(validate_entry)

        t_pone = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg, validate="key",
                       validatecommand=(validate_command, "%P"))
        t_pone.place(x=577, y=347, width=243, height=23)
        t_pone.insert(0, "078 6.. ..")
        t_pone.bind("<FocusIn>", lambda event: pone_tap())
        t_pone.bind("<FocusOut>", lambda event: pone_dtap())

        def sub1_tap():
            t_subject_1.select_range(0, END)

        def sub1_dtap():
            if t_subject_1.get() == "":
                t_subject_1.insert(0, "main subject")

        t_subject_1 = Entry(edit_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_subject_1.place(x=297, y=435, width=243, height=23)
        t_subject_1.insert(0, "main subject")
        t_subject_1.bind("<FocusIn>", lambda event: sub1_tap())
        t_subject_1.bind("<FocusOut>", lambda event: sub1_dtap())

        def sub2_tap():
            t_subject_2.select_range(0, END)

        def sub2_dtap():
            if t_subject_2.get() == "":
                t_subject_2.insert(0, "subject 2 ( optional )")

        t_subject_2 = Entry(edit_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_subject_2.place(x=577, y=435, width=243, height=23)
        t_subject_2.insert(0, "subject 2 ( optional )")
        t_subject_2.bind("<FocusIn>", lambda event: sub2_tap())
        t_subject_2.bind("<FocusOut>", lambda event: sub2_dtap())

        t_dob = DateEntry(edit_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        t_dob.place(x=857, y=435, width=243, height=23)

        def ad_tap():
            t_address.select_range(0, END)

        def ad_dtap():
            if t_address.get() == "":
                t_address.insert(0, "No. 361/A example,")

        t_address = Entry(edit_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_address.place(x=297, y=497, width=243, height=23)
        t_address.insert(0, "No. 361/A example,")
        t_address.bind("<FocusIn>", lambda event: ad_tap())
        t_address.bind("<FocusOut>", lambda event: ad_dtap())

        def adl_tap():
            t_address_line.select_range(0, END)

        def adl_dtap():
            if t_address_line.get() == "":
                t_address_line.insert(0, "address line 2 ( optional )")

        t_address_line = Entry(edit_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_address_line.place(x=577, y=497, width=243, height=23)
        t_address_line.insert(0, "address line 2 ( optional )")
        t_address_line.bind("<FocusIn>", lambda event: adl_tap())
        t_address_line.bind("<FocusOut>", lambda event: adl_dtap())

        def town_tap():
            t_town.select_range(0, END)

        def town_dtap():
            if t_town.get() == "":
                t_town.insert(0, "home town")

        t_town = Entry(edit_frame, font=fonts, bg="white", bd=0, fg=fg)
        t_town.place(x=857, y=497, width=243, height=23)
        t_town.insert(0, "home town")
        t_town.bind("<FocusIn>", lambda event: town_tap())
        t_town.bind("<FocusOut>", lambda event: town_dtap())

        list = Listbox(edit_frame, height=10, width=43, bd=0)
        list.bind("<Double-Button-1>", lambda event: select())
    except:
        pass

    def Update():
        if search_box.get() == "":
            messagebox.showerror("Error", "Please Enter Your Index")
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
            except:
                messagebox.showerror("Error", "Database Failing")
                return

            query = "update teacher set family_name=%s,first_name=%s,last_name=%s,full_name=%s,gender=%s," \
                    "e_mail=%s,pone_number=%s,sub1=%s,sub2=%s,dob=%s,address=%s,address_line=%s,city=%s where " \
                    "(teacher.id=%s or teacher.nic=%s)"
            parameters = [t_family_name.get(), t_first_name.get(), t_last_name.get(), t_ful_name.get(),
                          t_gender.get(), t_mail.get(), t_pone.get(), t_subject_1.get(), t_subject_2.get(),
                          t_dob.get(), t_address.get(), t_address_line.get(), t_town.get(), search_box.get(),
                          t_nic.get()]
            mycursor.execute(query, parameters)
            con.commit()
            con.close()
            messagebox.showinfo("success", "Saved !")
            find()

    fontl = ("Candara", 14, "bold")

    update = Button(edit_frame, text="UPDATE", bg="#ce4912", fg="white", font=fontl, command=Update)
    update.place(x=254, y=593, width=172, height=34)

    def load():
        edit_frame.destroy()
        Find(frame)

    search_teacher = Button(edit_frame, text="SEARCH", bg="#3b3086", fg="white", font=fontl, command=load)
    search_teacher.place(x=22, y=295, width=172, height=34)


def update_admin_info():
    sai = Toplevel()
    sai.grab_set()

    screen_width = sai.winfo_screenwidth()
    screen_height = sai.winfo_screenheight()
    window_width = 500
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    sai.geometry(f"{window_width}x{window_height}+{x}+{y}")

    sai.iconbitmap("pad.ico")
    sai.title("Set Admin Info")
    sai.resizable(False, False)

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.uai/Admin Info.png")
    back_p = Label(sai, image=back)
    back_p.image = back
    back_p.pack()

    # noinspection PyBroadException
    def Set():
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
            messagebox.showerror("Error", "Database Failing")
            return

        query = "select * from admin where NIC=%s"
        parameters = [admin_nic]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()

        if result is not None:
            try:
                query = "update admin set Name=%s,AdminRank=%s where NIC=%s"
                parameters = [set_name_entry.get(), set_rank_entry.get(), admin_nic]
                mycursor.execute(query, parameters)
                con.commit()
                messagebox.showinfo("SUCCESS", "DATA SET SUCCESSFULLY")

                query = "select * from admin where NIC=%s"
                parameters = [admin_nic]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()
                con.close()

                import UI_WIN
                UI_WIN.admin_name = result[1]
                UI_WIN.admin_rank = result[3]
                print("Done !")
            except:
                messagebox.showerror("ERROR", "DATA SET FAILED")
        else:
            messagebox.showerror("ERROR", "404 , DATA NOT FOUND")

    def Update():
        sai.destroy()

    fonts = ("Candara", 12, "bold")
    admin_nic_lbl = Label(sai, text=admin_nic, font=fonts, fg="#1b2d52", bg="#9fb0e8")
    admin_nic_lbl.place(width=248, height=34, x=168, y=106)

    fonts = ("Candara", 12, "bold")

    def non_enter():
        set_name_entry.select_range(0, END)

    def non_leave():
        get = set_name_entry.get()
        if get == "":
            set_name_entry.insert(0, str(admin_name))

    set_name_entry = Entry(sai, fg="#1b2d52", font=fonts)
    set_name_entry.place(x=168, y=152, width=291, height=34)
    set_name_entry.insert(0, str(admin_name))
    set_name_entry.bind("<FocusIn>", lambda event: non_enter())
    set_name_entry.bind("<FocusOut>", lambda event: non_leave())

    def ron_enter():
        set_rank_entry.select_range(0, END)

    def ron_leave():
        get = set_rank_entry.get()
        if get == "":
            set_rank_entry.insert(0, str(admin_rank))

    set_rank_entry = Entry(sai, fg="#1b2d52", font=fonts)
    set_rank_entry.place(x=168, y=200, width=291, height=34)
    set_rank_entry.insert(0, str(admin_rank))
    set_rank_entry.bind("<FocusIn>", lambda event: ron_enter())
    set_rank_entry.bind("<FocusOut>", lambda event: ron_leave())

    fonts = ("Candara", 15, "bold")
    set_btn = Button(sai, bg="#3b3086", fg="white", text="SET", font=fonts, command=Set)
    set_btn.place(x=168, y=248, width=140, height=34)

    update_btn = Button(sai, bg="#3b3086", fg="white", text="CLOSE", font=fonts, command=Update)
    update_btn.place(x=321, y=248, width=140, height=34)


def reset():
    # print("rest Successful")
    reset_win = Toplevel()
    reset_win.grab_set()

    screen_width = reset_win.winfo_screenwidth()
    screen_height = reset_win.winfo_screenheight()
    window_width = 500
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    reset_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

    reset_win.iconbitmap("pad.ico")
    reset_win.title("Reset Your Password")
    reset_win.resizable(False, False)

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.reset/Reset Pasword.png")
    back_p = Label(reset_win, image=back)
    back_p.image = back
    back_p.pack()

    # noinspection PyBroadException
    def up():
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
            messagebox.showerror("Error", "Database Failing")
            return

        if reset_nic_entry.get() == "" \
                or reset_password_entry.get() == "" \
                or reset_re_password_entry.get() == "":
            messagebox.showerror("Error", "All Fields Required")
        elif reset_password_entry.get() != reset_re_password_entry.get():
            messagebox.showerror("Error", "Password Mis-Match")
        else:
            query = "select * from admin where nic=%s"
            parameters = [reset_nic_entry.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                query = "update admin set password=%s where nic=%s"
                parameters = [reset_password_entry.get(), reset_nic_entry.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("Done", "Password Reset Successful")
                reset_win.destroy()
            else:
                messagebox.showerror("Error", "Invalid Nic")

    def non_enter():
        reset_nic_entry.delete(0, END)

    def non_leave():
        get = reset_nic_entry.get()
        if get == "":
            reset_nic_entry.insert(0, " NIC")

    fonts = ("Candara", 15)
    reset_nic_entry = Entry(reset_win, fg="#1b2d52", font=fonts)
    reset_nic_entry.place(x=168, y=104, width=291, height=34)
    reset_nic_entry.insert(0, admin_nic)
    reset_nic_entry.bind("<FocusIn>", lambda event: non_enter())
    reset_nic_entry.bind("<FocusOut>", lambda event: non_leave())

    def pon_enter():
        reset_password_entry.delete(0, END)

    def pon_leave():
        get = reset_password_entry.get()
        if get == "":
            reset_password_entry.insert(0, " New-Password")

    reset_password_entry = Entry(reset_win, fg="#1b2d52", font=fonts)
    reset_password_entry.place(x=168, y=152, width=291, height=34)
    reset_password_entry.insert(0, " New-Password")
    reset_password_entry.bind("<FocusIn>", lambda event: pon_enter())
    reset_password_entry.bind("<FocusOut>", lambda event: pon_leave())

    def ron_enter():
        reset_re_password_entry.delete(0, END)

    def ron_leave():
        get = reset_re_password_entry.get()
        if get == "":
            reset_re_password_entry.insert(0, " Re-Password")

    reset_re_password_entry = Entry(reset_win, fg="#1b2d52", font=fonts)
    reset_re_password_entry.place(x=168, y=200, width=291, height=34)
    reset_re_password_entry.insert(0, " Re-Password")
    reset_re_password_entry.bind("<FocusIn>", lambda event: ron_enter())
    reset_re_password_entry.bind("<FocusOut>", lambda event: ron_leave())

    # Buttons
    fonts = ("Candara", 15, "bold")
    Login_btn = Button(reset_win, bg="#3b3086", fg="white", text="RESET", font=fonts, command=up)
    Login_btn.place(x=169, y=248, width=140, height=34)

    def back():
        reset_win.destroy()

    create_btn = Button(reset_win, bg="#3b3086", fg="white", text="CLOSE", font=fonts, command=back)
    create_btn.place(x=321, y=248, width=140, height=34)


def Grader(frame):
    grader = Frame(frame, height=651, width=1185)
    grader.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.grader/grader.png")
    Background = Label(grader, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    def generate_password():
        password = ""
        for _ in range(6):
            password += random.choice(string.digits)
        return password

    fg = "#444444"
    fonts = ("Calibri", 12)

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
        except:
            messagebox.showerror("Error", "Database Failing")
            return

        try:
            query = "CREATE TABLE grader(nic VARCHAR(50),name varchar(100),class_group varchar(50),class varchar(50), " \
                    "pass varchar(6))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from grader"
        mycursor.execute(query)
        result = mycursor.fetchall()

        counter = 0
        for row in result:
            counter += 1
            view.insert(parent="", index=0, iid=counter, text="", values=(row[0], row[1], row[2], row[3]))

    def add_grader():
        otp = generate_password()
        if mode.get() == "Search Mode":
            messagebox.showerror("Error", "You are in Search Mode !")
        elif mode.get() == "Pass Mode":
            messagebox.showerror("Error", "You are in Pass Mode !")
        elif g_nic.get() == "":
            messagebox.showerror("Error", "Please Type Your Nic")
        elif g_class_group.get() == "":
            messagebox.showerror("Error", "Please select your group")
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
            except:
                messagebox.showerror("Error", "Database Failing")
                return

            try:
                query = "CREATE TABLE grader(nic VARCHAR(100), name varchar(200), group varchar(50), class varchar(" \
                        "50), pass varchar(6))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = """create table rights(nic varchar(100), se varchar(3),ss varchar(3),sed varchar(3),
                sa varchar(3),sn varchar(3),sr varchar(3),sd varchar(3), te varchar(3),ts varchar(3),ted varchar(3),
                tg varchar(3),tr varchar(3), ma varchar(3),med varchar(3),mv varchar(3),mr varchar(3), inv varchar(3),
                inm varchar(3),ins varchar(3),ind varchar(3),inr varchar(3), lib varchar(3))"""
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from teacher where nic=%s"
            parameter = [g_nic.get()]
            mycursor.execute(query, parameter)
            res = mycursor.fetchone()

            if res is not None:
                query = "select * from grader where nic = %s"
                parameter = [g_nic.get()]
                mycursor.execute(query, parameter)
                result = mycursor.fetchone()

                if result is not None:
                    respond = messagebox.askyesno("Assigned", "Data Available Already, Do You Want Update Data?")
                    if respond:
                        query = "update grader set class_group=%s, class=%s, pass=%s where nic=%s"
                        parameter = [g_class_group.get(), g_class.get(), otp, g_nic.get()]
                        mycursor.execute(query, parameter)
                        con.commit()
                    else:
                        pass
                else:
                    query = " insert into grader values (%s,%s,%s,%s,%s)"
                    parameter = [g_nic.get(), g_name.get(), g_class_group.get(), g_class.get(), otp]
                    mycursor.execute(query, parameter)
                    query = "insert into rights (nic) values (%s)"
                    parameter = [g_nic.get()]
                    mycursor.execute(query, parameter)
                    con.commit()
            else:
                messagebox.showerror("error", "Teacher Not Found, Invalid Nic")

            con.close()
        collect()

    def pass_show():
        if mode.get() == "Password Mode":
            if g_nic.get() == "":
                messagebox.showerror("error", "Enter Nic Number")
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
                except:
                    messagebox.showerror("Error", "Database Failing")
                    return

                query = "select pass from grader where nic=%s"
                parameter = [g_nic.get()]
                mycursor.execute(query, parameter)
                res = mycursor.fetchone()
                messagebox.showinfo("Pass", "Your Password is : " + res[0])
                con.close()
        else:
            messagebox.showerror("Error", "Please Select -Pass Mode- to Show Pass")

    def mode_sel():
        if mode.get() == "Add Mode":
            g_nic.config(state="normal")
            g_name.config(state="normal")
            g_class_group.config(state="readonly")
            g_class.config(state="readonly")
        elif mode.get() == "Password Mode":
            g_nic.config(state="normal")
            g_name.config(state="normal")
            g_class_group.config(state="disabled")
            g_class.config(state="disabled")

    try:
        option = ["Add Mode", "Password Mode"]
        mode = ttk.Combobox(grader, font=fonts, foreground=fg, values=option, state="readonly")
        mode.place(x=22, y=306, width=172, height=34)
        mode.set(option[0])
        mode.bind("<<ComboboxSelected>>", lambda event: mode_sel())

        def Select(text):
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
                messagebox.showerror("Error", "Database Failing")
                return

            query = '''
                    select nic,full_name from teacher where nic LIKE '%''' + text + '''%' or 
                    full_name like '%''' + text + '''%'
                    '''
            mycursor.execute(query)
            res = mycursor.fetchall()
            con.close()
            value = []
            if res is not None:
                for row in res:
                    value.append((row[0]).strip("{}\""))
                g_nic.configure(values=value)
            get()

        def get():
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
                messagebox.showerror("Error", "Database Failing")
                return

            query = '''
                    select full_name from teacher where nic = %s
                    '''
            para = [g_nic.get()]
            mycursor.execute(query, para)
            res = mycursor.fetchone()
            con.close()

            if res is not None:
                name = res[0]
                # print(name)
                g_name.delete(0, END)
                g_name.insert(0, name)

        g_nic = ttk.Combobox(grader, font=fonts, foreground=fg)
        g_nic.place(x=253, y=161, width=341, height=23)
        g_nic.bind("<KeyRelease>", lambda event: Select(g_nic.get()))
        g_nic.bind("<<ComboboxSelected>>", lambda event: get())

        g_name = Entry(grader, font=fonts, foreground=fg, bg="white", border=1)
        g_name.place(x=253, y=228, width=341, height=23)

        option = ["Secondary", "Under O/L", "Under A/L", "13 Years", "Other"]
        g_class_group = ttk.Combobox(grader, font=fonts, foreground=fg, values=option, state="readonly")
        g_class_group.place(x=253, y=298, width=156, height=23)
        g_class_group.bind("<<ComboboxSelected>>", lambda event: g_chooser())

        def g_chooser():
            if g_class_group.get() == "Secondary":
                options_g6 = ["6A", "6B", "6C", "6D", "6E", "6F"]
                options_g7 = ["7A", "7B", "7C", "7D", "7E", "7F"]
                options_g8 = ["8A", "6B", "8C", "8D", "8E", "8F"]
                options_g9 = ["9A", "9B", "9C", "9D", "9E", "9F"]
                options = options_g6 + options_g7 + options_g8 + options_g9
                g_class.config(values=options)
                g_class.set(options_g6[0])
            elif g_class_group.get() == "Under O/L":
                options_g10 = ["10A", "10B", "10C", "10D", "10E", "10F"]
                options_g11 = ["11A", "11B", "11C", "11D", "11E", "11F"]
                options = options_g11 + options_g10
                g_class.config(values=options)
                g_class.set(options_g10[0])
            elif g_class_group.get() == "Under A/L":
                options_g12a = ["12artA", "12artB", "12artC", "12artD", "12artE", "12artF"]
                options_g12c = ["12commerceA", "12commerceB", "12commerceC"]
                options_g12s = ["12scienceA", "12scienceB", "12scienceC"]
                options_g13a = ["13artA", "13artB", "12artC", "13artD", "13artE", "13artF"]
                options_g13c = ["13commerceA", "13commerceB", "13commerceC"]
                options_g13s = ["13scienceA", "13scienceB", "13scienceC"]
                options = options_g12a + options_g13c + options_g12s + options_g12c + options_g13s + options_g13a
                g_class.config(values=options)
                g_class.set(options_g12a[0])
            elif g_class_group.get() == "Other":
                option_other = ["None"]
                options = option_other
                g_class.config(values=options)
                g_class.set(option_other[0])
            elif g_class_group.get() == "13 Years":
                options_g13y = ["13 year A", "13 year B"]
                options = options_g13y
                g_class.config(values=options)
                g_class.set(option[0])

        g_class = ttk.Combobox(grader, font=fonts, foreground=fg, state="readonly")
        g_class.place(x=438, y=298, width=156, height=23)

        fontl = ("Calibri", 12, "bold")

        add = Button(grader, text="PROMOTE", bg="#3b3086", fg="white", font=fontl, command=add_grader)
        add.place(x=22, y=351, width=172, height=34)

        show = Button(grader, text="SHOW PASSWORD", bg="#3b3086", fg="white", font=fontl, command=pass_show)
        show.place(x=22, y=395, width=172, height=34)
    except:
        pass

    mode_sel()

    try:
        view = ttk.Treeview(grader)
        view.place(x=634, y=126, width=518, height=496)

        view["columns"] = ("1", "2", "3", "4")
        view["show"] = "headings"

        view.column("1", minwidth=10, width=15)
        view.column("2", minwidth=50, width=100)
        view.column("3", minwidth=30, width=40)
        view.column("4", minwidth=20, width=30)

        view.heading("1", text="Nic")
        view.heading("2", text="Name")
        view.heading("3", text="Group")
        view.heading("4", text="Class")
    except:
        pass

    collect()


def ur(frame):
    right = Frame(frame, height=651, width=1185)
    right.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.ur/UR.png")
    Background = Label(right, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    try:
        stf = Frame(right, bg="#e1edf5")
        stf.place(x=144, y=258, width=45, height=265)

        def full():
            if fulla.get() == "on":
                student_enroll.select()
                student_edit.select()
                student_search.select()
                student_acadamic.select()
                student_note.select()
                student_report.select()
                student_delete.select()
            elif fulla.get() == "off":
                student_enroll.deselect()
                student_edit.deselect()
                student_search.deselect()
                student_acadamic.deselect()
                student_note.deselect()
                student_report.deselect()
                student_delete.deselect()

        color = "#e1edf5"
        fulla = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912"
                                        , command=full)
        fulla.place(y=15)

        student_enroll = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        student_enroll.place(y=59)

        student_search = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        student_search.place(y=87)

        student_edit = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                               onvalue="on", offvalue="off", text="", bg_color=color,
                                               progress_color="#ce4912")
        student_edit.place(y=115)

        student_acadamic = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                   onvalue="on", offvalue="off", text="", bg_color=color,
                                                   progress_color="#ce4912")
        student_acadamic.place(y=143)

        student_note = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                               onvalue="on", offvalue="off", text="", bg_color=color,
                                               progress_color="#ce4912")
        student_note.place(y=171)

        student_report = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        student_report.place(y=199)

        student_delete = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        student_delete.place(y=227)
    except:
        pass

    try:
        stf = Frame(right, bg="#e1edf5")
        stf.place(x=341, y=258, width=45, height=265)

        def check():
            if tfull.get() == "on":
                teacher_enroll.select()
                teacher_edit.select()
                teacher_search.select()
                teacher_grader.select()
                teacher_right.select()
            elif tfull.get() == "off":
                teacher_enroll.deselect()
                teacher_edit.deselect()
                teacher_search.deselect()
                teacher_grader.deselect()
                teacher_right.deselect()

        color = "#e1edf5"
        tfull = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912"
                                        , command=check)
        tfull.place(y=15)

        teacher_enroll = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        teacher_enroll.place(y=59)

        teacher_search = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        teacher_search.place(y=87)

        teacher_edit = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                               onvalue="on", offvalue="off", text="", bg_color=color,
                                               progress_color="#ce4912")
        teacher_edit.place(y=115)

        teacher_grader = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                 onvalue="on", offvalue="off", text="", bg_color=color,
                                                 progress_color="#ce4912")
        teacher_grader.place(y=143)

        teacher_right = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                                onvalue="on", offvalue="off", text="", bg_color=color,
                                                progress_color="#ce4912")
        teacher_right.place(y=171)

        treport = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                          onvalue="on", offvalue="off", text="", bg_color=color,
                                          progress_color="#ce4912", state="disabled")
        treport.place(y=199)

        tdelete = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                          onvalue="on", offvalue="off", text="", bg_color=color,
                                          progress_color="#ce4912", state="disabled")
        tdelete.place(y=227)
    except:
        pass

    try:
        stf = Frame(right, bg="#e1edf5")
        stf.place(x=539, y=258, width=45, height=265)

        def check():
            if fullm.get() == "on":
                add.select()
                edit.select()
                view.select()
                report.select()
            elif fullm.get() == "off":
                add.deselect()
                edit.deselect()
                view.deselect()
                report.deselect()

        color = "#e1edf5"
        fullm = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912"
                                        , command=check)
        fullm.place(y=15)

        add = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                      onvalue="on", offvalue="off", text="", bg_color=color,
                                      progress_color="#ce4912")
        add.place(y=59)

        edit = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                       onvalue="on", offvalue="off", text="", bg_color=color,
                                       progress_color="#ce4912")
        edit.place(y=87)

        view = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                       onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912")
        view.place(y=115)

        report = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                         onvalue="on", offvalue="off", text="", bg_color=color,
                                         progress_color="#ce4912")
        report.place(y=143)

        trans = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912"
                                        , state="disabled")
        trans.place(y=171)
    except:
        pass

    try:
        stf = Frame(right, bg="#e1edf5")
        stf.place(x=736, y=258, width=45, height=265)

        def check():
            if fulli.get() == "on":
                i_view.select()
                i_m.select()
                i_stock.select()
                i_donater.select()
                i_report.select()
            elif fulli.get() == "off":
                i_view.deselect()
                i_m.deselect()
                i_stock.deselect()
                i_donater.deselect()
                i_report.deselect()

        color = "#e1edf5"
        fulli = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912"
                                        , command=check)
        fulli.place(y=15)

        i_view = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                         onvalue="on", offvalue="off", text="", bg_color=color,
                                         progress_color="#ce4912")
        i_view.place(y=59)

        i_m = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                      onvalue="on", offvalue="off", text="", bg_color=color,
                                      progress_color="#ce4912")
        i_m.place(y=87)

        i_stock = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                          onvalue="on", offvalue="off", text="", bg_color=color,
                                          progress_color="#ce4912")
        i_stock.place(y=115)

        i_donater = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                            onvalue="on", offvalue="off", text="", bg_color=color,
                                            progress_color="#ce4912")
        i_donater.place(y=171)

        i_report = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                           onvalue="on", offvalue="off", text="", bg_color=color,
                                           progress_color="#ce4912")
        i_report.place(y=199)
    except:
        pass

    try:
        stf = Frame(right, bg="#e1edf5")
        stf.place(x=934, y=258, width=45, height=265)

        def check():
            if fulll.get() == "on":
                lib.select()
            elif fulll.get() == "off":
                lib.deselect()

        color = "#e1edf5"
        fulll = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                        onvalue="on", offvalue="off", text="", bg_color=color, progress_color="#ce4912",
                                        command=check)
        fulll.place(y=15)

        lib = customtkinter.CTkSwitch(stf, switch_width=44, switch_height=20, button_color="#3b3086",
                                      onvalue="on", offvalue="off", text="", bg_color=color,
                                      progress_color="#ce4912")
        lib.place(y=59)
    except:
        pass

    fg = "#444444"
    fonts = ("Calibri", 12)

    def Select(text):
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
            messagebox.showerror("Error", "Database Failing")
            return

        query = '''
                select nic,name from grader where nic LIKE '%''' + text + '''%' or 
                name like '%''' + text + '''%'
                '''
        mycursor.execute(query)
        res = mycursor.fetchall()
        con.close()
        value = []
        if res is not None:
            for row in res:
                value.append((row[0]).strip("{}\""))
            g_nic.configure(values=value)
        get()

    def get():
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
            messagebox.showerror("Error", "Database Failing")
            return

        query = '''
                select name from grader where nic = %s
                '''
        para = [g_nic.get()]
        mycursor.execute(query, para)
        res = mycursor.fetchone()
        con.close()

        if res is not None:
            name = res[0]
            # print(name)
            g_name.delete(0, END)
            g_name.insert(0, name)

    def collect():
        zero()
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
            messagebox.showerror("Error", "Database Failing")
            return

        query = "select * from rights where nic=%s"
        parameters = [g_nic.get()]
        mycursor.execute(query, parameters)
        r = mycursor.fetchone()
        con.close()

        if r is not None:
            if r[1] == "on":
                student_enroll.select()
            else:
                student_enroll.deselect()
            if r[2] == "on":
                student_search.select()
            else:
                student_search.deselect()
            if r[3] == "on":
                student_edit.select()
            else:
                student_edit.deselect()
            if r[4] == "on":
                student_acadamic.select()
            else:
                student_acadamic.deselect()
            if r[5] == "on":
                student_note.select()
            else:
                student_note.deselect()
            if r[6] == "on":
                student_report.select()
            else:
                student_report.deselect()
            if r[7] == "on":
                student_delete.select()
            else:
                student_delete.deselect()

            if r[8] == "on":
                teacher_enroll.select()
            else:
                teacher_enroll.deselect()
            if r[9] == "on":
                teacher_search.select()
            else:
                teacher_search.deselect()
            if r[10] == "on":
                teacher_edit.select()
            else:
                teacher_edit.deselect()
            if r[11] == "on":
                teacher_grader.select()
            else:
                teacher_grader.deselect()
            if r[12] == "on":
                teacher_right.select()
            else:
                teacher_right.deselect()

            if r[13] == "on":
                add.select()
            else:
                add.deselect()
            if r[14] == "on":
                edit.select()
            else:
                edit.deselect()
            if r[15] == "on":
                view.select()
            else:
                view.deselect()
            if r[16] == "on":
                report.select()
            else:
                report.deselect()

            if r[17] == "on":
                i_view.select()
            else:
                i_view.deselect()
            if r[18] == "on":
                i_m.select()
            else:
                i_m.deselect()
            if r[19] == "on":
                i_stock.select()
            else:
                i_stock.deselect()
            if r[20] == "on":
                i_donater.select()
            else:
                i_donater.deselect()
            if r[21] == "on":
                i_report.select()
            else:
                i_report.deselect()

            if r[22] == "on":
                lib.select()
            else:
                lib.deselect()

    def zero():
        student_enroll.deselect()
        student_edit.deselect()
        student_search.deselect()
        student_acadamic.deselect()
        student_note.deselect()
        student_report.deselect()
        student_delete.deselect()
        teacher_enroll.deselect()
        teacher_edit.deselect()
        teacher_search.deselect()
        teacher_grader.deselect()
        teacher_right.deselect()
        add.deselect()
        edit.deselect()
        view.deselect()
        report.deselect()
        i_view.deselect()
        i_m.deselect()
        i_stock.deselect()
        i_donater.deselect()
        i_report.deselect()
        lib.deselect()

    g_nic = ttk.Combobox(right, font=fonts, foreground=fg)
    g_nic.place(x=80, y=124, width=243, height=23)
    g_nic.bind("<KeyRelease>", lambda event: Select(g_nic.get()))
    g_nic.bind("<<ComboboxSelected>>", lambda event: (get(), collect()))

    g_name = Entry(right, font=fonts, foreground=fg, bg="white", border=1)
    g_name.place(x=367, y=124, width=455, height=23)

    def rights():
        if g_nic.get() == "":
            messagebox.showerror("error", "Nic Required")
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
            except:
                messagebox.showerror("Error", "Database Failing")
                return

            try:
                query = """create table rights(nic varchar(100), se varchar(3),ss varchar(3),sed varchar(3),
                sa varchar(3),sn varchar(3),sr varchar(3),sd varchar(3), te varchar(3),ts varchar(3),ted varchar(3),
                tg varchar(3),tr varchar(3), ma varchar(3),med varchar(3),mv varchar(3),mr varchar(3), inv varchar(3),
                inm varchar(3),ins varchar(3),ind varchar(3),inr varchar(3), lib varchar(3))"""
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from rights where nic=%s"
            parameter = [g_nic.get()]
            mycursor.execute(query, parameter)
            res = mycursor.fetchone()

            if res is not None:
                query = '''
                        update rights set
                        se=%s,ss=%s,sed=%s,sa=%s,sn=%s,sr=%s,sd=%s,
                        te=%s,ts=%s,ted=%s,tg=%s,tr=%s,
                        ma=%s,med=%s,mv=%s,mr=%s,
                        inv=%s,inm=%s,ins=%s,ind=%s,inr=%s,
                        lib=%s where nic = %s
                        '''
                parameters = [student_enroll.get(), student_search.get(), student_edit.get(),
                              student_acadamic.get(), student_note.get(), student_report.get(), student_report.get(),
                              teacher_enroll.get(), teacher_search.get(), teacher_edit.get(), teacher_grader.get(),
                              teacher_right.get(),
                              add.get(), edit.get(), view.get(), report.get(),
                              i_view.get(), i_m.get(), i_stock.get(), i_donater.get(), i_report.get(),
                              lib.get(), g_nic.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("success", "Data Updated")
            elif res is None:
                query = "insert into rights values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                        "%s,%s)"
                parameters = [g_nic.get(), student_enroll.get(), student_search.get(), student_edit.get(),
                              student_acadamic.get(), student_note.get(), student_report.get(), student_report.get(),
                              teacher_enroll.get(), teacher_search.get(), teacher_edit.get(), teacher_grader.get(),
                              teacher_right.get(),
                              add.get(), edit.get(), view.get(), report.get(),
                              i_view.get(), i_m.get(), i_stock.get(), i_donater.get(), i_report.get(),
                              lib.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("success", "Settings Saved")
            else:
                messagebox.showerror("Error", "Process Failed !")

    fontl = ("Calibri", 12, "bold")

    save = Button(right, text="SAVE", bg="#3b3086", fg="white", font=fontl, command=rights)
    save.place(x=314, y=577, width=172, height=34)


def pc(frame):
    code = Frame(frame, height=651, width=1185)
    code.pack()

    back = PhotoImage(file=current + "/.ux/padma/.teacher/.pc/pc.png")
    Background = Label(code, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Candara", 12)
    reset_nic = Entry(code, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff")
    reset_nic.place(x=747, y=212, width=291, height=34)
    reset_nic.insert(0, nic)
    reset_nic.config(state="readonly")

    def non_enter():
        old_pass.select_range(0, END)

    def non_leave():
        get = old_pass.get()
        if get == "":
            old_pass.insert(0, " Enter Old Password")

    old_pass = Entry(code, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff", show="*")
    old_pass.place(x=747, y=279, width=291, height=34)
    old_pass.insert(0, " Enter Old Password")
    old_pass.config(state=control)
    old_pass.bind("<FocusIn>", lambda event: non_enter())
    old_pass.bind("<FocusOut>", lambda event: non_leave())

    # old_pass.insert(0, " NIC")

    def pon_enter():
        new_pass.select_range(0, END)

    def pon_leave():
        get = new_pass.get()
        if get == "":
            new_pass.insert(0, " Enter New Password")

    def validate_entry(text):
        if len(text) > 6:
            return False
        return True

    validate_command = code.register(validate_entry)

    new_pass = Entry(code, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff", show="*"
                     , validatecommand=(validate_command, "%P"), validate="key")
    new_pass.place(x=747, y=347, width=291, height=34)
    new_pass.insert(0, "000000")
    new_pass.config(state=control)
    new_pass.bind("<FocusIn>", lambda event: pon_enter())
    new_pass.bind("<FocusOut>", lambda event: pon_leave())

    def pone_enter():
        re_new_pass.select_range(0, END)

    def pone_leave():
        get = re_new_pass.get()
        if get == "":
            re_new_pass.insert(0, " Re-Enter New Password")

    re_new_pass = Entry(code, fg="#1b2d52", font=fonts, bd=0, bg="#f8fbff", show="*"
                        , validatecommand=(validate_command, "%P"), validate="key")
    re_new_pass.place(x=747, y=415, width=291, height=34)
    re_new_pass.insert(0, "000000")
    re_new_pass.config(state=control)
    re_new_pass.bind("<FocusIn>", lambda event: pone_enter())
    re_new_pass.bind("<FocusOut>", lambda event: pone_leave())

    def submit():
        if new_pass.get() == re_new_pass.get():
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
                messagebox.showerror("Error", "Database Failing")
                return

            query = "select * from grader where nic=%s and pass=%s"
            parameters = [reset_nic.get(), old_pass.get()]
            mycursor.execute(query, parameters)
            res = mycursor.fetchone()

            if res is not None:
                query = "update grader set pass=%s where nic=%s"
                parameters = [new_pass.get(), reset_nic.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("success", "Passcode Updated")
            else:
                messagebox.showerror("error", "old passcode is incorrect")
                con.close()
        else:
            messagebox.showerror("error", "new passcodes are does not match")
            new_pass.delete(0, END)
            re_new_pass.delete(0, END)

    # Buttons
    fonts = ("Candara", 15, "bold")
    signup_btn = Button(code, bg="#ce4912", fg="white", text="CHANGE", font=fonts, bd=0, command=submit)
    signup_btn.place(x=747, y=474, width=291, height=48)


def bulk():
    BUlk_win = Toplevel()
    BUlk_win.grab_set()

    screen_width = BUlk_win.winfo_screenwidth()
    screen_height = BUlk_win.winfo_screenheight()
    window_width = 500
    window_height = 537
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    BUlk_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

    BUlk_win.iconbitmap("pad.ico")
    BUlk_win.title("Bulk Data")
    BUlk_win.resizable(False, False)
    BUlk_win.transient()

    back = PhotoImage(file=current + "/.ux/padma/.student/.bulk/Bulking.png")
    back_p = Label(BUlk_win, image=back)
    back_p.image = back
    back_p.pack()

    def transfer_excel_to_mysql_student():
        info.delete(0, END)
        info_bar["value"] = 0
        # Open file dialog to select the Excel file
        Tk().withdraw()
        excel_file = askopenfilename(title="Select Excel file", filetypes=[("Excel Files", "*.xlsx")])

        if excel_file != "":
            info_bar["value"] = 25
            info.insert(END, "Reading The Excel And Validating.....")
            # Read Excel data into a pandas DataFrame, skipping the first row
            df = pd.read_excel(excel_file, skiprows=2)

            # MySQL database connection details
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)
            mysql_database = "pcc"
            mysql_table = "teacher"

            # Connect to the MySQL database
            cnx = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=mysql_database
            )
            cursor = cnx.cursor()

            # Create the MySQL table if it doesn't exist
            columns = [f"`{col}` VARCHAR(255)" for col in df.columns]
            create_table_query = f"CREATE TABLE IF NOT EXISTS {mysql_table} ({', '.join(columns)});"
            cursor.execute(create_table_query)

            # Check for existing IDs in the MySQL table
            existing_ids = set()
            cursor.execute(f"SELECT {df.columns[0]} FROM {mysql_table};")
            result = cursor.fetchall()
            if result:
                existing_ids = {row[0] for row in result}

            # Check for existing IDs in the Excel file
            excel_ids_set = set(df[df.columns[0]].astype(str))

            # Transfer data from DataFrame to MySQL table, skipping existing IDs
            rows_to_insert = []
            skipped_excel_ids = [id for id in excel_ids_set if id in existing_ids]
            info.insert(END, "Collecting the data from Excel")
            info_bar["value"] = 50
            for row in df.itertuples(index=False):
                if row[0] not in existing_ids and row[0] not in excel_ids_set:
                    rows_to_insert.append(tuple(pd.NaT if pd.isnull(value) else value for value in row))
                else:
                    info.insert(END, f"ID {row[0]} already exists. Teacher Skipping...")

            if rows_to_insert:
                insert_query = f"INSERT INTO {mysql_table} VALUES ({','.join(['%s'] * len(df.columns))})"
                cursor.executemany(insert_query, rows_to_insert)
                # Commit the changes and close the connection
                cnx.commit()
                info_bar["value"] = 75
                info.insert(END, "Bulk Imported Successfully !")
            else:
                info.insert(END, "No New Record was Imported !")
                info_bar["value"] = 10

            if skipped_excel_ids:
                info.insert(END, "Skipped IDs from Excel:")
                for skipped_id in skipped_excel_ids:
                    info.insert(END, skipped_id)

            cursor.close()
            cnx.close()
            info.insert(END, "Bulk Import Procedure Successfully Ended !")
            info_bar["value"] = 100
        else:
            info.insert(END, "No Excel file selected")
            info_bar["value"] = 0
            info.insert(END, "Bulk Import Procedure Aborted !")

    fontl = ("Candara", 14, "bold")

    teacher = Button(BUlk_win, text="Choose Excel File", bg="#ce4912", fg="white", font=fontl,
                     command=transfer_excel_to_mysql_student)
    teacher.place(x=48, y=225, width=404, height=34)

    info = Listbox(BUlk_win)
    info.place(x=48, y=284, height=161, width=387)

    scrollbar = tk.Scrollbar(BUlk_win)
    scrollbar.place(x=435, y=284, height=161)
    info.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=info.yview)

    info_bar = ttk.Progressbar(BUlk_win, orient=HORIZONTAL, length=404, mode="determinate")
    info_bar.place(x=48, y=468, height=34)
    info_bar["value"] = 0
