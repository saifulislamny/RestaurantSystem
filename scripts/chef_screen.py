# TODO: Dante, create the screen that a chef would see after logging in (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for chefs listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features chefs have
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature
import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow


def main():
    root = tk.Tk()
    app = Window_Registered_Customer_Screen(root)

class Window_Registered_Customer_Screen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.signOutWindow)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        chefLabel = tk.Label(frame, text="Chef", font=('Times New Roman', 20), bg="white")
        chefLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        dishRatingButton = tk.Button(frame, text="View Personal Dish Ratings", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.dishRatingWindow)
        dishRatingButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menuWindow)
        menuButton.place(relx=0.35, rely=0.45, relwidth=0.3, relheight=0.1)

        addDescButton = tk.Button(frame, text="Add food \ndescription/keyword", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.addDescWindow)
        addDescButton.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)
    def dishRatingWindow(self):
        self.openDishRatingWindow = tk.Toplevel(self.root)
        self.app = dishRatingWindow(self.openDishRatingWindow)
    def menuWindow(self):
        self.openMenuWindow = tk.Toplevel(self.root)
        self.app = menuWindow(self.openMenuWindow)
    def addDescWindow(self):
        self.openAddDescWindow = tk.Toplevel(self.root)
        self.app = addDescWindow(self.openAddDescWindow)

class dishRatingWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        dishRatingLabel = tk.Label(frame, text="You chose to view dish ratings!", font=('Times New Roman', 20), bg="#e6e6e6")
        dishRatingLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class menuWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 20), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class addDescWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        addDescLabel = tk.Label(frame, text="You chose to add \ndescription/keyword!", font=('Times New Roman', 20), bg="#e6e6e6")
        addDescLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

main()