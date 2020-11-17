# This file is the central part of the entire system

import tkinter as tk
from startup import login_screen

def startup():
    root = tk.Tk()
    login_screen(root)
    root.mainloop()
    pass

if __name__ == '__main__':
    startup()