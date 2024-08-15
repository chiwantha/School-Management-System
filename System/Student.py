import tkinter as tk
from tkinter import *
from tkinter import ttk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import winreg
import mysql.connector
from tkinter import messagebox
from datetime import datetime
from fpdf import FPDF
from tkinter import filedialog
import os
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkcalendar import DateEntry

current = os.path.dirname(os.path.realpath(__file__))


def Enrollment(frame):
    enrollment_frame = Frame(frame, height=651, width=1185)
    enrollment_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.enrollment/Student Enrollment.png")
    Background = Label(enrollment_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    now = datetime.now()
    year = now.year

    fonts = ("Calibri", 12)

    def autoad(text):
        parent_address_entry.delete(0, END)
        parent_address_entry.insert(0, text)

    fg = "#444444"
    # Date Control Entries
    try:
        def unlock():
            print("mode selected")
            if mode.get() == "Auto ( grade 6 )":
                enrollment_date.config(state="readonly")
                seq.config(state="normal")
                seq.delete(0, END)
                seq.insert(0, "8")
                seq.config(state="readonly")
                unenrollment_date.config(state="readonly")
                rapid.place_forget()
            elif mode.get() == "Semi Auto( custom )":
                enrollment_date.config(state="readonly")
                seq.config(state="normal")
                unenrollment_date.config(state="readonly")
                rapid.place_forget()
            elif mode.get() == "Manual":
                enrollment_date.config(state="normal")
                seq.config(state="normal")
                unenrollment_date.config(state="normal")
                rapid.place_forget()
            elif mode.get() == "Rapid":
                enrollment_date.config(state="disabled")
                seq.config(state="disabled")
                unenrollment_date.config(state="normal")
                rapid.place(x=171, y=611, width=23, height=23)
            else:
                pass

        options = ["Auto ( grade 6 )", "Semi Auto( custom )", "Manual", "Rapid"]
        mode = ttk.Combobox(enrollment_frame, font=fonts, background="red", values=options, foreground=fg)
        mode.set(options[0])
        mode.config(state="readonly")
        mode.bind("<<ComboboxSelected>>", lambda event: unlock())
        mode.place(x=24, y=438, width=170, height=27)

        enrollment_date = DateEntry(enrollment_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        enrollment_date.place(x=24, y=501, width=170, height=23)
        enrollment_date.config(state="readonly")

        seq = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        seq.place(x=24, y=556, width=170, height=23)
        seq.insert(0, "8")
        seq.config(state="readonly")
        seq.bind("<KeyRelease>", lambda event: cal())

        def cal():
            if seq.get() == "":
                value = 0
            else:
                value = int(seq.get())
            outdate = int(year) + value
            unenrollment_date.config(state="normal")
            unenrollment_date.delete(0, END)
            unenrollment_date.insert(0, outdate)
            unenrollment_date.config(state="readonly")

        def tap_nic():
            unenrollment_date.select_range(0, END)

        def dtap_nic():
            if unenrollment_date.get() == "":
                unenrollment_date.insert(0, year)

        unenrollment_date = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        unenrollment_date.place(x=24, y=611, width=147, height=23)
        cal()
        unenrollment_date.bind("<FocusIn>", lambda event: tap_nic())
        unenrollment_date.bind("<FocusOut>", lambda event: dtap_nic())

        fontl = ("Candara", 14, "bold")

        def rapid_change():
            if student_index_entry.get() == "" or student_index_entry.get() == "index number" or \
                    unenrollment_date.get() == "":
                messagebox.showerror("Error", "Student Index & Unenrollment Date is Compulsory !")
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

                query = "Select full_name from Student where id=%s"
                parameters = [student_index_entry.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()

                if result is not None:
                    respond = messagebox.askyesno("confirm", "Do You Really Want Say Bye To - " + result[0])
                    if respond:
                        query = "update student set und=%s where id=%s"
                        parameters = [unenrollment_date.get(), student_index_entry.get()]
                        mycursor.execute(query, parameters)
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success", "Data Updated")
                    else:
                        pass
                else:
                    messagebox.showerror("Error", "Unknown Student Or Invalid Index")
                con.close()

        rapid = Button(enrollment_frame, text="X", bg="red", fg="white", font=fontl, bd=0, command=rapid_change)
    except:
        pass

    # Student Entries
    try:
        def tap_index():
            student_index_entry.select_range(0, END)

        def dtap_index():
            if student_index_entry.get() == "":
                student_index_entry.insert(0, "index number")

        student_index_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_index_entry.place(x=297, y=152, width=243, height=23)
        student_index_entry.insert(0, "index number")
        student_index_entry.bind("<FocusIn>", lambda event: tap_index())
        student_index_entry.bind("<FocusOut>", lambda event: dtap_index())

        student_DOB_entry = DateEntry(enrollment_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        student_DOB_entry.place(x=577, y=152, width=243, height=23)

        def ftap_fam():
            student_full_name_entry.select_range(0, END)

        def fdtap_fam():
            if student_full_name_entry.get() == "":
                student_full_name_entry.insert(0, "ful name with initials")

        student_full_name_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_full_name_entry.place(x=857, y=152, width=243, height=23)
        student_full_name_entry.insert(0, "ful name with initials")
        student_full_name_entry.bind("<FocusIn>", lambda event: ftap_fam())
        student_full_name_entry.bind("<FocusOut>", lambda event: fdtap_fam())

        def tap_fam():
            student_Family_name_entry.select_range(0, END)

        def dtap_fam():
            if student_Family_name_entry.get() == "":
                student_Family_name_entry.insert(0, "family name")

        student_Family_name_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_Family_name_entry.place(x=297, y=208, width=243, height=23)
        student_Family_name_entry.insert(0, "family name")
        student_Family_name_entry.bind("<FocusIn>", lambda event: tap_fam())
        student_Family_name_entry.bind("<FocusOut>", lambda event: dtap_fam())

        def tap_fn():
            student_F_name_entry.select_range(0, END)

        def dtap_fn():
            if student_F_name_entry.get() == "":
                student_F_name_entry.insert(0, "first name")

        student_F_name_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_F_name_entry.place(x=577, y=208, width=243, height=23)
        student_F_name_entry.insert(0, "first name")
        student_F_name_entry.bind("<FocusIn>", lambda event: tap_fn())
        student_F_name_entry.bind("<FocusOut>", lambda event: dtap_fn())

        def tap_ln():
            student_L_name_entry.select_range(0, END)

        def dtap_ln():
            if student_L_name_entry.get() == "":
                student_L_name_entry.insert(0, "last name")

        student_L_name_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_L_name_entry.place(x=857, y=208, width=243, height=23)
        student_L_name_entry.insert(0, "last name")
        student_L_name_entry.bind("<FocusIn>", lambda event: tap_ln())
        student_L_name_entry.bind("<FocusOut>", lambda event: dtap_ln())

        def tap_ad():
            student_address_entry.select_range(0, END)

        def dtap_ad():
            if student_address_entry.get() == "":
                student_address_entry.insert(0, "eg : No 315/A example,")

        student_address_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_address_entry.place(x=297, y=267, width=243, height=23)
        student_address_entry.insert(0, "eg : No 315/A example,")
        student_address_entry.bind("<FocusIn>", lambda event: tap_ad())
        student_address_entry.bind("<FocusOut>", lambda event: dtap_ad())
        student_address_entry.bind("<KeyRelease>", lambda event: autoad(student_address_entry.get()))

        def tap_adl():
            student_address_line_entry.select_range(0, END)

        def dtap_adl():
            if student_address_line_entry.get() == "":
                student_address_line_entry.insert(0, "address line 2 ( optional )")

        student_address_line_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_address_line_entry.place(x=577, y=267, width=243, height=23)
        student_address_line_entry.insert(0, "address line 2 ( optional )")
        student_address_line_entry.bind("<FocusIn>", lambda event: tap_adl())
        student_address_line_entry.bind("<FocusOut>", lambda event: dtap_adl())

        def tap_ci():
            student_city_entry.select_range(0, END)

        def dtap_ci():
            if student_city_entry.get() == "":
                student_city_entry.insert(0, "your city")

        student_city_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_city_entry.place(x=857, y=267, width=243, height=23)
        student_city_entry.insert(0, "your city")
        student_city_entry.bind("<FocusIn>", lambda event: tap_ci())
        student_city_entry.bind("<FocusOut>", lambda event: dtap_ci())

        options = ["Buddhism", "Christian", "Muslim", "Other"]
        student_religion_entry = ttk.Combobox(enrollment_frame, font=fonts, background="red", values=options
                                              , foreground=fg)
        student_religion_entry.set(options[0])
        student_religion_entry.place(x=297, y=324, width=243, height=23)
        student_religion_entry.config(state="readonly")

        options = ["Male", "Female", "Other"]
        student_gender_entry = ttk.Combobox(enrollment_frame, font=fonts, background="red", values=options
                                            , foreground=fg)
        student_gender_entry.set(options[0])
        student_gender_entry.place(x=577, y=324, width=243, height=23)
        student_gender_entry.config(state="readonly")

        def tap_nic():
            student_nic_entry.select_range(0, END)

        def dtap_nic():
            if student_nic_entry.get() == "":
                student_nic_entry.insert(0, "nic ( optional )")

        student_nic_entry = Entry(enrollment_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_nic_entry.place(x=857, y=324, width=243, height=23)
        student_nic_entry.insert(0, "nic ( optional )")
        student_nic_entry.bind("<FocusIn>", lambda event: tap_nic())
        student_nic_entry.bind("<FocusOut>", lambda event: dtap_nic())
    except:
        pass

    # parent Entries
    try:
        def tap_pfn():
            parent_F_name_entry.select_range(0, END)

        def dtap_pfn():
            if parent_F_name_entry.get() == "":
                parent_F_name_entry.insert(0, "full name with initials")

        parent_F_name_entry = Entry(enrollment_frame, font=fonts, bd=0, fg=fg)
        parent_F_name_entry.place(x=298, y=419, width=522, height=23)
        parent_F_name_entry.insert(0, "full name with initials")
        parent_F_name_entry.bind("<FocusIn>", lambda event: tap_pfn())
        parent_F_name_entry.bind("<FocusOut>", lambda event: dtap_pfn())

        options = ["Parents", "GrandParents", "Sibling", "Other"]
        parent_parentship = ttk.Combobox(enrollment_frame, font=fonts, background="red", values=options
                                         , foreground=fg)
        parent_parentship.set(options[0])
        parent_parentship.place(x=857, y=419, width=243, height=23)
        parent_parentship.config(state="readonly")

        def tap_pad():
            parent_address_entry.select_range(0, END)

        def dtap_pad():
            if parent_address_entry.get() == "":
                parent_address_entry.insert(0, "eg : No 315/A example,")

        parent_address_entry = Entry(enrollment_frame, font=fonts, bd=0, fg=fg)
        parent_address_entry.place(x=298, y=477, width=522, height=23)
        parent_address_entry.insert(0, "eg : No 315/A example,")
        parent_address_entry.bind("<FocusIn>", lambda event: tap_pad())
        parent_address_entry.bind("<FocusOut>", lambda event: dtap_pad())

        def tap_pci():
            parent_profession_entry.select_range(0, END)

        def dtap_pci():
            if parent_profession_entry.get() == "":
                parent_profession_entry.insert(0, "your profession")

        parent_profession_entry = Entry(enrollment_frame, font=fonts, bd=0, fg=fg)
        parent_profession_entry.place(x=857, y=477, width=243, height=23)
        parent_profession_entry.insert(0, "your profession")
        parent_profession_entry.bind("<FocusIn>", lambda event: tap_pci())
        parent_profession_entry.bind("<FocusOut>", lambda event: dtap_pci())

        options = ["Buddhism", "Christian", "Muslim", "Other"]
        parent_religion_entry = ttk.Combobox(enrollment_frame, font=fonts, background="red", values=options
                                             , foreground=fg)
        parent_religion_entry.set(options[0])
        parent_religion_entry.place(x=297, y=534, width=243, height=23)
        parent_religion_entry.config(state="readonly")

        def tap_pp():
            parent_pone_entry.select_range(0, END)

        def dtap_pp():
            if parent_pone_entry.get() == "":
                parent_pone_entry.insert(0, "071 12. ..")

        def validate_entry(text):
            if len(text) > 10:
                return False
            return True

        validate_command = enrollment_frame.register(validate_entry)

        parent_pone_entry = tk.Entry(enrollment_frame, font=fonts, bd=0, fg=fg, validate="key",
                                     validatecommand=(validate_command, "%P"))
        parent_pone_entry.place(x=577, y=534, width=243, height=23)
        parent_pone_entry.insert(0, "071 12. ..")
        parent_pone_entry.bind("<FocusIn>", lambda event: tap_pp())
        parent_pone_entry.bind("<FocusOut>", lambda event: dtap_pp())

        def tap_pnic():
            parent_nic_entry.select_range(0, END)

        def dtap_pnic():
            if parent_nic_entry.get() == "":
                parent_nic_entry.insert(0, "nic ( optional )")

        parent_nic_entry = Entry(enrollment_frame, font=fonts, bd=0, fg=fg)
        parent_nic_entry.place(x=857, y=534, width=243, height=23)
        parent_nic_entry.insert(0, "nic ( optional )")
        parent_nic_entry.bind("<FocusIn>", lambda event: tap_pnic())
        parent_nic_entry.bind("<FocusOut>", lambda event: dtap_pnic())
    except:
        pass

    # noinspection PyBroadException
    def add_data():
        if student_index_entry.get() == "" \
                or student_index_entry.get() == "index number" \
                or student_full_name_entry.get() == "" \
                or student_Family_name_entry.get() == "" \
                or student_F_name_entry.get() == "" \
                or student_L_name_entry.get() == "" \
                or student_DOB_entry.get() == "" \
                or student_address_entry.get() == "" \
                or student_city_entry.get() == "" \
                or student_religion_entry.get() == "" \
                or student_gender_entry.get() == "" \
                or enrollment_date.get() == "" \
                or unenrollment_date.get() == "":
            messagebox.showerror("Error", "All Student Data Required")
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
                query = "CREATE TABLE student (id int,dob DATE," \
                        "full_name varchar(200),family_name VARCHAR(100),first_name VARCHAR(100),last_name VARCHAR(" \
                        "100)," \
                        "address VARCHAR(100), address_line VARCHAR(100), city VARCHAR(50)," \
                        "religion VARCHAR(50), gender VARCHAR(50), nic VARCHAR(50), enroll_date varchar(20)," \
                        "und varchar(5))"
                mycursor.execute(query)
                con.commit()
            except:
                pass
            try:
                query = "create table parents(id int,name varchar(200)," \
                        "relation varchar(50),address varchar(100),pro varchar(100)," \
                        "religion varchar(50),pone varchar(10),nic varchar(100))"
                mycursor.execute(query)
                con.commit()
                # print("done tabel parent")
            except:
                # print("Test two Pass")
                pass

            query = "select * from student where id=%s"
            parameters = [student_index_entry.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            query = "select * from parents where id=%s"
            parameters = [student_index_entry.get()]
            mycursor.execute(query, parameters)
            result2 = mycursor.fetchone()

            if result is not None:
                messagebox.showerror("Error", "The Index You Entered already exist")
                print("")
                for Row in result:
                    print(Row)
                for Row in result2:
                    print(Row)
            else:
                query = "insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                parameters = [student_index_entry.get(),
                              student_DOB_entry.get(),
                              student_full_name_entry.get(),
                              student_Family_name_entry.get(),
                              student_F_name_entry.get(),
                              student_L_name_entry.get(),
                              student_address_entry.get(),
                              student_address_line_entry.get(),
                              student_city_entry.get(),
                              student_religion_entry.get(),
                              student_gender_entry.get(),
                              student_nic_entry.get(),
                              enrollment_date.get(),
                              unenrollment_date.get()]
                mycursor.execute(query, parameters)
                query = "insert into parents values (%s,%s,%s,%s,%s,%s,%s,%s)"
                parameters = [student_index_entry.get(),
                              parent_F_name_entry.get(),
                              parent_parentship.get(),
                              parent_address_entry.get(),
                              parent_profession_entry.get(),
                              parent_religion_entry.get(),
                              parent_pone_entry.get(),
                              parent_nic_entry.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                messagebox.showinfo("SUCCESS", "STUDENT added SUCCESSFULLY")

    # noinspection PyBroadException
    '''
    def update():
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE_PADMA")
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

        query = "select id from parents where id=%s"
        parameters = [student_index_entry.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()

        if result is not None:
            query = "update parents set " \
                    "name=%s,relation=%s,address=%s,address_line=%s," \
                    "city=%s,religion=%s,pone=%s,nic=%s where id=%s"
            parameters = [
                parent_F_name_entry.get(),
                parent_parentship.get(),
                parent_address_entry.get(),
                parent_address_line_entry.get(),
                parent_profession_entry.get(),
                parent_religion_entry.get(),
                parent_pone_entry.get(),
                parent_nic_entry.get(),
                student_index_entry.get()
            ]
            mycursor.execute(query, parameters)
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS", "Update Successful")
        else:
            messagebox.showerror("Error", "Wrong Index Number")
    '''

    fontl = ("Candara", 14, "bold")

    btn_student_add = Button(enrollment_frame, text="SUBMIT", bg="#ce4912", fg="white", font=fontl, command=add_data)
    btn_student_add.place(x=254, y=593, width=172, height=34)

    btn_student_update = Button(enrollment_frame, text="UPDATE", bg="#3b3086", fg="white", font=fontl,
                                command=lambda: messagebox.showerror("error", "Cannot Update Here, Go to Edit !"))
    btn_student_update.place(x=446, y=593, width=172, height=34)

    # noinspection PyBroadException
    def delete():
        try:
            student_index_entry.delete(0, END)
            student_full_name_entry.delete(0, END)
            student_Family_name_entry.delete(0, END)
            student_F_name_entry.delete(0, END)
            student_L_name_entry.delete(0, END)
            student_address_entry.delete(0, END)
            student_address_line_entry.delete(0, END)
            student_city_entry.delete(0, END)
            student_nic_entry.delete(0, END)

            parent_F_name_entry.delete(0, END)
            parent_address_entry.delete(0, END)
            parent_profession_entry.delete(0, END)
            parent_pone_entry.delete(0, END)
            parent_nic_entry.delete(0, END)
        except:
            pass
        try:
            student_index_entry.insert(0, "index number")
            student_full_name_entry.insert(0, "full name with initials")
            student_Family_name_entry.insert(0, "family name")
            student_F_name_entry.insert(0, "first name")
            student_L_name_entry.insert(0, "last name")
            student_address_entry.insert(0, "eg : No 315/A example,")
            student_address_line_entry.insert(0, "address line 2 ( optional )")
            student_city_entry.insert(0, "your city")
            student_nic_entry.insert(0, "nic ( optional )")

            parent_F_name_entry.insert(0, "full name with initials")
            parent_address_entry.insert(0, "eg : No 315/A example,")
            parent_profession_entry.insert(0, "your profession")
            parent_pone_entry.insert(0, "071 12. ..")
            parent_nic_entry.insert(0, "nic ( optional )")
        except:
            pass

    btn_student_del = Button(enrollment_frame, text="CLEAR", bg="#3b3086", fg="white", font=fontl, command=delete)
    btn_student_del.place(x=638, y=593, width=172, height=34)

    def load():
        enrollment_frame.destroy()
        Search(frame)

    search_student = Button(enrollment_frame, text="SEARCH", bg="#3b3086", fg="white", font=fontl, command=load)
    search_student.place(x=11, y=334, width=194, height=34)

    Bulk = Button(enrollment_frame, text="Import as Bulk", bg="#3b3086", fg="white", font=fontl, command=bulk)
    Bulk.place(x=11, y=280, width=194, height=34)


def Edit(frame):
    edit_frame = Frame(frame, height=651, width=1185)
    edit_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.edit/Edit.png")
    Background = Label(edit_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    # now = datetime.now()
    # year = now.year

    fonts = ("Calibri", 12)

    def autoad(text):
        parent_address_entry.delete(0, END)
        parent_address_entry.insert(0, text)

    fg = "#444444"

    # Student Entries
    try:
        student_DOB_entry = DateEntry(edit_frame, selectmode="day", date_pattern="yyyy/mm/dd")
        student_DOB_entry.place(x=577, y=152, width=243, height=23)

        def ftap_fam():
            student_full_name_entry.select_range(0, END)

        def fdtap_fam():
            if student_full_name_entry.get() == "":
                student_full_name_entry.insert(0, "ful name with initials")

        student_full_name_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_full_name_entry.place(x=857, y=152, width=243, height=23)
        student_full_name_entry.insert(0, "ful name with initials")
        student_full_name_entry.bind("<FocusIn>", lambda event: ftap_fam())
        student_full_name_entry.bind("<FocusOut>", lambda event: fdtap_fam())

        def tap_fam():
            student_Family_name_entry.select_range(0, END)

        def dtap_fam():
            if student_Family_name_entry.get() == "":
                student_Family_name_entry.insert(0, "family name")

        student_Family_name_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_Family_name_entry.place(x=297, y=208, width=243, height=23)
        student_Family_name_entry.insert(0, "family name")
        student_Family_name_entry.bind("<FocusIn>", lambda event: tap_fam())
        student_Family_name_entry.bind("<FocusOut>", lambda event: dtap_fam())

        def tap_fn():
            student_F_name_entry.select_range(0, END)

        def dtap_fn():
            if student_F_name_entry.get() == "":
                student_F_name_entry.insert(0, "first name")

        student_F_name_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_F_name_entry.place(x=577, y=208, width=243, height=23)
        student_F_name_entry.insert(0, "first name")
        student_F_name_entry.bind("<FocusIn>", lambda event: tap_fn())
        student_F_name_entry.bind("<FocusOut>", lambda event: dtap_fn())

        def tap_ln():
            student_L_name_entry.select_range(0, END)

        def dtap_ln():
            if student_L_name_entry.get() == "":
                student_L_name_entry.insert(0, "last name")

        student_L_name_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_L_name_entry.place(x=857, y=208, width=243, height=23)
        student_L_name_entry.insert(0, "last name")
        student_L_name_entry.bind("<FocusIn>", lambda event: tap_ln())
        student_L_name_entry.bind("<FocusOut>", lambda event: dtap_ln())

        def tap_ad():
            student_address_entry.select_range(0, END)

        def dtap_ad():
            if student_address_entry.get() == "":
                student_address_entry.insert(0, "eg : No 315/A example,")

        student_address_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_address_entry.place(x=297, y=267, width=243, height=23)
        student_address_entry.insert(0, "eg : No 315/A example,")
        student_address_entry.bind("<FocusIn>", lambda event: tap_ad())
        student_address_entry.bind("<FocusOut>", lambda event: dtap_ad())
        student_address_entry.bind("<KeyRelease>", lambda event: autoad(student_address_entry.get()))

        def tap_adl():
            student_address_line_entry.select_range(0, END)

        def dtap_adl():
            if student_address_line_entry.get() == "":
                student_address_line_entry.insert(0, "address line 2 ( optional )")

        student_address_line_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_address_line_entry.place(x=577, y=267, width=243, height=23)
        student_address_line_entry.insert(0, "address line 2 ( optional )")
        student_address_line_entry.bind("<FocusIn>", lambda event: tap_adl())
        student_address_line_entry.bind("<FocusOut>", lambda event: dtap_adl())

        def tap_ci():
            student_city_entry.select_range(0, END)

        def dtap_ci():
            if student_city_entry.get() == "":
                student_city_entry.insert(0, "your city")

        student_city_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_city_entry.place(x=857, y=267, width=243, height=23)
        student_city_entry.insert(0, "your city")
        student_city_entry.bind("<FocusIn>", lambda event: tap_ci())
        student_city_entry.bind("<FocusOut>", lambda event: dtap_ci())

        options = ["Buddhism", "Christian", "Muslim", "Other"]
        student_religion_entry = ttk.Combobox(edit_frame, font=fonts, background="red", values=options
                                              , foreground=fg)
        student_religion_entry.set(options[0])
        student_religion_entry.place(x=297, y=324, width=243, height=23)
        student_religion_entry.config(state="readonly")

        options = ["Male", "Female", "Other"]
        student_gender_entry = ttk.Combobox(edit_frame, font=fonts, background="red", values=options
                                            , foreground=fg)
        student_gender_entry.set(options[0])
        student_gender_entry.place(x=577, y=324, width=243, height=23)
        student_gender_entry.config(state="readonly")

        def tap_nic():
            student_nic_entry.select_range(0, END)

        def dtap_nic():
            if student_nic_entry.get() == "":
                student_nic_entry.insert(0, "nic ( optional )")

        student_nic_entry = Entry(edit_frame, font=fonts, bg="#e9edfa", bd=0, fg=fg)
        student_nic_entry.place(x=857, y=324, width=243, height=23)
        student_nic_entry.insert(0, "nic ( optional )")
        student_nic_entry.bind("<FocusIn>", lambda event: tap_nic())
        student_nic_entry.bind("<FocusOut>", lambda event: dtap_nic())
    except:
        pass

    # parent Entries
    try:
        def tap_pfn():
            parent_F_name_entry.select_range(0, END)

        def dtap_pfn():
            if parent_F_name_entry.get() == "":
                parent_F_name_entry.insert(0, "full name with initials")

        parent_F_name_entry = Entry(edit_frame, font=fonts, bd=0, fg=fg)
        parent_F_name_entry.place(x=298, y=419, width=522, height=23)
        parent_F_name_entry.insert(0, "full name with initials")
        parent_F_name_entry.bind("<FocusIn>", lambda event: tap_pfn())
        parent_F_name_entry.bind("<FocusOut>", lambda event: dtap_pfn())

        options = ["Parents", "GrandParents", "Sibling", "Other"]
        parent_parentship = ttk.Combobox(edit_frame, font=fonts, background="red", values=options
                                         , foreground=fg)
        parent_parentship.set(options[0])
        parent_parentship.place(x=857, y=419, width=243, height=23)
        parent_parentship.config(state="readonly")

        def tap_pad():
            parent_address_entry.select_range(0, END)

        def dtap_pad():
            if parent_address_entry.get() == "":
                parent_address_entry.insert(0, "eg : No 315/A example,")

        parent_address_entry = Entry(edit_frame, font=fonts, bd=0, fg=fg)
        parent_address_entry.place(x=298, y=477, width=522, height=23)
        parent_address_entry.insert(0, "eg : No 315/A example,")
        parent_address_entry.bind("<FocusIn>", lambda event: tap_pad())
        parent_address_entry.bind("<FocusOut>", lambda event: dtap_pad())

        def tap_pci():
            parent_profession_entry.select_range(0, END)

        def dtap_pci():
            if parent_profession_entry.get() == "":
                parent_profession_entry.insert(0, "your city")

        parent_profession_entry = Entry(edit_frame, font=fonts, bd=0, fg=fg)
        parent_profession_entry.place(x=857, y=477, width=243, height=23)
        parent_profession_entry.insert(0, "your city")
        parent_profession_entry.bind("<FocusIn>", lambda event: tap_pci())
        parent_profession_entry.bind("<FocusOut>", lambda event: dtap_pci())

        options = ["Buddhism", "Christian", "Muslim", "Other"]
        parent_religion_entry = ttk.Combobox(edit_frame, font=fonts, background="red", values=options
                                             , foreground=fg)
        parent_religion_entry.set(options[0])
        parent_religion_entry.place(x=297, y=534, width=243, height=23)
        parent_religion_entry.config(state="readonly")

        def tap_pp():
            parent_pone_entry.select_range(0, END)

        def dtap_pp():
            if parent_pone_entry.get() == "":
                parent_pone_entry.insert(0, "071 12. ..")

        def validate_entry(text):
            if len(text) > 10:
                return False
            return True

        validate_command = edit_frame.register(validate_entry)

        parent_pone_entry = tk.Entry(edit_frame, font=fonts, bd=0, fg=fg, validate="key",
                                     validatecommand=(validate_command, "%P"))
        parent_pone_entry.place(x=577, y=534, width=243, height=23)
        parent_pone_entry.insert(0, "071 12. ..")
        parent_pone_entry.bind("<FocusIn>", lambda event: tap_pp())
        parent_pone_entry.bind("<FocusOut>", lambda event: dtap_pp())

        def tap_pnic():
            parent_nic_entry.select_range(0, END)

        def dtap_pnic():
            if parent_nic_entry.get() == "":
                parent_nic_entry.insert(0, "nic ( optional )")

        parent_nic_entry = Entry(edit_frame, font=fonts, bd=0, fg=fg)
        parent_nic_entry.place(x=857, y=534, width=243, height=23)
        parent_nic_entry.insert(0, "nic ( optional )")
        parent_nic_entry.bind("<FocusIn>", lambda event: tap_pnic())
        parent_nic_entry.bind("<FocusOut>", lambda event: dtap_pnic())
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
            mycursor = con.cursor(buffered=True)
        except:
            messagebox.showerror("Error", "Database Error")
            return

        query = "SELECT id, full_name FROM student WHERE full_name LIKE '%" + text + "%' " \
                                                                                     "OR id LIKE '%" + text + "%' ORDER BY id ASC"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        list.place(x=286, y=180)

        list.delete(0, END)
        for row in result:
            idd = str(row[0])
            list.insert(END, idd + " , " + row[1])

    def select():
        selected_suggestion = list.get(list.curselection()[0])
        selected_suggestion = selected_suggestion.split()
        Key = selected_suggestion[0]

        search_box.delete(0, END)
        search_box.insert(0, Key)

        list.place_forget()
        find()

    def find():
        # noinspection PyBroadException
        try:
            # noinspection PyBroadException
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

            query = "select * from student inner join parents on student.id = parents.id where student.id=%s"
            parameters = [search_box.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()
            # print(result)
            student_DOB_entry.delete(0, END)
            student_Family_name_entry.delete(0, END)
            student_full_name_entry.delete(0, END)
            student_F_name_entry.delete(0, END)
            student_L_name_entry.delete(0, END)
            student_address_entry.delete(0, END)
            student_address_line_entry.delete(0, END)
            student_city_entry.delete(0, END)
            student_religion_entry.delete(0, END)
            student_gender_entry.delete(0, END)
            student_nic_entry.delete(0, END)
            parent_F_name_entry.delete(0, END)
            parent_parentship.delete(0, END)
            parent_address_entry.delete(0, END)
            parent_profession_entry.delete(0, END)
            parent_religion_entry.delete(0, END)
            parent_pone_entry.delete(0, END)
            parent_nic_entry.delete(0, END)

            student_DOB_entry.insert(0, result[1])
            student_Family_name_entry.insert(0, result[3])
            student_full_name_entry.insert(0, result[2])
            student_F_name_entry.insert(0, result[4])
            student_L_name_entry.insert(0, result[5])
            student_address_entry.insert(0, result[6])
            student_address_line_entry.insert(0, result[7])
            student_city_entry.insert(0, result[8])
            student_religion_entry.insert(0, result[9])
            student_gender_entry.insert(0, result[10])
            student_nic_entry.insert(0, result[11])
            parent_F_name_entry.insert(0, result[15])
            parent_parentship.insert(0, result[16])
            parent_address_entry.insert(0, result[17])
            parent_profession_entry.insert(0, result[18])
            parent_religion_entry.insert(0, result[19])
            parent_pone_entry.insert(0, result[20])
            parent_nic_entry.insert(0, result[21])
            con.close()
        except:
            student_DOB_entry.delete(0, END)
            student_Family_name_entry.delete(0, END)
            student_full_name_entry.delete(0, END)
            student_F_name_entry.delete(0, END)
            student_L_name_entry.delete(0, END)
            student_address_entry.delete(0, END)
            student_address_line_entry.delete(0, END)
            student_city_entry.delete(0, END)
            student_religion_entry.delete(0, END)
            student_gender_entry.delete(0, END)
            student_nic_entry.delete(0, END)
            parent_F_name_entry.delete(0, END)
            parent_parentship.delete(0, END)
            parent_address_entry.delete(0, END)
            parent_profession_entry.delete(0, END)
            parent_religion_entry.delete(0, END)
            parent_pone_entry.delete(0, END)
            parent_nic_entry.delete(0, END)

    search_box = Entry(edit_frame, font=fonts, foreground="#1b2d52", bd=0)
    search_box.place(x=286, y=150, width=227, height=28)
    search_box.bind("<KeyRelease>", lambda event: collect(search_box.get()))

    def show():
        if list.winfo_ismapped():
            list.place_forget()
        else:
            list.place(x=286, y=180)

    drop_btn = Button(edit_frame, text="⇅", bg="white", font=("Candara", 20, "bold"), bd=0, command=show)
    drop_btn.place(x=513, y=150, width=28, height=28)

    list = Listbox(edit_frame, height=10, width=43, bd=0)
    list.bind("<Double-Button-1>", lambda event: select())

    # noinspection PyBroadException
    def update():
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

        query = "select id from student where id=%s"
        parameters = [search_box.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()

        if result is not None:
            query = "update student set " \
                    "dob=%s,full_name=%s,family_name=%s,first_name=%s," \
                    "last_name=%s,address=%s,address_line=%s,city=%s," \
                    "religion=%s,gender=%s,nic=%s where id=%s"
            parameters = [student_DOB_entry.get(), student_full_name_entry.get(), student_Family_name_entry.get(),
                          student_F_name_entry.get(), student_L_name_entry.get(), student_address_entry.get(),
                          student_address_line_entry.get(), student_city_entry.get(), student_religion_entry.get(),
                          student_gender_entry.get(), student_nic_entry.get(), search_box.get()]
            mycursor.execute(query, parameters)
            con.commit()

            query = "update parents set " \
                    "name=%s,relation=%s,address=%s," \
                    "pro=%s,religion=%s,pone=%s,nic=%s where id=%s"
            parameters = [
                parent_F_name_entry.get(),
                parent_parentship.get(),
                parent_address_entry.get(),
                parent_profession_entry.get(),
                parent_religion_entry.get(),
                parent_pone_entry.get(),
                parent_nic_entry.get(),
                search_box.get()
            ]
            mycursor.execute(query, parameters)
            con.commit()
            con.close()
            messagebox.showinfo("SUCCESS", "Update Successful")
        else:
            messagebox.showerror("Error", "Wrong Index Number")

    fontl = ("Candara", 14, "bold")

    btn_student_update = Button(edit_frame, text="UPDATE", bg="#3b3086", fg="white", font=fontl,
                                command=update)
    btn_student_update.place(x=284, y=593, width=172, height=34)

    def load():
        edit_frame.destroy()
        Search(frame)

    search_student = Button(edit_frame, text="SEARCH", bg="#3b3086", fg="white", font=fontl, command=load)
    search_student.place(x=11, y=334, width=194, height=34)


def Search(frame):
    search_frame = Frame(frame, height=651, width=1185)
    search_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.search/Student Search.png")
    Background = Label(search_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Calibri", 12)

    try:
        background = "#e9edfa"

        dob_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        dob_label.place(x=577, y=152, width=243, height=23)

        name_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        name_label.place(x=857, y=152, width=243, height=23)

        fam_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        fam_label.place(x=297, y=208, width=243, height=23)

        fn_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        fn_label.place(x=577, y=208, width=243, height=23)

        ln_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        ln_label.place(x=857, y=208, width=243, height=23)

        ad_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        ad_label.place(x=297, y=267, width=243, height=23)

        adl_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        adl_label.place(x=577, y=267, width=243, height=23)

        city_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        city_label.place(x=857, y=267, width=243, height=23)

        rel_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        rel_label.place(x=297, y=324, width=243, height=23)

        gen_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        gen_label.place(x=577, y=324, width=243, height=23)

        nic_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        nic_label.place(x=857, y=324, width=243, height=23)
    except:
        pass

    try:
        background = "white"
        pfn_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        pfn_label.place(x=298, y=419, width=522, height=23)

        ps_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        ps_label.place(x=857, y=419, width=243, height=23)

        pad_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        pad_label.place(x=297, y=477, width=522, height=23)

        pcity_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        pcity_label.place(x=857, y=477, width=243, height=23)

        prel_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        prel_label.place(x=297, y=534, width=243, height=23)

        ppn_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        ppn_label.place(x=577, y=534, width=243, height=23)

        pnic_label = Label(search_frame, text="none", background=background, font=fonts, fg="#1b2d52")
        pnic_label.place(x=857, y=534, width=243, height=23)
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
            query = "CREATE TABLE student (id VARCHAR PRIMARY KEY,dob DATE," \
                    "full_name varchar(200),family_name VARCHAR(100),first_name VARCHAR(100),last_name VARCHAR(100)," \
                    "address VARCHAR(100), address_line VARCHAR(100), city VARCHAR(50)," \
                    "religion VARCHAR(50), gender VARCHAR(50), nic VARCHAR(50), enroll_date varchar(20)," \
                    "und varchar(5))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "SELECT id, full_name FROM student WHERE full_name LIKE '%" + text + "%' " \
                                                                                     "OR id LIKE '%" + text + "%' ORDER BY id ASC"
        mycursor.execute(query)
        result = mycursor.fetchall()

        list.place(x=286, y=180)

        list.delete(0, END)
        for row in result:
            idd = str(row[0])
            list.insert(END, idd + " , " + row[1])

    def select():
        selected_suggestion = list.get(list.curselection()[0])
        selected_suggestion = selected_suggestion.split()
        Key = selected_suggestion[0]

        search_box.delete(0, END)
        search_box.insert(0, Key)

        list.place_forget()
        find()

    def find():
        # noinspection PyBroadException
        try:
            # noinspection PyBroadException
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

            query = "select * from student inner join parents on student.id = parents.id where student.id=%s"
            parameters = [search_box.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()
            # print(result)

            dob_label.config(text=result[1])
            fam_label.config(text=result[3])
            name_label.config(text=result[2])
            fn_label.config(text=result[4])
            ln_label.config(text=result[5])
            ad_label.config(text=result[6])
            adl_label.config(text=result[7])
            city_label.config(text=result[8])
            rel_label.config(text=result[9])
            gen_label.config(text=result[10])
            nic_label.config(text=result[11])
            pfn_label.config(text=result[15])
            ps_label.config(text=result[16])
            pad_label.config(text=result[17])
            pcity_label.config(text=result[18])
            prel_label.config(text=result[19])
            ppn_label.config(text=result[20])
            pnic_label.config(text=result[21])
            con.close()
        except:
            name_label.config(text="none")
            dob_label.config(text="none")
            fam_label.config(text="none")
            fn_label.config(text="none")
            ln_label.config(text="none")
            ad_label.config(text="none")
            adl_label.config(text="none")
            city_label.config(text="none")
            rel_label.config(text="none")
            gen_label.config(text="none")
            nic_label.config(text="none")
            pfn_label.config(text="none")
            ps_label.config(text="none")
            pad_label.config(text="none")
            pcity_label.config(text="none")
            prel_label.config(text="none")
            ppn_label.config(text="none")
            pnic_label.config(text="none")

    search_box = Entry(search_frame, font=fonts, foreground="#1b2d52", bd=0)
    search_box.place(x=286, y=150, width=227, height=28)
    search_box.bind("<KeyRelease>", lambda event: collect(search_box.get()))

    def show():
        if list.winfo_ismapped():
            list.place_forget()
        else:
            list.place(x=286, y=180)

    drop_btn = Button(search_frame, text="⇅", bg="white", font=("Candara", 20, "bold"), bd=0, command=show)
    drop_btn.place(x=513, y=150, width=28, height=28)

    list = Listbox(search_frame, height=10, width=43, bd=0)
    list.bind("<Double-Button-1>", lambda event: select())

    def load():
        search_frame.destroy()
        Enrollment(frame)

    fontl = ("Candara", 14, "bold")

    search_student = Button(search_frame, text="ENROLLMENT", bg="#3b3086", fg="white", font=fontl, command=load)
    search_student.place(x=22, y=295, width=172, height=34)


def Note():
    note = Toplevel()
    note.title("Student Note")
    note.grab_set()

    screen_height = note.winfo_screenheight()
    window_width = 954
    window_height = 508
    x = 200
    y = (screen_height - window_height) // 2 - 20
    note.geometry(f"{window_width}x{window_height}+{x}+{y}")

    note.iconbitmap("pad.ico")
    note.resizable(False, False)

    frame = Frame(note)
    frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.note/Student Note.png")
    Background = Label(frame, image=back)
    Background.image = back
    Background.pack()

    # noinspection PyBroadException
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
            messagebox.showerror("ERROR", "Database Failed")
            return

        query = "SELECT id, full_name FROM student WHERE full_name LIKE '%" + text + "%' " \
                                                                                     "OR id LIKE '%" + text + "%' ORDER BY id ASC"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        dropdown.place(x=132, y=131)
        dropdown.delete(0, END)
        for row in result:
            idd = str(row[0])
            dropdown.insert(tk.END, idd + " , " + row[1])

    def select_item():
        dropdown.place_forget()
        select_sug = dropdown.get(dropdown.curselection()[0])
        print(select_sug)
        select_sug = select_sug.split()
        select_sug_id = select_sug[0]

        note_index.delete(0, END)
        note_index.insert(0, select_sug_id)

        find()

    fonts = ("Candara", 15)
    note_index = Entry(frame, fg="#1b2d52", font=fonts, bd=0)
    note_index.place(x=133, y=93, width=148, height=34)
    note_index.bind("<KeyRelease>", lambda event: collect(note_index.get()))

    note_date = DateEntry(frame, selectmode="day", date_pattern="yyyy/mm/dd")
    note_date.place(x=408, y=93, width=201, height=34)

    options_g6 = ["6A", "6B", "6C", "6D", "6E", "6F"]
    options_g7 = ["7A", "7B", "7C", "7D", "7E", "7F"]
    options_g8 = ["8A", "6B", "8C", "8D", "8E", "8F"]
    options_g9 = ["9A", "9B", "9C", "9D", "9E", "9F"]
    options = options_g6 + options_g7 + options_g8 + options_g9
    note_class_combo = ttk.Combobox(frame, values=options, font=fonts)
    note_class_combo.place(width=72, height=34, x=704, y=93)
    note_class_combo.set(options[0])

    note_note = Entry(frame, bg="#e9edfa", fg="#1b2d52", font=fonts, bd=0)
    note_note.place(x=364, y=149, width=557, height=34)

    def show():
        if dropdown.winfo_ismapped():
            dropdown.place_forget()
        else:
            dropdown.place(x=132, y=129)

    # fonts = ("Candara", 20, "bold")
    slide_button = Button(frame, text="⇅", fg="#3b3086", font=("Candara", 20, "bold"), bg="white", bd=0
                          , command=show)
    slide_button.place(x=281, y=93, width=34, height=34)

    # noinspection PyBroadException
    def add():
        if note_index.get() == "" or note_date.get() == "" or note_class_combo.get() == "" or note_note.get() == "":
            messagebox.showerror("ERROR", "All Fields Required")
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
                messagebox.showerror("ERROR", "Database Failed")
                return

            try:
                query = "create table note(Id varchar(100), Name varchar(200),Date varchar(20),Class varchar(10)," \
                        "Note varchar(" \
                        "500))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            try:
                query = "select first_name, last_name from student where Id=%s"
                parameters = [note_index.get()]
                mycursor.execute(query, parameters)
                res = mycursor.fetchone()
                Name = res[0] + " " + res[1]

                query = "insert into note (Id,Name,Date,Class,Note) values (%s,%s,%s,%s,%s)"
                parameters = [note_index.get(), Name, note_date.get(), note_class_combo.get(), note_note.get()]
                mycursor.execute(query, parameters)
                con.commit()
                con.close()
                # messagebox.showinfo("Success", "Note Added Successfully")
            except:
                messagebox.showerror("Unknown Error", "Data add proceed failed")

            find()

    # noinspection PyBroadException
    def find():
        for item in view.get_children():
            view.delete(item)

        if note_index.get() == "":
            messagebox.showerror("ERROR", "index Number Required")
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
                messagebox.showerror("ERROR", "Database Failed")
                return

            try:
                query = "create table note(Id int, Name varchar(50),Date varchar(20),Class varchar(10),Note varchar(" \
                        "500))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select * from note where Id = %s"
            parameters = [note_index.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()
            con.close()

            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=1, iid=counter, text="", values=(
                    row[1],
                    row[2],
                    row[3],
                    row[4]))

    add_button = Button(frame, text="➕", fg="white", font=("Candara", 15, "bold"), bg="#3b3086", bd=0
                        , command=add)
    add_button.place(x=791, y=93, width=34, height=34)

    fonts = ("Candara", 15, "bold")
    search_button = Button(frame, text="FIND", fg="white", font=fonts, bg="#ce4912", bd=0, command=find)
    search_button.place(x=835, y=93, width=77, height=34)

    view = ttk.Treeview(note)
    view.place(x=30, y=195, width=876, height=294)

    scroll = ttk.Scrollbar(frame, orient=VERTICAL, command=view.yview())
    scroll.place(x=906, y=195, height=294)
    view.configure(yscrollcommand=scroll.set)

    view["columns"] = ("Name", "Date", "Class", "Note")

    view["show"] = "headings"
    view.column("Name", minwidth=40, width=120)
    view.column("Date", minwidth=60, width=60)
    view.column("Class", minwidth=10, width=20)
    view.column("Note", minwidth=100, width=500)

    view.heading("Name", text="Name")
    view.heading("Date", text="Date")
    view.heading("Class", text="Class")
    view.heading("Note", text="Note or Description")

    dropdown = tk.Listbox(note, width=30, height=10, bd=0, bg="#e9edfa")
    dropdown.bind("<Double-Button-1>", lambda event: select_item())

    # note.mainloop()


def st_Delete():
    Delete = Toplevel()
    Delete.grab_set()

    screen_width = Delete.winfo_screenwidth()
    screen_height = Delete.winfo_screenheight()
    window_width = 500
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    Delete.geometry(f"{window_width}x{window_height}+{x}+{y}")

    Delete.iconbitmap("pad.ico")
    Delete.resizable(False, False)
    Delete.title("Set Admin Info")

    back = PhotoImage(file=current+"/.ux/padma/.student/.delete/Delete Student.png")
    back_p = Label(Delete, image=back)
    back_p.image = back
    back_p.pack()

    fonts = ("Candara", 17, "bold")

    del_index = Entry(Delete, fg="#1b2d52", font=fonts, foreground="red")
    del_index.place(width=291, height=34, x=168, y=106)

    # noinspection PyBroadException
    def Delete_student():
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

        query = "select * from student where id=%s"
        parameters = [del_index.get()]
        mycursor.execute(query, parameters)
        result = mycursor.fetchone()
        print(result)

        if result is not None:
            response = messagebox.askyesno("CONFIRM", "Are You Sure ?")
            if response:
                try:
                    query = "delete from student where student.id = %s"
                    parameters = [del_index.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Student Removed from System")
                    del_index.delete(0, END)
                except:
                    messagebox.showerror("Error", "Process Unsuccessful")
            else:
                pass
        else:
            messagebox.showerror("Error", "Invalid Student Index")

    fonts = ("Candara", 15, "bold")
    delete_btn = Button(Delete, bg="red", fg="white", text="REMOVE", font=fonts, command=Delete_student)
    delete_btn.place(x=168, y=248, width=140, height=34)

    def end():
        Delete.destroy()

    Back = Button(Delete, bg="#3b3086", fg="white", text="Close", font=fonts, command=end)
    Back.place(x=319, y=248, width=140, height=34)

    Delete.mainloop()


def Acadamic(frame):
    acadamic_frame = Frame(frame, height=651, width=1185)
    acadamic_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.acadamic/St Rep.png")
    Background = Label(acadamic_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Calibri", 12)

    option = ["Regular"]
    Mode = ttk.Combobox(acadamic_frame, font=fonts, values=option, state="readonly")
    Mode.place(x=1041, y=47, width=118, height=26)
    Mode.set(option[0])

    # OPTION BAR
    try:
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
                query = "CREATE TABLE student (id INTEGER PRIMARY KEY,dob DATE," \
                        "full_name varchar(100),family_name VARCHAR(50),first_name VARCHAR(50),last_name VARCHAR(50)," \
                        "address VARCHAR(50), address_line VARCHAR(50), city VARCHAR(20)," \
                        "religion VARCHAR(50), gender VARCHAR(50), nic VARCHAR(25), enroll_date varchar(20)," \
                        "und varchar(5))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "SELECT id, full_name FROM student WHERE full_name LIKE '%" + text + "%' " \
                                                                                     "OR id LIKE '%" + text + "%' ORDER BY id ASC"
            mycursor.execute(query)
            result = mycursor.fetchall()

            list.place(x=24, y=172)

            list.delete(0, END)
            for row in result:
                idd = str(row[0])
                list.insert(END, idd + " , " + row[1])

        def select():
            selected_suggestion = list.get(list.curselection()[0])
            selected_suggestion = selected_suggestion.split()
            Key = selected_suggestion[0]

            search_box.delete(0, END)
            search_box.insert(0, Key)

            list.place_forget()

            find()

        def find():
            # noinspection PyBroadException
            try:
                # noinspection PyBroadException
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

                query = "select * from student inner join parents on student.id = parents.id where student.id=%s"
                parameters = [search_box.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()
                # print(result)

                Dob.config(text=result[1])
                Name.config(text=result[2])
                Address.config(text=result[6]+", "+result[7])
                Gender.config(text=result[10])
                Contact.config(text=result[20])
                con.close()
            except:
                Dob.config(text="none")
                Name.config(text="none")
                Address.config(text="none")
                Gender.config(text="none")
                Contact.config(text="none")

        search_box = Entry(acadamic_frame, font=fonts, foreground="#1b2d52", bd=0, bg="#e9edfa")
        search_box.place(x=24, y=145, width=177, height=26)
        search_box.bind("<KeyRelease>", lambda event: collect(search_box.get()))

        def show():
            if list.winfo_ismapped():
                list.place_forget()
            else:
                list.place(x=24, y=172)

        drop_btn = Button(acadamic_frame, text="⇅", bg="#e9edfa", font=("Candara", 20, "bold"), bd=0, command=show)
        drop_btn.place(x=201, y=145, width=26, height=26)

        option = ["A/L", "O/L"]
        Exam = ttk.Combobox(acadamic_frame, font=fonts, values=option, state="readonly")
        Exam.place(x=46, y=222, width=121, height=26)
        Exam.set(option[0])

        p_index = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        p_index.place(x=195, y=222, width=137, height=26)
        p_index.insert(0, "         Disabled")
        p_index.config(state="disabled")

        batch = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        batch.place(x=360, y=222, width=137, height=26)

        admission = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        admission.place(x=212, y=263, width=231, height=26)

        a = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        a.place(x=109, y=304, width=26, height=26)

        b = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        b.place(x=145, y=304, width=26, height=26)

        c = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        c.place(x=181, y=304, width=26, height=26)

        s = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        s.place(x=217, y=304, width=26, height=26)

        w = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        w.place(x=253, y=304, width=26, height=26)

        list = Listbox(acadamic_frame, height=10, width=34, bd=0)
        list.bind("<Double-Button-1>", lambda event: select())
    except:
        pass

    # LABELS
    try:
        Name = Label(acadamic_frame, bg="#e9edfa", font=fonts, text=" Student Name", anchor=W)
        Name.place(x=222, y=398, width=320, height=30)

        Dob = Label(acadamic_frame, bg="#e9edfa", font=fonts, text=" Student Dob", anchor=W)
        Dob.place(x=222, y=439, width=320, height=30)

        Gender = Label(acadamic_frame, bg="#e9edfa", font=fonts, text=" Student Gender", anchor=W)
        Gender.place(x=222, y=480, width=320, height=30)

        Address = Label(acadamic_frame, bg="#e9edfa", font=fonts, text=" Student Address", anchor=W)
        Address.place(x=222, y=524, width=320, height=30)

        Contact = Label(acadamic_frame, bg="#e9edfa", font=fonts, text=" Student Contact", anchor=W)
        Contact.place(x=222, y=565, width=320, height=30)
    except:
        pass

    # SEARCH PARA
    try:
        s_index = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        s_index.place(x=595, y=145, width=130, height=26)
        s_index.bind("<KeyRelease>", lambda event: filter_data())

        option = ["A/L", "O/L", "All"]
        s_Exam = ttk.Combobox(acadamic_frame, font=fonts, values=option, state="readonly")
        s_Exam.place(x=750, y=145, width=130, height=26)
        s_Exam.set(option[2])
        s_Exam.bind("<<ComboboxSelected>>", lambda event: filter_data())

        s_batch = Entry(acadamic_frame, bg="#e9edfa", border=1, font=fonts)
        s_batch.place(x=905, y=145, width=130, height=26)
        s_batch.bind("<KeyRelease>", lambda event: filter_data())
    except:
        pass

    # VIEW
    try:
        view = ttk.Treeview(acadamic_frame)
        view.place(x=595, y=191, width=569, height=438)

        view["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        view["show"] = "headings"

        view.column("1", width=30, minwidth=25)
        view.column("2", width=20, minwidth=10)
        view.column("3", width=20, minwidth=15)
        view.column("4", width=70, minwidth=30)
        view.column("5", width=20, minwidth=10)
        view.column("6", width=20, minwidth=10)
        view.column("7", width=20, minwidth=10)
        view.column("8", width=20, minwidth=10)
        view.column("9", width=20, minwidth=10)

        view.heading("1", text="Index")
        view.heading("2", text="Exam")
        view.heading("3", text="Batch")
        view.heading("4", text="Admission")
        view.heading("5", text="A")
        view.heading("6", text="B")
        view.heading("7", text="C")
        view.heading("8", text="S")
        view.heading("9", text="W")
    except:
        pass

    fontl = ("Candara", 14, "bold")

    def filter_data():
        for item in view.get_children():
            view.delete(item)

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
            mycursor = con.cursor(buffered=True)

        except:
            messagebox.showerror("ERROR", "Database Failed")
            return

        index_pattern = s_index.get()
        s_exam_value = s_Exam.get()
        batch_pattern = s_batch.get()

        if s_exam_value == "All":
            exam_pattern = ""
        else:
            exam_pattern = "%" + s_exam_value + "%"

        filters = []

        if index_pattern:
            filters.append("id LIKE '%" + index_pattern + "%'")

        if exam_pattern:
            filters.append("exam LIKE '%" + exam_pattern + "%'")

        if batch_pattern and batch_pattern != "All":
            filters.append("batch LIKE '%" + batch_pattern + "%'")

        if filters:
            query = "SELECT * FROM acadamic WHERE " + " AND ".join(filters)
        else:
            query = "SELECT * FROM acadamic"

        mycursor.execute(query)
        result = mycursor.fetchall()

        if result:
            counter = 0
            for row in result:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[0], row[1], row[2], row[3], row[4],
                                                                              row[5], row[6], row[7], row[8]))

        con.close()

    def fetch():
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
            messagebox.showerror("ERROR", "Database Failed")
            return

        try:
            query = "create table acadamic(id varchar(100), exam varchar(4), batch varchar(5), admission varchar(50)," \
                    "a int(10), b int(10), c int(10), s int(10), w int(10))"
            mycursor.execute(query)
            con.commit()
        except:
            pass

        query = "select * from acadamic"
        mycursor.execute(query)
        res = mycursor.fetchall()

        if res is not None:
            counter = 0
            for row in res:
                counter += 1
                view.insert(parent="", index=0, iid=counter, text="", values=(row[0], row[1], row[2], row[3], row[4],
                                                                              row[5], row[6], row[7], row[8]))
        con.close()

    fetch()

    def add():
        if search_box.get() == "" or Exam.get() == "" or batch.get() == "" or admission.get() == "":
            messagebox.showerror("Error", "Index, Exam, Batch, Admission to Be Full-Filled")
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
            except:
                messagebox.showerror("ERROR", "Database Failed")
                return

            try:
                query = "create table acadamic(id varchar(100), exam varchar(4), batch varchar(5), admission varchar(" \
                        "50)," \
                        "a int(10), b int(10), c int(10), s int(10), w int(10))"
                mycursor.execute(query)
                con.commit()
            except:
                pass

            query = "select id from student where id=%s"
            parameters = [search_box.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                query = "select * from acadamic where id=%s and exam=%s"
                parameters = [search_box.get(), Exam.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()

                if result is not None:
                    response = messagebox.askyesno("Confirm", "Data Already Available, Do you still want to update ?")
                    if response:
                        query = "update acadamic set batch=%s, admission=%s, a=%s, b=%s, c=%s, s=%s, w=%s where id=%s "\
                                "and " \
                                "exam=%s"
                        parameters = [batch.get(), admission.get(), a.get(), b.get(), c.get(), s.get(), w.get(),
                                      search_box.get(), Exam.get()]
                        mycursor.execute(query, parameters)
                        con.commit()
                    else:
                        pass
                else:
                    query = "insert into acadamic values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    parameters = [search_box.get(), Exam.get(), batch.get(), admission.get(), a.get(), b.get(), c.get(),
                                  s.get(), w.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
            else:
                messagebox.showerror("error", "Invalid Index or Unknown Student")
            con.close()
        fetch()

    add = Button(acadamic_frame, text="ADD/UPDATE", bg="#3b3086", fg="white", font=fontl, border=0, command=add)
    add.place(x=248, y=145, width=153, height=30)

    g = Button(acadamic_frame, text="SEARCH", bg="#3b3086", fg="white", font=fontl, state="disabled", border=0)
    g.place(x=421, y=145, width=153, height=30)


def Report(frame):
    report_frame = Frame(frame, height=651, width=1185)
    report_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.student/.report/Student Report.png")
    Background = Label(report_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    fonts = ("Calibri", 12)

    index = Entry(report_frame, font=fonts, fg="#1b2d52", background="#d2daf4")
    index.place(x=55, y=189, width=203, height=26)

    try:
        background = "#d2daf4"

        name_label = Label(report_frame, text="Student Name", background=background, font=fonts, fg="#1b2d52")
        name_label.place(x=55, y=251, width=377, height=26)

        pfn_label = Label(report_frame, text="Holder Name", background=background, font=fonts, fg="#1b2d52")
        pfn_label.place(x=55, y=316, width=377, height=26)

        gen_label = Label(report_frame, text="Male/Female", background=background, font=fonts, fg="#1b2d52")
        gen_label.place(x=461, y=189, width=203, height=26)

        ppn_label = Label(report_frame, text="Contact Number", background=background, font=fonts, fg="#1b2d52")
        ppn_label.place(x=461, y=251, width=203, height=26)

        ps_label = Label(report_frame, text="Relationship", background=background, font=fonts, fg="#1b2d52")
        ps_label.place(x=461, y=316, width=203, height=26)
    except:
        pass

    fontl = ("Candara", 14, "bold")

    def find():
        if index.get() == "":
            messagebox.showerror("Error", "Index Number Required !")
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

            query = "select * from student where id = %s"
            para = [index.get()]
            mycursor.execute(query, para)
            res = mycursor.fetchone()

            if res is not None:
                query = """
                        select student.full_name,parents.name,student.gender,parents.pone,parents.relation 
                        from student inner join parents on student.id = parents.id
                        where student.id=%s
                        """
                parameters = [index.get()]
                mycursor.execute(query, parameters)
                result = mycursor.fetchone()

                if result is not None:
                    name_label.config(text=None)
                    pfn_label.config(text=None)
                    gen_label.config(text=None)
                    ppn_label.config(text=None)
                    ps_label.config(text=None)

                    name_label.config(text=result[0])
                    pfn_label.config(text=result[1])
                    gen_label.config(text=result[2])
                    ppn_label.config(text=result[3])
                    ps_label.config(text=result[4])
            else:
                messagebox.showerror("error", "Invalid Index Number or Unknown Student")
            con.close()

    check = Button(report_frame, text="CHECK", bg="green", fg="white", font=fontl, command=find)
    check.place(x=290, y=189, width=142, height=30)

    def summery():
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

        query = "select * from student where id = %s"
        para = [index.get()]
        mycursor.execute(query, para)
        res = mycursor.fetchone()

        if res is not None:
            image_path = current+"/.ux/padma/.student/.addon/Sheet.png"
            image = image_path
            inverse = 832
            save_location = filedialog.asksaveasfilename(
                title="Select a file",
                filetypes=[("PDF", "*.pdf"), ("JPEG", "*.jpg"), ("PNG", "*.png")],
                defaultextension=".pdf"
            )

            c = canvas.Canvas(save_location, pagesize=A4)
            c.drawImage(image, 0, 0)

            query = """
                    select student.id,student.full_name,student.dob,student.address,student.address_line,student.gender
                    ,parents.name,parents.pone 
                    from student inner join parents on student.id = parents.id
                    where student.id=%s
                    """
            parameters = [index.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()
            # print(result)

            value = []
            if result is not None:
                for row in result:
                    value.append(row)
                c.drawString(151, inverse - 188, str(value[0]))
                c.drawString(151, inverse - 210, str(value[1]))
                c.drawString(151, inverse - 231, str(value[2]))
                c.drawString(151, inverse - 253, str(value[3] + ", " + value[4]))
                c.drawString(151, inverse - 274, str(value[5]))
                c.drawString(151, inverse - 296, str(value[6]))
                c.drawString(151, inverse - 317, str(value[7]))
                c.save()
            else:
                messagebox.showerror("Error", "Student Details Error")
        else:
            messagebox.showerror("Error", "invalid Index or Unknown Student. please press the check button first !")
        con.close()

    Summery = Button(report_frame, text="GENERATE", bg="#3b3086", fg="white", font=fontl, command=summery)
    Summery.place(x=300, y=481, width=116, height=39)

    def student_report_exam():
        if index.get() == "":
            messagebox.showerror("Error", "Enter Index click The Check Button First !")
        else:
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
                mycursor = conn.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select * from exam where id=%s"
            parameters = [index.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                query = """
                    SELECT student.full_name, exam.class, exam.term, 

                    mark_uo.sinhala,mark_uo.maths,mark_uo.science,mark_uo.english,mark_uo.religion,mark_uo.history,
                    mark_uo.geograpy,mark_uo.ce,mark_uo.health,mark_uo.art,mark_uo.dance,mark_uo.music,
                    mark_uo.drama,mark_uo.tamil,mark_uo.pts,mark_uo.ict

                    FROM exam
                    INNER JOIN mark_uo ON exam.exam_id = mark_uo.exam_id
                    INNER JOIN student ON exam.id = student.id
                    WHERE student.id = %s;
                        """
                parameters = [index.get()]
                mycursor.execute(query, parameters)
                results = mycursor.fetchall()
                conn.close()

                pdf = FPDF(orientation='L', unit='mm')
                pdf.set_auto_page_break(auto=False, margin=0)
                pdf.set_font("Arial", size=30, style='B')
                pdf.add_page()

                title_x = 20
                title_y = 10
                pdf.set_xy(title_x, title_y)
                pdf.cell(0, 10, "Padmavathie N.C - " + index.get() + " - All Classes - Mark Sheet", ln=True, align='L')

                subtitle_x = 50
                subtitle_y = title_y + 15
                pdf.set_xy(subtitle_x, subtitle_y)
                pdf.set_font("Arial", size=0, style='I')
                pdf.cell(0, 10, "", ln=True, align='L')

                # Set font and font size for table content
                pdf.set_font("Arial", size=10)
                # Calculate column widths
                header = [i[0] for i in mycursor.description]  # Get column names from mycursor
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
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

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

                mycursor.close()
                conn.close()
            else:
                messagebox.showerror("Error", "Invalid Student Id Or No Data Found")

    exams = Button(report_frame, text="GENERATE", bg="#3b3086", fg="white", font=fontl, command=student_report_exam)
    exams.place(x=593, y=481, width=116, height=39)

    def student_report_note():
        if index.get() == "":
            messagebox.showerror("Error", "Enter Index click The Check Button First !")
        else:
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
                mycursor = conn.cursor(buffered=True)
                # print("connection ok !")
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select * from note where Id=%s"
            parameters = [index.get()]
            mycursor.execute(query, parameters)
            result = mycursor.fetchone()

            if result is not None:
                query = """
                    SELECT name,date ,class,note from note where Id = %s
                        """
                parameters = [index.get()]
                mycursor.execute(query, parameters)
                results = mycursor.fetchall()
                conn.close()

                pdf = FPDF(orientation='L', unit='mm')
                pdf.set_auto_page_break(auto=False, margin=0)
                pdf.set_font("Arial", size=30, style='B')
                pdf.add_page()

                title_x = 20
                title_y = 10
                pdf.set_xy(title_x, title_y)
                pdf.cell(0, 10, "Padmavathie N.C - " + index.get() + " - Student Notes", ln=True, align='L')

                subtitle_x = 50
                subtitle_y = title_y + 15
                pdf.set_xy(subtitle_x, subtitle_y)
                pdf.set_font("Arial", size=0, style='I')
                pdf.cell(0, 10, "", ln=True, align='L')

                # Set font and font size for table content
                pdf.set_font("Arial", size=10)
                # Calculate column widths
                header = [i[0] for i in mycursor.description]  # Get column names from mycursor
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
                    pdf.cell(width + 2 * margin, 10, str(header_name), border=1, ln=False,
                             align='C')  # Adjusted cell width

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

                mycursor.close()
                conn.close()
            else:
                messagebox.showerror("Error", "Invalid Student Id Or No Data Found")

    note_sheet = Button(report_frame, text="GENERATE", bg="#3b3086", fg="white", font=fontl
                        , command=student_report_note)
    note_sheet.place(x=884, y=481, width=116, height=39)


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
            df = pd.read_excel(excel_file, skiprows=0)

            # MySQL database connection details
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)
            mysql_database = "pcc"
            mysql_table = "student"

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
                    info.insert(END, f"ID {row[0]} already exists. Student Skipping...")

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

    def transfer_excel_to_mysql_parent():
        info_bar["value"] = 0
        info.delete(0, END)
        # Open file dialog to select the Excel file
        Tk().withdraw()
        excel_file = askopenfilename(title="Select Excel file", filetypes=[("Excel Files", "*.xlsx")])

        if excel_file != "":
            info_bar["value"] = 25
            info.insert(END, "Reading The Excel And Validating.....")
            # Read Excel data into a pandas DataFrame, skipping the first row
            df = pd.read_excel(excel_file, skiprows=0)

            # MySQL database connection details
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)
            mysql_database = "pcc"
            mysql_table = "parents"

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
                    info.insert(END, f"ID {row[0]} already exists. parents Skipping...")

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

    student = Button(BUlk_win, text="Student", bg="#ce4912", fg="white", font=fontl,
                     command=transfer_excel_to_mysql_student)
    student.place(x=48, y=225, width=194, height=34)

    parent = Button(BUlk_win, text="Parent", bg="#3b3086", fg="white", font=fontl,
                    command=transfer_excel_to_mysql_parent)
    parent.place(x=257, y=225, width=194, height=34)

    info = Listbox(BUlk_win)
    info.place(x=48, y=284, height=161, width=387)

    scrollbar = tk.Scrollbar(BUlk_win)
    scrollbar.place(x=435, y=284, height=161)
    info.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=info.yview)

    info_bar = ttk.Progressbar(BUlk_win, orient=HORIZONTAL, length=404, mode="determinate")
    info_bar.place(x=48, y=468, height=34)
    info_bar["value"] = 0
