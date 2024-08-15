from tkinter import *
import os
import Access
import Admin
import Application
import Inventory
import Library
import Student
import Teachers
import Mark
import winreg
import mysql.connector
from tkinter import messagebox


who = ""
nic = ""


def ui():
    ui_window = Tk()
    ui_window.iconbitmap("pad.ico")

    screen_width = ui_window.winfo_screenwidth()
    screen_height = ui_window.winfo_screenheight()
    window_width = 1185
    window_height = 671
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2 - 20
    ui_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    ui_window.resizable(False, False)
    ui_window.title("Padmawathie National Collage - School Management Software")

    Main_frame = Frame(ui_window, bg="red")
    Main_frame.place(height=651, width=1185)

    current = os.path.dirname(os.path.realpath(__file__))

    def collect():
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
        parameters = [nic]
        mycursor.execute(query, parameters)
        r = mycursor.fetchone()
        con.close()

        if r is not None:
            if r[1] == "on":
                index = student.index("Enrollment")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Enrollment")
                student.entryconfig(index, state="disabled")
            if r[2] == "on":
                index = student.index("Search")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Search")
                student.entryconfig(index, state="disabled")
            if r[3] == "on":
                index = student.index("Edit...")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Edit...")
                student.entryconfig(index, state="disabled")
            if r[4] == "on":
                index = student.index("Acadamic")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Acadamic")
                student.entryconfig(index, state="disabled")
            if r[5] == "on":
                index = student.index("Note")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Note")
                student.entryconfig(index, state="disabled")
            if r[6] == "on":
                index = student.index("Report")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("Report")
                student.entryconfig(index, state="disabled")
            if r[7] == "on":
                index = student.index("St.Delete")
                student.entryconfig(index, state="normal")
            else:
                index = student.index("St.Delete")
                student.entryconfig(index, state="disabled")

            if r[8] == "on":
                index = teacher.index("New..")
                teacher.entryconfig(index, state="normal")
            else:
                index = teacher.index("New..")
                teacher.entryconfig(index, state="disabled")
            if r[9] == "on":
                index = teacher.index("Find")
                teacher.entryconfig(index, state="normal")
            else:
                index = teacher.index("Find")
                teacher.entryconfig(index, state="disabled")
            if r[10] == "on":
                index = teacher.index("Edit")
                teacher.entryconfig(index, state="normal")
            else:
                index = teacher.index("Edit")
                teacher.entryconfig(index, state="disabled")
            if r[11] == "on":
                index = teacher.index("Graders")
                teacher.entryconfig(index, state="normal")
            else:
                index = teacher.index("Graders")
                teacher.entryconfig(index, state="disabled")
            if r[12] == "on":
                index = teacher.index("User Rights")
                teacher.entryconfig(index, state="normal")
            else:
                index = teacher.index("User Rights")
                teacher.entryconfig(index, state="disabled")

            if r[13] == "on":
                index = mark.index("Form")
                mark.entryconfig(index, state="normal")
            else:
                index = mark.index("Form")
                mark.entryconfig(index, state="disabled")
            if r[14] == "on":
                index = mark.index("Editors")
                mark.entryconfig(index, state="normal")
            else:
                index = mark.index("Editors")
                mark.entryconfig(index, state="disabled")
            if r[15] == "on":
                index = mark.index("Viewer")
                mark.entryconfig(index, state="normal")
            else:
                index = mark.index("Viewer")
                mark.entryconfig(index, state="disabled")
            if r[16] == "on":
                index = mark.index("Report")
                mark.entryconfig(index, state="normal")
            else:
                index = mark.index("Report")
                mark.entryconfig(index, state="disabled")

            if r[17] == "on":
                index = assets.index("View")
                assets.entryconfig(index, state="normal")
            else:
                index = assets.index("View")
                assets.entryconfig(index, state="disabled")
            if r[18] == "on":
                index = assets.index("Inventory & Books")
                assets.entryconfig(index, state="normal")
            else:
                index = assets.index("Inventory & Books")
                assets.entryconfig(index, state="disabled")
            if r[19] == "on":
                index = assets.index("Inventory Items")
                assets.entryconfig(index, state="normal")
            else:
                index = assets.index("Inventory Items")
                assets.entryconfig(index, state="disabled")
            if r[20] == "on":
                index = assets.index("Sponsors")
                assets.entryconfig(index, state="normal")
            else:
                index = assets.index("Sponsors")
                assets.entryconfig(index, state="disabled")
            if r[21] == "on":
                index = assets.index("Inventory Report")
                assets.entryconfig(index, state="normal")
            else:
                index = assets.index("Inventory Report")
                assets.entryconfig(index, state="disabled")

            if r[22] == "on":
                index = library.index("Library Management ( v 0.11 )")
                library.entryconfig(index, state="normal")
            else:
                index = library.index("Library Management ( v 0.11 )")
                library.entryconfig(index, state="disabled")

    def rights():
        if who == "admin":
            pass
        elif who == "user":
            collect()

    def home_back():
        back = PhotoImage(file=current+"/.ux/padma/.home/Home.png")
        Background = Label(Main_frame, image=back)
        Background.image = back
        Background.place(x=0, y=0, relheight=1, relwidth=1)

    def clear():
        for frame in Main_frame.winfo_children():
            frame.destroy()

    def menu_home():
        clear()
        home_back()

    home_back()

    menu_bar = Menu(ui_window, tearoff=0)
    ui_window.config(menu=menu_bar)

    home = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Home", menu=home)
    home.add_command(label="Home", command=menu_home)
    home.add_command(label="Log Out", command=lambda: (ui_window.destroy(), Access.acc()))
    home.add_command(label="Quit", command=lambda: (ui_window.destroy()))

    admin = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Admin", menu=admin)
    admin.add_command(label="Admin Dashboard", command=lambda: (clear(), Admin.dashboard(Main_frame)))
    if who == "admin":
        admin.add_command(label="Admin Account", command=lambda: (clear(), Admin.adash(Main_frame)))
    elif who == "user":
        admin.add_command(label="Admin Account", command=lambda: (clear(), Admin.adash(Main_frame)), state="disabled")
    else:
        pass

    student = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Student", menu=student)
    student.add_command(label="Enrollment", command=lambda: (clear(), Student.Enrollment(Main_frame)))
    student.add_command(label="Search", command=lambda: (clear(), Student.Search(Main_frame)))
    student.add_separator()
    student.add_command(label="Edit...", command=lambda: (clear(), Student.Edit(Main_frame)))
    student.add_separator()
    student.add_command(label="Acadamic", command=lambda: (clear(), Student.Acadamic(Main_frame)))
    student.add_command(label="Note", command=lambda: Student.Note())
    student.add_separator()
    student.add_command(label="Report", command=lambda: (clear(), Student.Report(Main_frame)))
    student.add_separator()
    student.add_command(label="St.Delete", command=lambda: Student.st_Delete())

    teacher = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Teachers", menu=teacher)
    teacher.add_command(label="New..", command=lambda: (clear(), Teachers.Enrollment(Main_frame)))
    teacher.add_command(label="Find", command=lambda: (clear(), Teachers.Find(Main_frame)))
    teacher.add_separator()
    teacher.add_command(label="Edit", command=lambda: (clear(), Teachers.Edit(Main_frame)))
    teacher.add_separator()
    teacher.add_command(label="Graders", command=lambda: (clear(), Teachers.Grader(Main_frame)))
    teacher.add_command(label="User Rights", command=lambda: (clear(), Teachers.ur(Main_frame)))
    teacher.add_command(label="Passcode Control", command=lambda: (clear(), Teachers.pc(Main_frame)))

    mark = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Mark Sheet", menu=mark)
    form = Menu(mark, tearoff=0)
    mark.add_cascade(label="Form", menu=form)
    form.add_command(label="6-9 Mark Form", command=lambda: (clear(), Mark.Mark_form_6_9(Main_frame)))
    form.add_command(label="10-11 Mark Form ( upcoming )")
    form.add_command(label="12-13 Mark Form ( upcoming )")
    editors = Menu(mark, tearoff=0)
    mark.add_cascade(label="Editors", menu=editors)
    editors.add_command(label="6-9 Mark Editor", command=lambda: (clear(), Mark.edit(Main_frame)))
    editors.add_command(label="10-11 Mark Editor ( upcoming )")
    editors.add_command(label="12-13 Mark Editor ( upcoming )")
    mark.add_separator()
    mark.add_command(label="Viewer", command=lambda: (clear(), Mark.Viewer(Main_frame)))
    # mark.add_command(label="Transfer", command=lambda: (clear(), Mark.Viewer(Main_frame)))
    mark.add_command(label="Report", command=lambda: (clear(), Mark.Report(Main_frame)))

    assets = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Assets", menu=assets)
    view = Menu(assets, tearoff=0)
    assets.add_cascade(label="View", menu=view)
    view.add_command(label="Inventory Live", command=lambda: (clear(), Inventory.Live(Main_frame)))
    view.add_command(label="Inventory Receive", command=lambda: (clear(), Inventory.receive_view(Main_frame)))
    view.add_command(label="Inventory Expend", command=lambda: (clear(), Inventory.expend_view(Main_frame)))
    assets.add_command(label="Inventory Report", command=lambda: (clear(), Inventory.Report(Main_frame)))
    assets.add_separator()
    Inventory_items = Menu(assets, tearoff=0)
    assets.add_cascade(label="Inventory Items", menu=Inventory_items)
    Inventory_items.add_command(label="Receive Items", command=lambda: (clear(), Inventory.Receive(Main_frame)))
    Inventory_items.add_command(label="Expend Items", command=lambda: (clear(), Inventory.Expend(Main_frame)))
    assets.add_separator()
    add_inventory = Menu(assets, tearoff=0)
    assets.add_cascade(label="Inventory & Books", menu=add_inventory)
    add_inventory.add_command(label="New Inventory", command=lambda: (clear(), Inventory.Add_Inventory(Main_frame)))
    add_inventory.add_command(label="Add Inventory Books", command=lambda: (clear(), Inventory.Add_Books(Main_frame)))
    add_inventory.add_command(label="Book Keeper", command=lambda: (clear(), Inventory.Guardian(Main_frame)))
    assets.add_separator()
    assets.add_command(label="Sponsors", command=lambda: (clear(), Inventory.Sponsor(Main_frame)))
    assets.add_command(label="About Inventory System", command=lambda: (clear(), Inventory.About(Main_frame)))

    library = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Library", menu=library)
    library.add_command(label="Library Management ( v 0.11 )",
                        command=lambda: (clear(), Library.Library_management(Main_frame)))
    library.add_command(label="About Library Management Module",
                        command=lambda: (clear(), Library.About_Library_management(Main_frame)))

    application = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Application", menu=application)
    application.add_command(label="Software Info", command=lambda: (clear(), Application.About(Main_frame)))
    application.add_command(label="Help", command=lambda: Application.Help())
    application.add_separator()
    application.add_command(label="Contact Developer..", command=lambda: (clear(), Application.Contact(Main_frame)))
    preferences = Menu(application, tearoff=0)
    application.add_cascade(label="Preferences", menu=preferences)
    preferences.add_command(label="Database Settings", command=lambda: (clear(), Application.database(Main_frame)))

    rights()

    ui_window.mainloop()

# ui()
