# TODO: Dante, create the screen that a delivery person would see after logging in (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for delivery people listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features delivery people have
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature
import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow


def main():
    root = tk.Tk()
    app = Window_Delivery_Screen(root)

class Window_Delivery_Screen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.signOutWindow)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        deliveryPersonLabel = tk.Label(frame, text="Delivery Person", font=('Times New Roman', 20), bg="white")
        deliveryPersonLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        findCustomerButton = tk.Button(frame, text="Find Customer", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.findCustomerWindow)
        findCustomerButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

        viewOwnRatingButton = tk.Button(frame, text="View Personal Ratings", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.viewOwnRatingsWindow)
        viewOwnRatingButton.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)
    def findCustomerWindow(self):
        self.openFindCustomerWindow = tk.Toplevel(self.root)
        self.app = findCustomerWindow(self.openFindCustomerWindow)
    def viewOwnRatingsWindow(self):
        self.openViewOwnRatingsWindow = tk.Toplevel(self.root)
        self.app = viewOwnRatingsWindow(self.openViewOwnRatingsWindow)

class findCustomerWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        findCustomerLabel = tk.Label(frame, text="You chose to find customer!", font=('Times New Roman', 20), bg="#e6e6e6")
        findCustomerLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class viewOwnRatingsWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkOwnRatingsLabel = tk.Label(frame, text="You chose to view own ratings!", font=('Times New Roman', 20), bg="#e6e6e6")
        checkOwnRatingsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

main()