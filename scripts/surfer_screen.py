# TODO: Dante, create the screen that a surfer would see (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for surfers listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features surfers have
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature

import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow


def main():
    root = tk.Tk()
    app = Window_Surfer_Screen(root)

class Window_Surfer_Screen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.signOutWindow)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        forSurferLabel = tk.Label(frame, text="Guest/Surfer", font=('Times New Roman', 20), bg="white")
        forSurferLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        topDishesButton = tk.Button(frame, text="View Top Dishes", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.topDishWindow)
        topDishesButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menuWindow)
        menuButton.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.1)

        signUpButton = tk.Button(frame, text="Sign Up", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.signUpWindow)
        signUpButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)
    def topDishWindow(self):
        self.openTopDishWindow = tk.Toplevel(self.root)
        self.app = topDishWindow(self.openTopDishWindow)
    def menuWindow(self):
        self.openMenuWindow = tk.Toplevel(self.root)
        self.app = menuWindow(self.openMenuWindow)
    def signUpWindow(self):
        self.openSignUpWindow = tk.Toplevel(self.root)
        self.app = signUpWindow(self.openSignUpWindow)

class topDishWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        topDishLabel = tk.Label(frame, text="You chose to view top dishes!", font=('Times New Roman', 20), bg="#e6e6e6")
        topDishLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class menuWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 20), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class signUpWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signUpLabel = tk.Label(frame, text="You chose to sign up!", font=('Times New Roman', 20), bg="#e6e6e6")
        signUpLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

main()