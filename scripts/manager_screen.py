# TODO: Dante, create the screen that a manager would see after logging in (using Tkinter)

# don't worry about having the screen in sync with the login screen, simply create your own canvas, frame, etc. 
# this screen can stand alone for now and later we can think about how we will sync this with the login screen

# look at page 43 of the Second Phase Report (reports/second_phase_report.pdf)
# the screen should look like the "My Task" box with every feature for manager listed as buttons and having each feature clickable to open a new screen associated with the feature
# look at specifications that professor posted to see what features manager has
# the new screen for each feature can simply say "Hello World" or something relevant for now, but the main goal is having it open to a new screen associated with the feature

import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow


def main() :
    root = tk.Tk()
    app = Window_Manager_Screen(root)

class Window_Manager_Screen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        titleLabel = tk.Label(frame, text="Manager", bg='white', font=('Times New Roman', 30))
        titleLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), command=self.signOutWindow)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        privilegesFrame = tk.Frame(frame, bg='#cccccc')
        privilegesFrame.place(relx=0.05, rely=0.25, relwidth=0.3, relheight=0.7)

        privilegesLabel = tk.Label(privilegesFrame, text="Manager Privileges", bg="white", font=('Times New Roman', 12, 'bold'))
        privilegesLabel.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")

        reviewButton = tk.Button(privilegesFrame, text="Check \nComplaints/Compliments", bg="white", font=('Times New Roman', 12), command=self.checkReviewsWindow)
        reviewButton.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

        registerButton = tk.Button(privilegesFrame, text="View Registrations", bg="white", font=('Times New Roman', 12), command=self.registerSurferWindow)
        registerButton.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.1)

        manageCustButton = tk.Button(privilegesFrame, text="Manage Customers", bg="white", font=('Times New Roman', 12), command=self.manageCustWindow)
        manageCustButton.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

        manageStaffButton = tk.Button(privilegesFrame, text="Manage Staffs", bg="white", font=('Times New Roman', 12), command=self.manageStaffWindow)
        manageStaffButton.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

        tabooListFrame = tk.Frame(frame, bg='#cccccc')
        tabooListFrame.place(relx=0.4, rely=0.25, relwidth=0.3, relheight=0.6)

        tabooListLabel = tk.Label(tabooListFrame, text="Taboo List", bg="white", font=('Times New Roman', 16))
        tabooListLabel.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

        tabooListTextBox = tk.Text(tabooListFrame, height=12, width=21)
        tabooListTextBox.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)



        self.root.mainloop()

    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)
    def checkReviewsWindow(self):
        self.openCheckReviewsWindow = tk.Toplevel(self.root)
        self.app = checkReviewsWindow(self.openCheckReviewsWindow)
    def registerSurferWindow(self):
        self.openRegisterSurferWindow = tk.Toplevel(self.root)
        self.app = registerSurferWindow(self.openRegisterSurferWindow)
    def manageCustWindow(self):
        self.openManageCustWindow = tk.Toplevel(self.root)
        self.app = manageCustWindow(self.openManageCustWindow)
    def manageStaffWindow(self):
        self.openManageStaffWindow = tk.Toplevel(self.root)
        self.app = manageStaffWindow(self.openManageStaffWindow)

class checkReviewsWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkReviewsLabel = tk.Label(frame, text="You chose to check reviews!", font=('Times New Roman', 20), bg="#e6e6e6")
        checkReviewsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class registerSurferWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        registerSurferLabel = tk.Label(frame, text="You chose to view registrations!", font=('Times New Roman', 20), bg="#e6e6e6")
        registerSurferLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class manageCustWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        manageCustLabel = tk.Label(frame, text="You chose to manage customers!", font=('Times New Roman', 14), bg="#e6e6e6")
        manageCustLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
class manageStaffWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        manageStaffLabel = tk.Label(frame, text="You chose to manage staffs!", font=('Times New Roman', 14), bg="#e6e6e6")
        manageStaffLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

main()