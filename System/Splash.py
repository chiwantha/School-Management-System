from tkinter import *
from tkinter import ttk
import time
import winreg
import Access
import mysql.connector
import os


class SplashScreen:
    def __init__(self, root):
        self.root = root
        self.loading = None
        self.fake = None

    def create_widgets(self):
        self.root.overrideredirect(True)
        self.root.attributes('-alpha', 0.0)  # Set window transparency initially
        self.root.wait_visibility(self.root)  # Wait until window is visible
        self.root.attributes('-alpha', 1.0)  # Set window transparency to full

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 779
        window_height = 421
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        spl = Frame(self.root, height=442, width=779)
        spl.pack()

        current = os.path.dirname(os.path.realpath(__file__))
        back = PhotoImage(file=current + "\\.ux\\splash\\Splash.png")
        background = Label(spl, image=back)
        background.image = back
        background.place(x=0, y=0, relheight=1, relwidth=1)

        self.loading = ttk.Progressbar(self.root, orient=HORIZONTAL, length=417, mode="determinate")
        self.loading.place(x=290, y=224, height=34)

        self.fake = Label(self.root, text="", bg="#ce4912", anchor=W, fg="White")
        self.fake.place(x=289, y=263, width=150, height=15)

    def step(self):
        self.fake.config(text="collecting files ....")
        for i in range(0, 50):
            self.loading["value"] += 1
            self.root.update_idletasks()
            time.sleep(0.01)

        self.fake.config(text="connecting database ....")
        time.sleep(3)

        for i in range(50, 70):
            self.loading["value"] += 1
            self.root.update_idletasks()
            time.sleep(0.01)

        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\PADMA")
            host = winreg.QueryValueEx(key, "Host")[0]
            user = winreg.QueryValueEx(key, "User")[0]
            password = winreg.QueryValueEx(key, "Pass")[0]
            winreg.CloseKey(key)

            con = mysql.connector.connect(host=host, user=user, password=password)
            con.close()
            Access.stu = "online"
            print("pass")
            Access.bt_status = "disabled"
        except:
            Access.bt_status = "normal"
            pass

        for i in range(70, 100):
            self.loading["value"] += 1
            self.root.update_idletasks()
            time.sleep(0.01)
            self.fake.config(text="loading login ....")

        if self.loading["value"] == 100:
            self.root.after(2000, self.load)
        else:
            print("error")

    def load(self):
        self.root.destroy()
        Access.acc()


if __name__ == "__main__":
    root = Tk()
    splash_screen = SplashScreen(root)
    splash_screen.create_widgets()
    root.after(3000, splash_screen.step)
    root.mainloop()
