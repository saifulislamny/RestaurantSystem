''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen

# TODO: Dante, check these errors that I get with VSCode

# def main() :
#    root = tk.Tk()
#    app = ManagerScreen(root,"hello321")

#class to show what appears on the main screen of "Manager"
class ManagerScreen:
    def __init__(self,master,user):
        self.root=master
        self.user=user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        titleLabel = tk.Label(frame, text="Manager", bg='white', font=('Times New Roman', 30))
        titleLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        privilegesFrame = tk.Frame(frame, bg='#cccccc')
        privilegesFrame.place(relx=0.05, rely=0.25, relwidth=0.3, relheight=0.7)

        privilegesLabel = tk.Label(privilegesFrame, text="Manager Privileges", bg="white", font=('Times New Roman', 12, 'bold'))
        privilegesLabel.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.1, anchor="center")

        reviewButton = tk.Button(privilegesFrame, text="Check \nComplaints/Compliments", bg="white", font=('Times New Roman', 12), command=self.check_reviews_window)
        reviewButton.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.1)

        registerButton = tk.Button(privilegesFrame, text="View Registrations", bg="white", font=('Times New Roman', 12), command=self.register_surfer_window)
        registerButton.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.1)

        manageCustButton = tk.Button(privilegesFrame, text="Manage Customers", bg="white", font=('Times New Roman', 12), command=self.manage_cust_window)
        manageCustButton.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

        manageStaffButton = tk.Button(privilegesFrame, text="Manage Staffs", bg="white", font=('Times New Roman', 12), command=self.manage_staff_window)
        manageStaffButton.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)

        tabooListFrame = tk.Frame(frame, bg='#cccccc')
        tabooListFrame.place(relx=0.4, rely=0.25, relwidth=0.3, relheight=0.1)

        tabooListButton = tk.Button(tabooListFrame, text="View Taboo List", bg="white", font=('Times New Roman', 14), command=self.taboo_list_window)
        tabooListButton.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.7)


        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to open check reviews window
    def check_reviews_window(self):
        self.app = CheckReviewsWindow(self.root,self.user)
# function to open register surfer window
    def register_surfer_window(self):
        self.app = RegisterSurferWindow(self.root,self.user)
# function to open manage customer window
    def manage_cust_window(self):
        self.app = ManageCustWindow(self.root,self.user)
# function to open manage staff window
    def manage_staff_window(self):
        self.app = ManageStaffWindow(self.root,self.user)
# function to open taboo list window
    def taboo_list_window(self):
        self.app = TabooListWindow(self.root,self.user)

#class to show what appears after "Check Complaints/Compliments" button pressed
class CheckReviewsWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        checkReviewsLabel = tk.Label(frame, text=self.user, font=('Times New Roman', 20), bg="#e6e6e6")
        checkReviewsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_chef_complaints_and_compliments() and view_delivery_complaints_and_compliments() from manager_operations.py (if it's already implemented)
#class to show what appears after "View Registrations" button pressed
class RegisterSurferWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        registerSurferLabel = tk.Label(frame, text="You chose to view registrations!", font=('Times New Roman', 20), bg="#e6e6e6")
        registerSurferLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
        # TODO: Dante, fulfill this window by using view_customer_registrations(), accept_customer_registrations(), and decline_customer_registrations() from manager_operations.py (if it's already implemented)
#class to show what appears after "Manage Customers" button pressed
class ManageCustWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        manageCustLabel = tk.Label(frame, text="You chose to manage customers!", font=('Times New Roman', 14), bg="#e6e6e6")
        manageCustLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        customerNameField = tk.Entry(frame)
        customerNameField.place(relx=0.15, rely=0.3, relwidth=0.45, relheight=0.05)

        getCustomerNameButton = tk.Button(frame, text="Close \nAccount", bg='#999999', font=('Times New Roman', 10), borderwidth=2)
        getCustomerNameButton.place(relx=0.65, rely=0.3, relwidth=0.1, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.07)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
        # TODO: Dante, fulfill this window by using close_customer_accounts() from manager_operations.py (if it's already implemented)
#class to show what appears after "Manage Staffs" button pressed
class ManageStaffWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        manageStaffLabel = tk.Label(frame, text="You chose to manage staffs!", font=('Times New Roman', 14), bg="#e6e6e6")
        manageStaffLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using close_employee_account(), cut_employee_pay(), and raise_employee_pay() from manager_operations.py (if it's already implemented)
#class to show what appears after "View Taboo List" button pressed
class TabooListWindow:
    def __init__(self, master,user):
        self.root = master
        self.user=user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        tabooListLabel = tk.Label(frame, text=self.user, font=('Times New Roman', 14), bg="#e6e6e6")
        tabooListLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

# TODO: Tanzil,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Manager screen
# let him know what buttons he has to add by specifying in the tanzil_comments_for_dante.txt file (in the repo, comments/tanzil_comments_for_dante.txt).
# you can run the Manager screen by running $ python3 manager_screen.py

# main()