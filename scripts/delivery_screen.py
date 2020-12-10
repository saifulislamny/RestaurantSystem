''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
#from discussion_board_screen import DiscussionBoardScreen
#NOTE: Ignore Discussion Board for now (Do not click on button) because it seems to be causing problems. Will try to fix ASAP.

# TODO: Dante, check these errors that I get with VSCode

# def main():
#     root = tk.Tk()
#     app = DeliveryScreen(root,"test5")

#class to show what appears on the main screen for "Delivery" people
class DeliveryScreen:
    def __init__(self,master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        deliveryPersonLabel = tk.Label(frame, text="Delivery Person", font=('Times New Roman', 20), bg="white")
        deliveryPersonLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        viewDeliveriesButton = tk.Button(frame, text="View Deliveries", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.view_deliveries_window)
        viewDeliveriesButton.place(relx=0.15, rely=0.3, relwidth=0.3, relheight=0.1)

        viewOwnRatingButton = tk.Button(frame, text="View Personal Ratings", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.view_own_rating_window)
        viewOwnRatingButton.place(relx=0.15, rely=0.5, relwidth=0.3, relheight=0.1)

        viewCompButton = tk.Button(frame, text="View Compliments/Complaints", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.view_comp_window)
        viewCompButton.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.1)

        fileComplaintButton = tk.Button(frame, text="File Complaint", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.file_complaint_window)
        fileComplaintButton.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)

        writeComplimentButton = tk.Button(frame, text="Write Compliment", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.write_compliment_window)
        writeComplimentButton.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1)

        DiscussionBoardButton = tk.Button(frame, text="Discussion Board", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.disc_board_window)
        DiscussionBoardButton.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to open signout window
    def view_deliveries_window(self):
        self.app = ViewDeliveriesWindow(self.root,self.user)
# function to open signout window
    def view_own_rating_window(self):
        self.app = ViewOwnRatingsWindow(self.root,self.user)
# function to open view compliment/complaint window
    def view_comp_window(self):
        self.app = ViewCompWindow(self.root,self.user)
# function to open file complaint window
    def file_complaint_window(self):
        self.app = FileComplaintWindow(self.root,self.user)
# function to open write compliment window
    def write_compliment_window(self):
        self.app = WriteComplimentWindow(self.root,self.user)
# function to open discussion board window
    def disc_board_window(self):
        self.app = DiscussionBoardScreen(self.root,self.user)

#class to show what appears after "View Deliveries" button pressed
class ViewDeliveriesWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        viewDeliveriesLabel = tk.Label(frame, text="You chose to view deliveries!", font=('Times New Roman', 16), bg="#e6e6e6")
        viewDeliveriesLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        
        
        viewDelivButton = tk.Button(frame, text="View deliveries", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.view_deliv_window)
        viewDelivButton.place(relx=0.30, rely=0.5, relwidth=0.4, relheight=0.1)


        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, "Find Customer" is not a feature. Did you mean "View Deliveries In Progress" or something similar? If so, use complete_delivery() and view_deliveries() from delivery_operations.py to fulfill this window (if they are already implemented)

#class to show what appears after "View Personal Ratings" button pressed
class ViewOwnRatingsWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        checkOwnRatingsLabel = tk.Label(frame, text="You chose to view own ratings!", font=('Times New Roman', 16), bg="#e6e6e6")
        checkOwnRatingsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_ratings_of_delivery_person() from delivery_operations.py (if it is already implemented)
#class to show what appears after "View Compliments/Complaints" button pressed
class ViewCompWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        viewCompLabel = tk.Label(frame, text="You chose to view \ncompliments/complaints!", font=('Times New Roman', 16), bg="#e6e6e6")
        viewCompLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)


#class to show what appears after "File Complaint" button pressed
class FileComplaintWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        fileCompLabel = tk.Label(frame, text="You chose to file a complaint!", font=('Times New Roman', 16), bg="#e6e6e6")
        fileCompLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "Write Compliment" button pressed
class WriteComplimentWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        writeComplimentLabel = tk.Label(frame, text="You chose to write a compliment!", font=('Times New Roman', 16), bg="#e6e6e6")
        writeComplimentLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

    
# TODO: Hafsa,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Delivery Person screen
# let him know what buttons he has to add by specifying in the hafsa_comments_for_dante.txt file (in the repo, comments/hafsa_comments_for_dante.txt).
# you can run the Delivery Person screen by running $ python3 delivery_screen.py

# main()
