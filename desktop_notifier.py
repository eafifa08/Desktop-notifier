# Desktop notifier by meshkov s.
# requires https://github.com/YuriyLisovskiy/pynotifier
# pip install py-notifier
from pynotifier import Notification
from sys import platform
import os
import tkinter as tk


def abs_path(os_ver):
    if os_ver == 1:
        return os.path.abspath('media\smile.png')
    elif os_ver == 3:
        return os.path.abspath('media\smile.ico')


def what_is_os():
    if platform == "linux" or platform == "linux2":
        # linux
        return 1
    elif platform == "darwin":
        # OS X
        return 2
    elif platform == "win32":
        # Windows...
        return 3


def run_tk():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            self.btn_show = tk.Button(self)
            self.btn_show["text"] = "Показать уведомление"
            self.btn_show["command"] = self.show
            self.btn_show.pack()

            self.var_title = tk.StringVar()
            self.var_title.set("Заголовок сообщения")
            self.entry_title = tk.Entry(self, textvariable=self.var_title, width=30)
            self.entry_title.pack()

            self.var_body = tk.StringVar()
            self.var_body.set("Здесь могла бы быть ваша реклама")
            self.entry_body = tk.Entry(self, textvariable=self.var_body, width=40)
            self.entry_body.pack()


            self.scl_interval = tk.Scale(self, orient=tk.HORIZONTAL, length=250, from_=1, to=8, tickinterval=1, resolution=1)
            self.scl_interval.pack()

            self.btn_quit = tk.Button(self, text="Выход", command=self.master.destroy)
            self.btn_quit.pack()

        def show(self):
            Notification(
                title=self.var_title.get(),
                description=self.var_body.get(),
                icon_path=abs_path(what_is_os()),  # On Windows .ico is required, on Linux - .png
                duration=self.scl_interval.get(),  # Duration in seconds
                urgency='normal'
            ).send()

    root = tk.Tk()
    root.geometry('300x300')
    root.title('Desktop Notifier')
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    run_tk()

