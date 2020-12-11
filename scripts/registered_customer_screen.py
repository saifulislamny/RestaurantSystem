''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
from scripts.all_user_operations import view_menu, view_my_complaints
from scripts.customer_operations import view_deposit, increase_deposit, complaints_for_customers, feedback_for_chef, \
    feedback_for_delivery, add_to_cart, delete_cart_item, cart_total_price, view_cart, make_order
from scripts.discussion_board_operations import view_discussion_boards
from scripts.surfer_operations import view_top_3_rated_dishes


def main():
    root = tk.Tk()
    app = RegisteredCustomerScreen(root,"barzy13")

#class to show what appears on the main screen of "Registered Customer"
class RegisteredCustomerScreen:
    def __init__(self,master,user):
        self.root=master
        self.user=user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        forCustLabel = tk.Label(frame, text="Registered Customer", font=('Times New Roman', 20), bg="white")
        forCustLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        warningLabel = tk.Label(frame, text="Warnings:",font=('Times New Roman', 16), bg="white")
        warningLabel.place(relx=0.05, rely=0.2, relwidth=0.3, relheight=0.07)

        orderButton = tk.Button(frame, text="Order Food", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.order_food_window)
        orderButton.place(relx=0.15, rely=0.35, relwidth=0.3, relheight=0.07)

        top3popDishesButton = tk.Button(frame, text="View Top 3 Popular Dishes", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.top_pop_dishes_window)
        top3popDishesButton.place(relx=0.15, rely=0.48, relwidth=0.3, relheight=0.07)

        top3ratedDishesButton = tk.Button(frame, text="View Top 3 Highest \nRated Dishes", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.top_rated_dishes_window)
        top3ratedDishesButton.place(relx=0.15, rely=0.61, relwidth=0.3, relheight=0.07)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menu_window)
        menuButton.place(relx=0.15, rely=0.74, relwidth=0.3, relheight=0.07)

        accountBalanceButton = tk.Button(frame, text="Account Balance", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.acc_bal_window)
        accountBalanceButton.place(relx=0.15, rely=0.87, relwidth=0.3, relheight=0.07)

        fileComplaintButton = tk.Button(frame, text="File Complaint", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.file_comp_window)
        fileComplaintButton.place(relx=0.6, rely=0.35, relwidth=0.3, relheight=0.07)

        writeComplimentButton = tk.Button(frame, text="Write Compliment", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.write_compliment_window)
        writeComplimentButton.place(relx=0.6, rely=0.48, relwidth=0.3, relheight=0.07)

        viewCompButton = tk.Button(frame, text="View Complaints", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.view_comp_window)
        viewCompButton.place(relx=0.6, rely=0.61, relwidth=0.3, relheight=0.07)

        DiscussionBoardButton = tk.Button(frame, text="Discussion Board", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.disc_board_window)
        DiscussionBoardButton.place(relx=0.6, rely=0.74, relwidth=0.3, relheight=0.07)

        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to order food in window
    def order_food_window(self):
        self.app = OrderFoodWindow(self.root,self.user)
# function to open top popular dishes window
    def top_pop_dishes_window(self):
        self.app = TopPopularDishesWindow(self.root,self.user)
# function to open top rated dishes window
    def top_rated_dishes_window(self):
        self.app = TopRatedDishesWindow(self.root,self.user)
# function to open food menu window
    def menu_window(self):
        self.app = MenuWindow(self.root,self.user)
# function to open file complaint window
    def file_comp_window(self):
        self.app = FileCompWindow(self.root,self.user)
# function to open write compliment window
    def write_compliment_window(self):
        self.app = WriteComplimentWindow(self.root,self.user)
# function to open view compliment/complaint window
    def view_comp_window(self):
        self.app = ViewCompWindow(self.root,self.user)
# function to open account balance window
    def acc_bal_window(self):
        self.app = AccBalWindow(self.root,self.user)
# function to open discussion board window
    def disc_board_window(self):
        self.app = DiscussionBoardScreen(self.root,self.user)


#class to show what appears after "Order Food" button pressed
class OrderFoodWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
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

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

        self.root.mainloop()

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root,self.user)
    # function to open dine in window
    def dine_in_window(self):
        #self.openDineInWindow = tk.Toplevel(self.root)
        self.app = DineInWindow(self.root,self.user)

    # function to open pick up window
    def pick_up_window(self):
        #self.openPickUpWindow = tk.Toplevel(self.root)
        self.app = PickUpWindow(self.root,self.user)

    # function to open delivery window
    def delivery_window(self):
        #self.openDeliveryWindow = tk.Toplevel(self.root)
        self.app = DeliveryWindow(self.root,self.user)
#class to show what appears after "Dine In" button pressed
class DineInWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        dineInLabel = tk.Label(frame, text="You chose to dine in!", font=('Times New Roman', 20), bg="#e6e6e6")
        dineInLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root,self.user)
#class to show what appears after "Pick Up" button pressed
class PickUpWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        #address is left empty because this is pickup but still needed to be passthrough
        address=""
        pickUp = "pickup"

        pickUpLabel = tk.Label(frame, text="Food Pickup", font=('Times New Roman', 20), bg="#e6e6e6")
        pickUpLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        nameLabel = tk.Label(frame, text="Enter item name:", font=('Times New Roman', 14), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.35, relheight=0.07)

        currAmount = tk.Label(frame,text="Current Balance:",font=('Times New Roman', 12), bg="#e6e6e6")
        currAmount.place(relx=0.6, rely=0.2, relwidth=0.2, relheight=0.07)
        depositAmount = tk.Label(frame, text=view_deposit(user), font=('Times New Roman', 14), bg="#e6e6e6")
        depositAmount.place(relx=0.8, rely=0.2, relwidth=0.1, relheight=0.07)

        itemNameEntry = tk.Entry(frame)
        itemNameEntry.place(relx=0.1, rely=0.3, relwidth=0.45, relheight=0.07)
        itemNameEntry.focus_set()

        addToCartButton = tk.Button(frame, text="Add to cart", font=('Times New Roman', 14), bg="#d9d9d9", borderwidth=2,command=lambda: self.add_item(user,itemNameEntry.get()))
        addToCartButton.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.07)

        deleteItemButton = tk.Button(frame, text="Remove from cart", font=('Times New Roman', 12), bg="#d9d9d9", borderwidth=2,command=lambda: self.remove_item(user,itemNameEntry.get()))
        deleteItemButton.place(relx=0.35, rely=0.4, relwidth=0.25, relheight=0.07)

        cartTotalButton = tk.Button(frame, text="Total cart price", font=('Times New Roman', 12), bg="#d9d9d9", borderwidth=2,command=lambda: self.show_total(user))
        cartTotalButton.place(relx=0.65, rely=0.4, relwidth=0.25, relheight=0.07)

        cartLabel = tk.Label(frame,text="",font=('Times New Roman', 12), bg="white")
        cartLabel.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)

        updateButton = tk.Button(frame, text="Update cart", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.update_cart(user,cartLabel))
        updateButton.place(relx=0.4, rely=0.8, relwidth=0.15, relheight=0.05)

        confirmButton = tk.Button(frame, text="Place order", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.place_order(user,pickUp,address))
        confirmButton.place(relx=0.4, rely=0.9, relwidth=0.15, relheight=0.05)



    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to open signout window
    def add_item(self,username,item):
        if add_to_cart(username,item) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Successfully added\nitem to cart")
            successLabel.pack()
        elif add_to_cart(username, item) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            failLabel = tk.Label(frame, text="Fail to add. \nCheck name of item!")
            failLabel.pack()
    def remove_item(self,username,item):
        if delete_cart_item(username,item) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Successfully removed\nitem from cart")
            successLabel.pack()
        elif delete_cart_item(username, item) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            failLabel = tk.Label(frame, text="Fail to remove. \nCheck name of item!")
            failLabel.pack()
    def show_total(self,username):
        root = tk.Tk()
        canvas = tk.Canvas(root)
        canvas.pack()
        frame = tk.Frame(root, bg='#F5F5F5')
        frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        root.geometry("200x200")
        titleLabel = tk.Label(frame, text="Total price in cart:")
        titleLabel.pack()
        totalLabel = tk.Label(frame, text=cart_total_price(username))
        totalLabel.pack()
    def update_cart(self,username,oldLabel):
        oldLabel.config(text=view_cart(username))
    def place_order(self,username,option,address):
        if make_order(username, option, address) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Successfully placed order")
            successLabel.pack()
        elif make_order(username, option, address) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            failLabel = tk.Label(frame, text="Fail to place order. \nCheck balance!")
            failLabel.pack()

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)
#class to show what appears after "Delivery" button pressed
class DeliveryWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        deliveryLabel = tk.Label(frame, text="You chose delivery!", font=('Times New Roman', 20), bg="#e6e6e6")
        deliveryLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)
#class to show what appears after "View Top 3 Popular Dishes" button pressed
class TopPopularDishesWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        topPopDishesLabel = tk.Label(frame, text="You chose to view top 3 \npopular dishes!", font=('Times New Roman', 16), bg="#e6e6e6")
        topPopDishesLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.
        # TODO: Saiful, include comment for how to fulfill this window
#class to show what appears after "View Top 3 Highest Rated Dishes" button pressed
class TopRatedDishesWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        titleLabel = tk.Label(frame, text="Top 3 Highest \nRated Dishes", font=('Times New Roman', 12), bg="#d9d9d9")
        titleLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        topRatedDishesLabel = tk.Label(frame, text=view_top_3_rated_dishes(),font=('Times New Roman', 10), bg="#d9d9d9",wraplength=250)
        topRatedDishesLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.
#class to show what appears after "View Menu" button pressed
class MenuWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()
        self.root.geometry("700x700")

        menuframe = tk.Frame(self.root, bg='#e6e6e6')
        menuframe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        titleLabel = tk.Label(menuframe, text="Menu", font=('Times New Roman', 16), bg="#d9d9d9")
        titleLabel.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.05)

        menuLabel = tk.Label(menuframe, text=view_menu(),font=('Times New Roman', 10), bg="#d9d9d9",wraplength=250)
        menuLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        signOutButton = tk.Button(menuframe, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(menuframe, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

#class to show what appears after "File Complaint" button pressed
class FileCompWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        fileCompLabel = tk.Label(frame, text="Who do you want to file complaint against?", font=('Times New Roman', 14), bg="#e6e6e6")
        fileCompLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        custButton = tk.Button(frame, text="Customer", bg='#d9d9d9', font=('Times New Roman', 16), borderwidth=2,command=self.cust_complaint_window)
        custButton.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.07)

        chefButton = tk.Button(frame, text="Chef", bg='#d9d9d9', font=('Times New Roman', 16), borderwidth=2,command=self.chef_complaint_window)
        chefButton.place(relx=0.35, rely=0.40, relwidth=0.3, relheight=0.07)

        deliveryPersonButton = tk.Button(frame, text="Delivery Person", bg='#d9d9d9', font=('Times New Roman', 16), borderwidth=2,command=self.delivery_complaint_window)
        deliveryPersonButton.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.07)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)
    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to open signout window
    def cust_complaint_window(self):
        self.app = CustComplaintWindow(self.root,self.user)
    # function to open signout window
    def chef_complaint_window(self):
        self.app = ChefComplaintWindow(self.root,self.user)
    # function to open signout window
    def delivery_complaint_window(self):
        self.app = DeliveryComplaintWindow(self.root,self.user)
#class to show what appears after "Customer" button pressed
class CustComplaintWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        nameLabel = tk.Label(frame, text="Which customer is this complaint for: ", font=('Times New Roman', 14), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)

        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.07)
        nameEntry.focus_set()

        messageLabel = tk.Label(frame, text="Complaint: ", font=('Times New Roman', 14), bg="#d9d9d9")
        messageLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.07)

        messageEntry = tk.Entry(frame)
        messageEntry.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.2)
        messageEntry.focus_set()

        confirmButton = tk.Button(frame, text="Confirm", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.confirm_complaint(user,nameEntry.get(),messageEntry.get()))
        confirmButton.place(relx=0.1, rely=0.75, relwidth=0.15, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to check if filed complaint was successful
    def confirm_complaint(self,user,toWhom,message):
        if complaints_for_customers(user,toWhom,message) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Complaint Successfully Filed!")
            successLabel.pack()
        elif complaints_for_customers(user,toWhom,message) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Complaint Failed! Try again")
            tryAgainLabel.pack()

#class to show what appears after "Chef" button pressed
class ChefComplaintWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        nameLabel = tk.Label(frame, text="Which chef is this complaint for: ", font=('Times New Roman', 14), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)

        complaint = "complaint"

        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.07)
        nameEntry.focus_set()

        messageLabel = tk.Label(frame, text="Complaint: ", font=('Times New Roman', 14), bg="#d9d9d9")
        messageLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.07)

        messageEntry = tk.Entry(frame)
        messageEntry.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.2)
        messageEntry.focus_set()

        confirmButton = tk.Button(frame, text="Confirm", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.confirm_complaint(user,nameEntry.get(),complaint,messageEntry.get()))
        confirmButton.place(relx=0.1, rely=0.75, relwidth=0.15, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to check if filed complaint was successful
    def confirm_complaint(self,user,toWhom,complaint,message):
        if feedback_for_chef(user,toWhom,complaint,message) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Complaint Successfully Filed!")
            successLabel.pack()
        elif feedback_for_chef(user,toWhom,complaint,message) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Complaint Failed! Try again")
            tryAgainLabel.pack()
#class to show what appears after "Delivery Person" button pressed
class DeliveryComplaintWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        nameLabel = tk.Label(frame, text="Which delivery person is this complaint for: ", font=('Times New Roman', 12), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)

        complaint = "complaint"

        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.07)
        nameEntry.focus_set()

        messageLabel = tk.Label(frame, text="Complaint: ", font=('Times New Roman', 14), bg="#d9d9d9")
        messageLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.07)

        messageEntry = tk.Entry(frame)
        messageEntry.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.2)
        messageEntry.focus_set()

        confirmButton = tk.Button(frame, text="Confirm", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.confirm_complaint(user,nameEntry.get(),complaint,messageEntry.get()))
        confirmButton.place(relx=0.1, rely=0.75, relwidth=0.15, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to check if filed complaint was successful
    def confirm_complaint(self,user,toWhom,complaint,message):
        if feedback_for_delivery(user,toWhom,complaint,message) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Complaint Successfully Filed!")
            successLabel.pack()
        elif feedback_for_delivery(user,toWhom,complaint,message) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Complaint Failed! Try again")
            tryAgainLabel.pack()
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

        fileCompLabel = tk.Label(frame, text="Who do you want to write compliment for?", font=('Times New Roman', 14),bg="#e6e6e6")
        fileCompLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        chefButton = tk.Button(frame, text="Chef", bg='#d9d9d9', font=('Times New Roman', 16), borderwidth=2,command=self.chef_compliment_window)
        chefButton.place(relx=0.35, rely=0.3, relwidth=0.3, relheight=0.07)

        deliveryPersonButton = tk.Button(frame, text="Delivery Person", bg='#d9d9d9', font=('Times New Roman', 16),borderwidth=2, command=self.delivery_compliment_window)
        deliveryPersonButton.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.07)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to open chef compliment window
    def chef_compliment_window(self):
        self.app = ChefComplimentWindow(self.root, self.user)
    # function to open delivery compliment window
    def delivery_compliment_window(self):
        self.app = DeliveryComplimentWindow(self.root, self.user)
#class to show what appears after "Chef" button pressed
class ChefComplimentWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        nameLabel = tk.Label(frame, text="Which chef is this compliment for: ", font=('Times New Roman', 14), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)

        compliment = "compliment"

        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.07)
        nameEntry.focus_set()

        messageLabel = tk.Label(frame, text="Compliment: ", font=('Times New Roman', 14), bg="#d9d9d9")
        messageLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.07)

        messageEntry = tk.Entry(frame)
        messageEntry.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.2)
        messageEntry.focus_set()

        confirmButton = tk.Button(frame, text="Confirm", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.confirm_compliment(user,nameEntry.get(),compliment,messageEntry.get()))
        confirmButton.place(relx=0.1, rely=0.75, relwidth=0.15, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to check if filed compliment was successful
    def confirm_compliment(self,user,toWhom,compliment,message):
        if feedback_for_chef(user,toWhom,compliment,message) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Compliment Successfully Filed!")
            successLabel.pack()
        elif feedback_for_chef(user,toWhom,compliment,message) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Compliment Failed! Try again")
            tryAgainLabel.pack()
#class to show what appears after "Delivery Person" button pressed
class DeliveryComplimentWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        nameLabel = tk.Label(frame, text="Which delivery person is this compliment for: ", font=('Times New Roman', 12), bg="#d9d9d9")
        nameLabel.place(relx=0.1, rely=0.2, relwidth=0.55, relheight=0.07)

        compliment = "compliment"

        nameEntry = tk.Entry(frame)
        nameEntry.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.07)
        nameEntry.focus_set()

        messageLabel = tk.Label(frame, text="Compliment: ", font=('Times New Roman', 14), bg="#d9d9d9")
        messageLabel.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.07)

        messageEntry = tk.Entry(frame)
        messageEntry.place(relx=0.1, rely=0.5, relwidth=0.6, relheight=0.2)
        messageEntry.focus_set()

        confirmButton = tk.Button(frame, text="Confirm", bg="#d9d9d9",font=('Times New Roman', 12), borderwidth=2,command=lambda: self.confirm_compliment(user,nameEntry.get(),compliment,messageEntry.get()))
        confirmButton.place(relx=0.1, rely=0.75, relwidth=0.15, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to check if filed compliment was successful
    def confirm_compliment(self,user,toWhom,compliment,message):
        if feedback_for_delivery(user,toWhom,compliment,message) == True :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Compliment Successfully Filed!")
            successLabel.pack()
        elif feedback_for_delivery(user,toWhom,compliment,message) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Compliment Failed! Try again")
            tryAgainLabel.pack()
#class to show what appears after "View Complaints" button pressed
class ViewCompWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        titleLabel = tk.Label(frame, text="Complaints", font=('Times New Roman', 16), bg="#d9d9d9")
        titleLabel.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.05)

        compLabel = tk.Label(frame, text=view_my_complaints(user), font=('Times New Roman', 14), bg="#d9d9d9",wraplength=250)
        compLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

#class to show what appears after "Account Balance" button pressed
class AccBalWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        accBalLabel = tk.Label(frame, text="Current balance on account: ", font=('Times New Roman', 16), bg="#e6e6e6")
        accBalLabel.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.05)

        currAmountLabel = tk.Label(frame, text=view_deposit(user), font=('Times New Roman', 14), bg="#d9d9d9")
        currAmountLabel.place(relx=0.6, rely=0.3, relwidth=0.15, relheight=0.05)

        addMoreLabel = tk.Label(frame, text="Enter amount to deposit:", font=('Times New Roman', 16), bg="#e6e6e6")
        addMoreLabel.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.05)

        depositEntry = tk.Entry(frame)
        depositEntry.place(relx=0.6, rely=0.5, relwidth=0.1, relheight=0.05)
        depositEntry.focus_set()

        confirmDepositButton = tk.Button(frame, text="+", bg='#e6e6e6', font=('Times New Roman', 18), borderwidth=2, command=lambda: self.deposit_amount(user,depositEntry.get(),currAmountLabel))
        confirmDepositButton.place(relx=0.72, rely=0.5, relwidth=0.05, relheight=0.05)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to add deposit
    def deposit_amount(self,user,amount,oldLabel):
        if increase_deposit(user, int(amount)) == True :
            oldLabel.config(text=view_deposit(user))
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            successLabel = tk.Label(frame, text="Deposit Successfully added!")
            successLabel.pack()
        elif increase_deposit(user, int(amount)) == False :
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            tryAgainLabel = tk.Label(frame, text="Invalid amount. Try again!")
            tryAgainLabel.pack()
#class to show what appears on the main screen of "Discussion Board"
class DiscussionBoardScreen:
    def __init__(self,master,user):
        self.root=master
        self.user=user
        self.root.geometry("800x800")
        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        discussionBoardLabel = tk.Label(frame, text="Discussion Board", font=('Times New Roman', 16), bg="white")
        discussionBoardLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        textAreaLabel = tk.Label(frame,text=view_discussion_boards(), font=('Times New Roman', 12), bg="white",wraplength=250)
        textAreaLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = RegisteredCustomerScreen(self.root, self.user)
# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)


# you can run the Registered Customer screen by running $ python3 registered_customer_screen.py

main()