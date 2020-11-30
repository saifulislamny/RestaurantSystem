# TODO: Dante, this should be the last thing you do so visit this later when you complete everything else
# create the animation that we will have when opening up the application (this is the first thing that is seen when application is executed)
# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen
import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow
from startup import login_screen


def startUpAnimation(root):
    app = Window_Animation_Startup_Screen(root)

class Window_Animation_Startup_Screen:
    def __init__(self,master):

        canvas = tk.Canvas(master, height=500, width=800)
        canvas.pack()
        frame = tk.Frame(master, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        startUpPage = start_up_page(frame,master)


class start_up_page:
    def __init__(self, frame, root):

        TitleLabel = tk.Label(frame, text="Food Delivery System", font=('Times New Roman', 24), bg="white")
        TitleLabel.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)

        NamesLabel = tk.Label(frame, text="Team X", font=('Times New Roman', 20), bg="white")
        NamesLabel.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
