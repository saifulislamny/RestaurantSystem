''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
from discussion_board_screen import DiscussionBoardScreen

# TODO: Dante, check these errors that I get with VSCode


def main():
    root = tk.Tk()
    app = VIPCustScreen(root)

#class to show what appears on the main screen of "VIP Customer"
class VIPCustScreen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        sign_out_button = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        sign_out_button.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        forVIPLabel = tk.Label(frame, text="VIP Customer", font=('Times New Roman', 20), bg="white")
        forVIPLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        orderButton = tk.Button(frame, text="Order Food", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.order_food_window)
        orderButton.place(relx=0.15, rely=0.3, relwidth=0.3, relheight=0.07)

        topDishesButton = tk.Button(frame, text="View Top Dishes", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.top_dish_window)
        topDishesButton.place(relx=0.15, rely=0.4, relwidth=0.3, relheight=0.07)

        vipDishesButton = tk.Button(frame, text="View VIP Dishes", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.vip_dish_window)
        vipDishesButton.place(relx=0.15, rely=0.5, relwidth=0.3, relheight=0.07)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menu_window)
        menuButton.place(relx=0.15, rely=0.6, relwidth=0.3, relheight=0.07)

        accountBalanceButton = tk.Button(frame, text="Account Balance", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.acc_bal_window)
        accountBalanceButton.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.07)

        viewCompButton = tk.Button(frame, text="View Compliments/Complaints", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.view_comp_window)
        viewCompButton.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.07)

        fileComplaintButton = tk.Button(frame, text="File Complaint", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.file_comp_window)
        fileComplaintButton.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.07)

        writeComplimentButton = tk.Button(frame, text="Write Compliment", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.write_compliment_window)
        writeComplimentButton.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.07)

        checkWarningsButton = tk.Button(frame, text="Check Warnings", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.check_warn_window)
        checkWarningsButton.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.07)

        DiscussionBoardButton = tk.Button(frame, text="Discussion Board", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.disc_board_window)
        DiscussionBoardButton.place(relx=0.6, rely=0.7, relwidth=0.3, relheight=0.07)

        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to order food in window
    def order_food_window(self):
        self.app = OrderFoodWindow(self.root)
# function to open top dishes window
    def top_dish_window(self):
        self.app = TopDishWindow(self.root)
# function to open vip dishes window
    def vip_dish_window(self):
        self.app = VipDishWindow(self.root)
# function to open view menu window
    def menu_window(self):
        self.app = MenuWindow(self.root)
# function to open view compliment/complaint window
    def view_comp_window(self):
        self.app = ViewCompWindow(self.root)
# function to open file complaint window
    def file_comp_window(self):
        self.app = FileCompWindow(self.root)
# function to open write compliment window
    def write_compliment_window(self):
        self.app = WriteComplimentWindow(self.root)
# function to open check warnings window
    def check_warn_window(self):
        self.app = CheckWarnWindow(self.root)
# function to open account balance window
    def acc_bal_window(self):
        self.app = AccBalWindow(self.root)
# function to open discussion board window
    def disc_board_window(self):
        self.app = DiscussionBoardScreen(self.root)

#class to show what appears after "Order Food" button pressed
class OrderFoodWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        dineInLabel = tk.Label(frame, text="Please pick an option below", font=('Times New Roman', 20), bg="#e6e6e6")
        dineInLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        eatAtRestButton = tk.Button(frame, text="Dine In", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.dine_in_window)
        eatAtRestButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.1)

        pickUpFoodButton = tk.Button(frame, text="Pick Up", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.pick_up_window)
        pickUpFoodButton.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.1)

        deliveryButton = tk.Button(frame, text="Delivery", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.delivery_window)
        deliveryButton.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

        self.root.mainloop()

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to open dine in window
    def dine_in_window(self):
        self.openDineInWindow = tk.Toplevel(self.root)
        self.app = DineInWindow(self.openDineInWindow)
    # function to open pick up window
    def pick_up_window(self):
        self.openPickUpWindow = tk.Toplevel(self.root)
        self.app = PickUpWindow(self.openPickUpWindow)
    # function to open delivery window
    def delivery_window(self):
        self.openDeliveryWindow = tk.Toplevel(self.root)
        self.app = DeliveryWindow(self.openDeliveryWindow)
#class to show what appears after "Dine In" button pressed
class DineInWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        dineInLabel = tk.Label(frame, text="You chose to dine in!", font=('Times New Roman', 20), bg="#e6e6e6")
        dineInLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "Pick Up" button pressed
class PickUpWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        pickUpLabel = tk.Label(frame, text="You chose to pickup food!", font=('Times New Roman', 20), bg="#e6e6e6")
        pickUpLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "Delivery" button pressed
class DeliveryWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        deliveryLabel = tk.Label(frame, text="You chose delivery!", font=('Times New Roman', 20), bg="#e6e6e6")
        deliveryLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "View Top Dishes" button pressed
class TopDishWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        topDishLabel = tk.Label(frame, text="You chose to view top dishes!", font=('Times New Roman', 20), bg="#e6e6e6")
        topDishLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.
    # TODO: Saiful, include comment for how to fulfill this window
#class to show what appears after "View VIP Dishes" button pressed
class VipDishWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        vipDishLabel = tk.Label(frame, text="You chose to view VIP dishes!", font=('Times New Roman', 20), bg="#e6e6e6")
        vipDishLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # TODO (for later):
#class to show what appears after "View Menu" button pressed
class MenuWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 16), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

# NOTE: Following 3 commented lines may be a way to insert images onto this window (For later)
        # test_img = ImageTk.PhotoImage(Image.open("[INSERT LOCATION OF PHOTO(S)]"))
        # test_img_label = tk.Label(menuframe, image=test_img)
        # test_img_label.place(relx=0.2, rely=0.4, relwidth=0.3, relheight=0.3)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

    # TODO: Dante, fulfill this window by using view_menu() from all_user_operations.py (if it's already implemented)
#class to show what appears after "View Compliment/Complaints" button pressed
class ViewCompWindow:
    def __init__(self, master):
        self.root = master
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
class FileCompWindow:
    def __init__(self, master):
        self.root = master
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
    # TODO: Dante, fulfill this window by using feedback_for_chef() and feedback_for_delivery() from customer_operations.py (if it's already implemented)
#class to show what appears after "Write Compliment" button pressed
class WriteComplimentWindow:
    def __init__(self, master):
        self.root = master
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
#class to show what appears after "Check Warnings" button pressed
class CheckWarnWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        checkWarnLabel = tk.Label(frame, text="You chose to check warnings!", font=('Times New Roman', 16), bg="#e6e6e6")
        checkWarnLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # TODO (for later):
#class to show what appears after "Account Balance" button pressed
class AccBalWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        accBalLabel = tk.Label(frame, text="You chose to check account balance!", font=('Times New Roman', 16), bg="#e6e6e6")
        accBalLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

    # TODO (for later): Dante, fulfill this window by using view_deposit() from customer_operations.py


main()

# TODO: Tanzil,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the VIP Customer screen
# let him know what buttons he has to add by specifying in the tanzil_comments_for_dante.txt file (in the repo, comments/tanzil_comments_for_dante.txt).
# you can run the VIP Customer screen by running $ python3 VIP_customer_screen.py