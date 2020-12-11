''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
from all_user_operations import view_menu
from chef_operations import add_keyword, create_menu_item, delete_menu_item, view_menu_ratings_of_chef
from discussion_board_operations import view_discussion_boards


# def main():
#     root = tk.Tk()
#     app = ChefScreen(root,"byrdeman")

#class to show what appears on the main screen of "Chef"
class ChefScreen:
    def __init__(self,master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.85, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        chefLabel = tk.Label(frame, text="Chef", font=('Times New Roman', 20), bg="white")
        chefLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        dishRatingButton = tk.Button(frame, text="View Personal Dish Ratings", bg='white', font=('Times New Roman', 10), borderwidth=2, command=self.dish_rating_window)
        dishRatingButton.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.1)

        viewCompButton = tk.Button(frame, text="View Compliments/Complaints", bg='white', font=('Times New Roman', 10), borderwidth=2, command=self.view_comp_window)
        viewCompButton.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menu_window)
        menuButton.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.1)

        addDescButton = tk.Button(frame, text="Add food \ndescription/keyword", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.add_desc_window)
        addDescButton.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

        DiscussionBoardButton = tk.Button(frame, text="Discussion Board", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.disc_board_window)
        DiscussionBoardButton.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to open dish rating window
    def dish_rating_window(self):
        self.app = DishRatingWindow(self.root,self.user)
# function to open dish rating window
    def view_comp_window(self):
        self.app = ViewCompWindow(self.root,self.user)
# function to open food menu window
    def menu_window(self):
        self.app = MenuWindow(self.root,self.user)
# function to open add food description window
    def add_desc_window(self):
        self.app = AddDescWindow(self.root,self.user)
# function to open discussion board window
    def disc_board_window(self):
        self.app = DiscussionBoardScreen(self.root,self.user)

#class to show what appears after "View Personal Dish Ratings" button pressed
class DishRatingWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        dishRatingLabel = tk.Label(frame, text="You chose to view dish ratings!", font=('Times New Roman', 16), bg="#e6e6e6")
        dishRatingLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        
        
        uSeR_nAmE_label = tk.Label(frame, text="Enter username:", font=('Times New Roman', 16), bg="#e6e6e6")
        uSeR_nAmE_label.place(rely=0.2)

        uSeR_nAmE_entry = tk.Entry(frame)
        uSeR_nAmE_entry.place(relx=0.25, rely=0.2)
        uSeR_nAmE_entry.focus_set()

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = ChefScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        
class ViewCompWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        compLabel = tk.Label(frame, text="You chose to view \ncompliments/complaints!", font=('Times New Roman', 16), bg="#e6e6e6")
        compLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)
        
        chef_username_label = tk.Label(frame, text="Enter username:", font=('Times New Roman', 16), bg="#e6e6e6")
        chef_username_label.place(rely=0.35)

        chef_username_entry = tk.Entry(frame)
        chef_username_entry.place(relx=0.4, rely=0.35)
        chef_username_entry.focus_set()

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = ChefScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

    
class MenuWindow:
    
    def menu_add_successful(self, item_name, description, price, frame):
        if create_menu_item(item_name, self.user, description, price) == True:
            success = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            success.place(relx=0.5, rely=0.4)
        else:
            unsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            unsuccessful.place(relx=0.5, rely=0.4)

    def delete_item_successful(self, item_delete, frame):
        if delete_menu_item(item_delete) == True:
            Success = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            Success.place(relx=0.5, rely=0.5)
        else:
            Unsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            Unsuccessful.place(relx=0.5, rely=0.6)


    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=950, width=900)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.85, relheight=0.8)
        self.root.geometry("700x700")

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 16), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)


        item_name_label = tk.Label(frame, text="Create item name:", font=('Times New Roman', 16), bg="#e6e6e6")
        item_name_label.place(rely=0.2)

        item_name_entry = tk.Entry(frame)
        item_name_entry.place(relx=0.4, rely=0.2)
        item_name_entry.focus_set()


        description_label = tk.Label(frame, text="Add description:", font=('Times New Roman', 16), bg="#e6e6e6")
        description_label.place(relx=0.6, rely=0.2)

        description_entry = tk.Entry(frame)
        description_entry.place(relx=0.8, rely=0.2)
        description_entry.focus_set()
        
        price_label = tk.Label(frame, text="Price:", font=('Times New Roman', 16), bg="#e6e6e6")
        price_label.place(rely=0.3)

        price_entry = tk.Entry(frame)
        price_entry.place(relx=0.2, rely=0.3)
        price_entry.focus_set()

        add_item_button = tk.Button(frame, text="Add menu item", command=lambda: self.menu_add_successful(item_name_entry.get(),description_entry.get(), price_entry.get(), frame), font=('Times New Roman', 16), bg="#e6e6e6")
        add_item_button.place(rely=0.4)


        item_delete_label = tk.Label(frame, text="Delete item name:", font=('Times New Roman', 16), bg="#e6e6e6")
        item_delete_label.place(rely=0.5)


        item_delete_entry = tk.Entry(frame)
        item_delete_entry.place(relx=0.18, rely=0.5)
        item_delete_entry.focus_set()


        delete_item_button = tk.Button(frame, text="Delete item", command=lambda: self.delete_item_successful(item_delete_entry.get(),frame), font=('Times New Roman', 16), bg="#e6e6e6")
        delete_item_button.place(rely=0.6)


        #menu = ''.join(view_menu())
        menu_label = tk.Label(frame, text=str(view_menu()), font=('Times New Roman', 16), bg="#e6e6e6")
        menu_label.place(rely=0.67)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = ChefScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        
class AddDescWindow:
    def keyword_add_successful(self, menu_item, keyword, frame):
        if add_keyword(menu_item, keyword) == True:
            success = tk.Label(frame, text="Successful", font=('Times New Roman', 16), bg="#e6e6e6")
            success.place(rely=0.5)
        else:
            unsuccessful = tk.Label(frame, text="Unsuccessful", font=('Times New Roman', 16), bg="#e6e6e6")
            unsuccessful.place(rely=0.5)

    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        addDescLabel = tk.Label(frame, text="You chose to add \ndescription/keyword!", font=('Times New Roman', 16), bg="#e6e6e6")
        addDescLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)


        menu_item_label = tk.Label(frame, text="Menu item for keyword", font=('Times New Roman', 16), bg="#e6e6e6")
        menu_item_label.place(rely=0.2)

        menu_item_entry = tk.Entry(frame)
        menu_item_entry.place(relx=0.4, rely=0.2)
        menu_item_entry.focus_set()

        instruction_label = tk.Label(frame, text="Add keyword:", font=('Times New Roman', 16), bg="#e6e6e6")
        instruction_label.place(rely=0.3)

        keyword_entry = tk.Entry(frame)
        keyword_entry.place(relx=0.25, rely=0.3)
        keyword_entry.focus_set()

        keyword_button = tk.Button(frame, text="Submit keyword", command=lambda: self.keyword_add_successful(menu_item_entry.get(),keyword_entry.get(), frame), font=('Times New Roman', 16), bg="#e6e6e6")
        keyword_button.place(rely=0.4)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = ChefScreen(self.root,self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

# class to show what appears on the main screen of "Discussion Board"
class DiscussionBoardScreen:
    def __init__(self, master, user):
        self.root = master
        self.user = user
        self.root.geometry("800x800")
        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18),borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        discussionBoardLabel = tk.Label(frame, text="Discussion Board", font=('Times New Roman', 16),bg="white")
        discussionBoardLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        textAreaLabel = tk.Label(frame, text=view_discussion_boards(), font=('Times New Roman', 12), bg="white",wraplength=250)
        textAreaLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

    # function to return to home screen
    def home_window(self):
        self.app = ChefScreen(self.root, self.user)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)



# you can run the chef screen by running $ python3 chef_screen.py

# main()
