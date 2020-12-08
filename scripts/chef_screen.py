''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen
#from discussion_board_screen import DiscussionBoardScreen
#NOTE: Ignore Discussion Board for now (Do not click on button) because it seems to be causing problems. Will try to fix ASAP.

# TODO: Dante, check these errors that I get with VSCode

# def main():
#     root = tk.Tk()
#     app = ChefScreen(root,"test2")

#class to show what appears on the main screen of "Chef"
class ChefScreen:
    def __init__(self,master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        chefLabel = tk.Label(frame, text="Chef", font=('Times New Roman', 20), bg="white")
        chefLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        dishRatingButton = tk.Button(frame, text="View Personal Dish Ratings", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.dish_rating_window)
        dishRatingButton.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.1)

        viewCompButton = tk.Button(frame, text="View Compliments/Complaints", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.view_comp_window)
        viewCompButton.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menu_window)
        menuButton.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.1)

        addDescButton = tk.Button(frame, text="Add food \ndescription/keyword", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.add_desc_window)
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

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_menu_ratings_of_chef() from chef_operations.py (if it's already implemented)
#class to show what appears after "View Personal Dish Ratings" button pressed
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

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_menu_ratings_of_chef() from chef_operations.py (if it's already implemented)
#class to show what appears after "View Menu" button pressed
class MenuWindow:
    def __init__(self, master,user):
        self.root = master
        self.user = user
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        menuLabel = tk.Label(frame, text="You chose to open to view menu!", font=('Times New Roman', 16), bg="#e6e6e6")
        menuLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_menu() from all_user_operations.py (if it's already implemented)
#class to show what appears after "Add food description/keyword" button pressed
class AddDescWindow:
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

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, this is part of a feature where chefs create menu items. Create menu items should be the box, not what you have right now.
        # TODO: Dante, fulfill this window by using create_menu_item(), delete_menu_item(), update_menu_item() from chef_operations.py (if they are already implemented)


# TODO: Hafsa,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Chef screen
# let him know what buttons he has to add by specifying in the hafsa_comments_for_dante.txt file (in the repo, comments/hafsa_comments_for_dante.txt).
# you can run the chef screen by running $ python3 chef_screen.py

#main()