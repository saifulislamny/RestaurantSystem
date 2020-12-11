# This file is the central part of the entire system

# TODO: Saiful, specify that you worked on this file in the header (look at Daniel's code in db_handling.py when he adds the header)

import tkinter as tk
from startup import login_screen
from animation_at_startup import startUpAnimation

def startup():
    root = tk.Tk()
    startUpAnimation(root)
    # Play time for animation screen transition into login screen
    root.after(5000, lambda: login_screen(root))
    root.mainloop()
    pass

if __name__ == '__main__':
    startup()