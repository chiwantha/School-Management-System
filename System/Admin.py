from tkinter import *
from tkinter import ttk
import winreg
import psutil
from tkinter import messagebox
import mysql.connector
import Teachers
from datetime import datetime
import os

Year = datetime.now().year

admin_nic = ""
admin_name = ""
admin_rank = ""

current = os.path.dirname(os.path.realpath(__file__))


def adash(frame):
    dash_frame = Frame(frame, height=651, width=1185)
    dash_frame.pack()

    back = PhotoImage(file=current+"/.ux/padma/.admin/.account/Teacher Dash.png")
    Background = Label(dash_frame, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    try:
        fonts = ("Calibri", 12)

        def FI():
            txt_box.select_range(0, END)

        def FO():
            if txt_box.get() == "":
                txt_box.insert(0, " type your toDO here...")

        txt_box = Entry(dash_frame, bg="white", font=fonts, foreground="#3b3086")
        txt_box.place(x=893, y=132, width=237, height=32)
        txt_box.insert(0, " type your toDO here...")
        txt_box.bind("<FocusIn>", lambda event: FI())
        txt_box.bind("<FocusOut>", lambda event: FO())

        def add_toDO():
            if txt_box.get() == "":
                messagebox.showerror("ERROR", "Please type toDO.")
            else:
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                    host = winreg.QueryValueEx(key, "Host")[0]
                    user = winreg.QueryValueEx(key, "User")[0]
                    password = winreg.QueryValueEx(key, "Pass")[0]
                    winreg.CloseKey(key)

                    con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
                    mycursor = con.cursor()
                except:
                    messagebox.showerror("Error", "DataBase Failed")
                    return

                try:
                    query = "Create Table todo(id int,note varchar(100))"
                    mycursor.execute(query)
                    con.commit()
                except:
                    pass

                try:
                    query = "insert into todo values (%s,%s)"
                    parameters = [admin_nic, txt_box.get()]
                    mycursor.execute(query, parameters)
                    con.commit()
                    con.close()
                except:
                    messagebox.showerror("ERROR", "Unknown Error")
                    con.close()

                get_todo()

        note_add = Button(dash_frame, text="ADD toDO", bg="#ce4912", fg="white", font=fonts, command=add_toDO)
        note_add.place(x=893, y=172, width=113, height=23)

        def clear():
            txt_box.delete(0, END)
            FO()
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "delete from todo where id=%s"
            parameters = [admin_nic]
            mycursor.execute(query, parameters)
            con.commit()
            con.close()
            get_todo()

        note_delete = Button(dash_frame, text="Clear", bg="#ce4912", fg="white", font=fonts, command=clear)
        note_delete.place(x=1017, y=172, width=113, height=23)

        view = ttk.Treeview(dash_frame)
        view.place(x=893, y=206, width=237, height=387)

        view["columns"] = ("id", "toDo")
        view["show"] = "headings"

        view.column("id", minwidth=10, width=10, anchor=CENTER)
        view.column("toDo", minwidth=100, width=150)

        view.heading("id", text="id")
        view.heading("toDo", text="toDo List")

        def get_todo():
            for item in view.get_children():
                view.delete(item)
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
                host = winreg.QueryValueEx(key, "Host")[0]
                user = winreg.QueryValueEx(key, "User")[0]
                password = winreg.QueryValueEx(key, "Pass")[0]
                winreg.CloseKey(key)

                con = mysql.connector.connect(host=host, user=user, password=password, database="pcc")
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "DataBase Failed")
                return

            query = "select note from todo where id=%s"
            parameters = [admin_nic]
            mycursor.execute(query, parameters)
            result = mycursor.fetchall()
            con.close()

            if result is not None:
                counter = 0
                numbering = 0
                for row in result:
                    counter += 1
                    numbering += 1
                    view.insert(parent="", index=1, iid=counter, text="", values=(numbering, row[0]))
            else:
                value = "No Data"
                view.insert(parent="", index=1, iid=1, text="", values=value)

        get_todo()

    except:
        pass

    fonts = ("Candara", 14, "bold")
    admin_nic_label = Label(dash_frame, text=admin_nic, font=fonts, foreground="#ce4912")
    admin_nic_label.place(x=443, y=190, height=34, width=221)
    admin_name_label = Label(dash_frame, text=admin_name, font=fonts, foreground="#ce4912")
    admin_name_label.place(x=443, y=230, height=34, width=221)
    admin_rank_label = Label(dash_frame, text=admin_rank, font=fonts, foreground="#ce4912")
    admin_rank_label.place(x=443, y=271, height=34, width=221)

    fontl = ("Candara", 14, "bold")

    btn_forgot_password = Button(dash_frame
                                 , text="Forgot Password"
                                 , bg="#3b3086"
                                 , fg="white"
                                 , font=fontl
                                 , command=Teachers.reset)
    btn_forgot_password.place(x=23, y=229, width=172, height=34)

    btn_student_class = Button(dash_frame
                               , text="Set Admin Info"
                               , bg="#3b3086"
                               , fg="white"
                               , font=fontl
                               , command=Teachers.update_admin_info)
    btn_student_class.place(x=23, y=288, width=172, height=34)


def init():
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
        return

    try:
        query = "CREATE TABLE student (id int,dob VARCHAR(100)," \
                "full_name varchar(200),family_name VARCHAR(100),first_name VARCHAR(100),last_name VARCHAR(100)," \
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

    try:
        query = "create table sponsor(id int AUTO_INCREMENT PRIMARY KEY, name varchar(100)," \
                "item_id varchar(50), quantity varchar(10), telephone varchar(15),address varchar(100))"
        mycursor.execute(query)
        con.commit()
    except:
        pass

    try:
        query = "CREATE TABLE grader(nic VARCHAR(100), name varchar(200), group varchar(50), class varchar(" \
                "50), pass varchar(6))"
        mycursor.execute(query)
        con.commit()
    except:
        pass

    con.close()


def dashboard(frame):
    init()

    global Dash
    Dash = Frame(frame, height=651, width=1185)
    Dash.pack()

    back = PhotoImage(file=current+"/.ux/padma/.admin/.dash/Admin.png")
    Background = Label(Dash, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    # Count
    try:
        fonts = ("Impact", 30)
        fg = "white"

        student = Label(Dash, text="0000", font=fonts, bg="#9e005d", fg=fg)
        student.place(x=22, y=271, width=123, height=47)
        student.config(text=student_count())

        teacher = Label(Dash, text="0000", font=fonts, bg="#f26d7d", fg=fg)
        teacher.place(x=257, y=271, width=123, height=47)
        teacher.config(text=teacher_count())

        admin = Label(Dash, text="0000", font=fonts, bg="#0076a3", fg=fg)
        admin.place(x=495, y=271, width=123, height=47)
        admin.config(text=admin_count())

        inventory = Label(Dash, text="0000", font=fonts, bg="#00a651", fg=fg)
        inventory.place(x=730, y=271, width=123, height=47)
        inventory.config(text=inventory_sponsor_count())

        user = Label(Dash, text="0000", font=fonts, bg="#636363", fg=fg)
        user.place(x=964, y=271, width=123, height=47)
        user.config(text=grader_count())
    except:
        pass

    # student bars
    try:
        male = ttk.Progressbar(Dash, orient=HORIZONTAL, length=334, mode="determinate")
        male.place(x=124, y=455, height=23)
        try:
            male.config(value=student_count_male())
        except:
            pass

        female = ttk.Progressbar(Dash, orient=HORIZONTAL, length=334, mode="determinate")
        female.place(x=124, y=490, height=23)
        try:
            female.config(value=student_count_female())
        except:
            pass

        biddhism = ttk.Progressbar(Dash, orient=HORIZONTAL, length=334, mode="determinate")
        biddhism.place(x=124, y=524, height=23)
        try:
            biddhism.config(value=student_count_buddhism())
        except:
            pass

        chrisrstian = ttk.Progressbar(Dash, orient=HORIZONTAL, length=334, mode="determinate")
        chrisrstian.place(x=124, y=559, height=23)
        try:
            chrisrstian.config(value=student_count_Christian())
        except:
            pass

        muslim = ttk.Progressbar(Dash, orient=HORIZONTAL, length=334, mode="determinate")
        muslim.place(x=124, y=594, height=23)
        try:
            muslim.config(value=student_count_Muslim())
        except:
            pass
    except:
        pass

    # teacher bars
    try:
        tmale = ttk.Progressbar(Dash, orient=VERTICAL, mode="determinate")
        tmale.place(x=526, y=455, height=168, width=33)
        try:
            tmale.config(value=teacher_count_male())
        except:
            pass

        tfemale = ttk.Progressbar(Dash, orient=VERTICAL, mode="determinate")
        tfemale.place(x=585, y=455, height=168, width=33)
        try:
            tfemale.config(value=teacher_count_female())
        except:
            pass

        grader = ttk.Progressbar(Dash, orient=VERTICAL, mode="determinate")
        grader.place(x=645, y=455, height=168, width=33)
        try:
            grader.config(value=grader_count_percentage())
        except:
            pass
    except:
        pass

    # admin details
    try:
        total_teacher = Label(Dash, text="0000", bg="#0076a3", fg="white", font=("Impact", 15), anchor=W)
        total_teacher.place(x=737, y=480, width=180, height=23)
        total_teacher.config(text=teacher_count())

        total_admin = Label(Dash, text="0000", bg="#0076a3", fg="white", font=("Impact", 15), anchor=W)
        total_admin.place(x=737, y=537, width=180, height=23)
        total_admin.config(text=admin_count())

        difference = Label(Dash, text="0000", bg="#0076a3", fg="white", font=("Impact", 15), anchor=W)
        difference.place(x=737, y=593, width=180, height=23)
        difference.config(text=(teacher_count() - admin_count()))
    except:
        pass

    # Users bars
    try:
        grader_user = Label(Dash, text="SYNCED", fg="White", bg="#3b3086")
        grader_user.place(x=974, y=480, height=23, width=180)

        graders = ttk.Progressbar(Dash, orient=HORIZONTAL, length=180, mode="determinate", value=89)
        graders.place(x=974, y=537, height=23)

        global ram_progress
        ram_progress = ttk.Progressbar(Dash, orient="horizontal", length=180, mode="determinate")
        ram_progress.place(x=974, y=593, height=23)
        update_usage()
    except:
        pass


# student cal
try:
    def student_count():
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
            return

        query = "select id, und from student"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1
        return count

    def student_count_female():
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
            return

        query = "select id, und from student where gender = \'Male\'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1

        female_count = student_count() - count
        female_count = (female_count * 100) / student_count()
        return female_count

    def student_count_male():
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
            return

        query = "select id, und from student where gender = \'Female\'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1

        male_count = student_count() - count
        male_count = (male_count * 100) / student_count()
        return male_count

    def student_count_buddhism():
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
            return

        query = "select id, und from student where religion = \'Buddhism\'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1

        buddhist_count = count
        buddhist_count = (buddhist_count * 100) / student_count()
        return buddhist_count

    def student_count_Christian():
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
            return

        query = "select id, und from student where religion = \'Christian\'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1

        Christian_count = count
        Christian_count = (Christian_count * 100) / student_count()
        return Christian_count

    def student_count_Muslim():
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
            return

        query = "select id, und from student where religion = \'Muslim\'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for row in result:
            if int(row[1]) > int(Year):
                count += 1

        Muslim_count = count
        Muslim_count = (Muslim_count * 100) / student_count()
        return Muslim_count
except:
    pass

# teacher cal
try:
    def teacher_count():
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
            return

        query = "select nic from teacher"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        return count

    def teacher_count_male():
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
            return

        query = "select nic from teacher where gender = \"Male\""
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        count = (count*100)/teacher_count()
        return count

    def teacher_count_female():
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
            return

        query = "select nic from teacher where gender = \"Female\""
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        count = (count * 100) / teacher_count()
        return count

    def grader_count():
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
            return

        query = "select nic from grader"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        return count

    def grader_count_percentage():
        count = (grader_count()*100)/teacher_count()
        return count
except:
    pass

# admin cal
try:
    def admin_count():
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
            return

        query = "select nic from admin"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        return count
except:
    pass

# inventory
try:
    def inventory_sponsor_count():
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
            return

        query = "select id from sponsor"
        mycursor.execute(query)
        result = mycursor.fetchall()
        con.close()

        count = 0
        for _ in result:
            count += 1
        return count
except:
    pass

# User cal
try:
    def update_usage():
        used_ram = psutil.virtual_memory().used
        ram_percentage = (used_ram / total_ram) * 100
        ram_progress["value"] = ram_percentage
        Dash.after(1000, update_usage)
    total_ram = psutil.virtual_memory().total
except:
    pass
