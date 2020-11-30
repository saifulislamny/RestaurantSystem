# This file is the central part of the entire system

import tkinter as tk
from startup import login_screen
from animation_at_startup import startUpAnimation

def startup():
    root = tk.Tk()
    startUpAnimation(root)
    # Play time for animation screen transition into login screen
    root.after(3000, lambda: login_screen(root))
    root.mainloop()
    pass

if __name__ == '__main__':
    startup()

# TODO: at the end of the project, insert 2 chefs, 2 delivery people, and 1 mananger