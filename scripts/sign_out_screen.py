import tkinter as tk
from tkinter import font

class signOutWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutLabel = tk.Label(frame, text="You signed out!", font=('Times New Roman', 20), bg="#e6e6e6")
        signOutLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)