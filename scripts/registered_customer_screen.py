# TODO: Dante, create the screen that a registered customer would see after logging in (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for registered customers listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features registered customers have
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature

# keep in mind that many of these features are also features for VIP customers so you will reuse this stuff for VIP_customer_screen.py
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

        forCustLabel = tk.Label(frame, text="Registered Customer", font=('Times New Roman', 20), bg="white")
        forCustLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        eatingOptionFrame = tk.Frame(frame, bg='#cccccc')
        eatingOptionFrame.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.65)

        eatOptions = tk.Label(eatingOptionFrame, text="Options:", bg="white", font=('Times New Roman', 18), relief="solid")
        eatOptions.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")

        eatAtRestButton = tk.Button(eatingOptionFrame, text="Dine In", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.eatThereWindow)
        eatAtRestButton.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)

        pickUpFoodButton = tk.Button(eatingOptionFrame, text="Pick Up", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.pickUpWindow)
        pickUpFoodButton.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.1)

        deliveryButton = tk.Button(eatingOptionFrame, text="Delivery", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.deliveryWindow)
        deliveryButton.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.1)

        topDishesButton = tk.Button(frame, text="View Top Dishes", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.topDishWindow)
        topDishesButton.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menuWindow)
        menuButton.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

        fileComplaintButton = tk.Button(frame, text="File Complaint", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.fileCompWindow)
        fileComplaintButton.place(relx=0.6, rely=0.55, relwidth=0.3, relheight=0.1)

        checkWarningsButton = tk.Button(frame, text="Check Warnings", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.checkWarnWindow)
        checkWarningsButton.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.1)

        accountBalanceButton = tk.Button(frame, text="Account Balance", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.accBalWindow)
        accountBalanceButton.place(relx=0.6, rely=0.85, relwidth=0.3, relheight=0.1)

        self.root.mainloop()

    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)
    def eatThereWindow(self):
        self.openEatThereWindow = tk.Toplevel(self.root)
        self.app = eatThereWindow(self.openEatThereWindow)
    def pickUpWindow(self):
        self.openPickUpWindow = tk.Toplevel(self.root)
        self.app = pickUpWindow(self.openPickUpWindow)
    def deliveryWindow(self):
        self.openDeliveryWindow = tk.Toplevel(self.root)
        self.app = deliveryWindow(self.openDeliveryWindow)
    def topDishWindow(self):
        self.openTopDishWindow = tk.Toplevel(self.root)
        self.app = topDishWindow(self.openTopDishWindow)
    def menuWindow(self):
        self.openMenuWindow = tk.Toplevel(self.root)
        self.app = menuWindow(self.openMenuWindow)
    def fileCompWindow(self):
        self.openFileCompWindow = tk.Toplevel(self.root)
        self.app = fileCompWindow(self.openFileCompWindow)
    def checkWarnWindow(self):
        self.openCheckWarnWindow = tk.Toplevel(self.root)
        self.app = checkWarnWindow(self.openCheckWarnWindow)
    def accBalWindow(self):
        self.openAccBalWindow = tk.Toplevel(self.root)
        self.app = accBalWindow(self.openAccBalWindow)

# TODO: Dante, the "Options" should be its own window for the button "Make Order for Delivery/Pickup"

class eatThereWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        eatThereLabel = tk.Label(frame, text="You chose to dine in!", font=('Times New Roman', 20), bg="#e6e6e6")
        eatThereLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class pickUpWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        pickUpLabel = tk.Label(frame, text="You chose to pickup food!", font=('Times New Roman', 20), bg="#e6e6e6")
        pickUpLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class deliveryWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        deliveryLabel = tk.Label(frame, text="You chose delivery!", font=('Times New Roman', 20), bg="#e6e6e6")
        deliveryLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class topDishWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        topDishLabel = tk.Label(frame, text="You chose to view top dishes!", font=('Times New Roman', 20), bg="#e6e6e6")
        topDishLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.
        # TODO: Saiful, include comment for how to fulfill this window
class menuWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 20), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
    # TODO: Dante, fulfill this window by using view_menu() from all_user_operations.py (if it's already implemented)
class fileCompWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        fileCompLabel = tk.Label(frame, text="You chose to file a complaint!", font=('Times New Roman', 20), bg="#e6e6e6")
        fileCompLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        # TODO: Dante, fulfill this window by using feedback_for_chef() and feedback_for_delivery() from customer_operations.py (if it's already implemented)
class checkWarnWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkWarnLabel = tk.Label(frame, text="You chose to check warnings!", font=('Times New Roman', 20), bg="#e6e6e6")
        checkWarnLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
    # TODO (for later):
class accBalWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        accBalLabel = tk.Label(frame, text="You chose to check account balance!", font=('Times New Roman', 18), bg="#e6e6e6")
        accBalLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
    # TODO (for later): Dante, fulfill this window by using view_deposit() from customer_operations.py

# TODO: Tanzil,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Registered Customer screen
# let him know what buttons he has to add by specifying in the tanzil_comments_for_dante.txt file (in the repo, comments/tanzil_comments_for_dante.txt).
# you can run the Registered Customer screen by running $ python3 registered_customer_screen.py

main()