from tkinter import *
import Book
import os

current = os.path.dirname(os.path.realpath(__file__))


def Library_management(frame):
    LM = Frame(frame, height=651, width=1185)
    LM.pack()

    back = PhotoImage(file=current+"/.ux./library/.menu/Lib Menu.png")
    Background = Label(LM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)

    User_btn = Button(LM, text="User", activeforeground="gray", font=("Impact", 15), bd=0
                      , bg="#302f3f", activebackground="#302f3f", fg="White")
    User_btn.place(x=191, y=264, width=175, height=31)

    Book_btn = Button(LM, text="Book Management", activeforeground="gray", font=("Impact", 15), bd=0
                      , bg="#302f3f", activebackground="#302f3f", fg="White"
                      , command=lambda: (LM.destroy(), Book.Book_Menu(frame)))
    Book_btn.place(x=191, y=310, width=175, height=31)

    Report_btn = Button(LM, text="Report", activeforeground="gray", font=("Impact", 15), bd=0
                        , bg="#302f3f", activebackground="#302f3f", fg="White")
    Report_btn.place(x=191, y=356, width=175, height=31)

    Librarion_btn = Button(LM, text="Librarion", activeforeground="gray", font=("Impact", 15), bd=0
                           , bg="#302f3f", activebackground="#302f3f", fg="White")
    Librarion_btn.place(x=191, y=403, width=175, height=31)

    About_btn = Button(LM, text="About", activeforeground="gray", font=("Impact", 15), bd=0
                       , bg="#302f3f", activebackground="#302f3f", fg="White"
                       , command=lambda: (LM.destroy(), About_Library_management(frame)))
    About_btn.place(x=191, y=450, width=175, height=31)

    LogOut_btn = Button(LM, text="Log Out", activeforeground="gray", font=("Impact", 15), bd=0
                        , bg="#ce4912", activebackground="#ce4912", fg="White")
    LogOut_btn.place(x=191, y=496, width=175, height=31)


def About_Library_management(frame):
    ALM = Frame(frame, height=651, width=1185)
    ALM.pack()

    back = PhotoImage(file=current+"/.ux/library/.about/about Library.png")
    Background = Label(ALM, image=back)
    Background.image = back
    Background.place(x=0, y=0, relheight=1, relwidth=1)
