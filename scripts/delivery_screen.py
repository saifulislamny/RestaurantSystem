# TODO: Dante, create the screen that a delivery person would see after logging in (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for delivery people listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features delivery people have
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature
import tkinter as tk
from tkinter import font

from sign_out_screen import signOutWindow

# TODO: Dante, specify that you and I worked on this file in the header (look at Daniel's code in db_handling.py when he adds the header)
# TODO: Dante, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Dante, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Dante, check these errors that I get with VSCode
# TODO: Dante, remove TODOs that you have already completed (leave them if you haven't completed yet)
# TODO: Dante, add in-line documentation to show what each class/function does where it may not be immediately understood

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

        # TODO: Dante, "Find Customer" is not a feature. Did you mean "View Deliveries In Progress" or something similar? If so, use complete_delivery() and view_deliveries() from delivery_operations.py to fulfill this window (if they are already implemented)

class viewOwnRatingsWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkOwnRatingsLabel = tk.Label(frame, text="You chose to view own ratings!", font=('Times New Roman', 20), bg="#e6e6e6")
        checkOwnRatingsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        # TODO: Dante, fulfill this window by using view_ratings_of_delivery_person() from delivery_operations.py (if it is already implemented)
    
# TODO: Hafsa,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Delivery Person screen
# let him know what buttons he has to add by specifying in the hafsa_comments_for_dante.txt file (in the repo, comments/hafsa_comments_for_dante.txt).
# you can run the Delivery Person screen by running $ python3 delivery_screen.py

main()