import tkinter as tk
from tkinter import font

# TODO: Dante, specify that you worked on this file in the header (look at Daniel's code in db_handling.py when he adds the header)
# TODO: Dante, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Dante, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Dante, check these errors that I get with VSCode
# TODO: Dante, add in-line documentation to show what each class/function does where it may not be immediately understood
# TODO: Dante, the sign out button is supposed to close all windows of Tkinter and open the login screen again

class signOutWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutLabel = tk.Label(frame, text="You signed out!", font=('Times New Roman', 20), bg="#e6e6e6")
        signOutLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)