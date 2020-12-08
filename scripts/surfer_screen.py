''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen

# TODO: Dante, check these errors that I get with VSCode

def main():
    root = tk.Tk()
    app = SurferScreen(root)

#class to show what appears on the main screen for "Surfers"
class SurferScreen:
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        forSurferLabel = tk.Label(frame, text="New Customer/Surfer", font=('Times New Roman', 20), bg="white")
        forSurferLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        top3popDishesButton = tk.Button(frame, text="View Top 3 Popular Dishes", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.top_pop_dishes_window)
        top3popDishesButton.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.1)

        top3ratedDishesButton = tk.Button(frame, text="View Top 3 Highest \nRated Dishes", bg='white', font=('Times New Roman', 12), borderwidth=2, command=self.top_rated_dishes_window)
        top3ratedDishesButton.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

        menuButton = tk.Button(frame, text="View Menu", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.menu_window)
        menuButton.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.1)

        ratingsButton = tk.Button(frame, text="View Ratings", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.ratings_window)
        ratingsButton.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.1)

        signUpButton = tk.Button(frame, text="Sign Up", bg='white', font=('Times New Roman', 14), borderwidth=2, command=self.sign_up_window)
        signUpButton.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)


        self.root.mainloop()

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
# function to open top popular dishes window
    def top_pop_dishes_window(self):
        self.app = TopPopularDishesWindow(self.root)
# function to open top rated dishes window
    def top_rated_dishes_window(self):
        self.app = TopRatedDishesWindow(self.root)
# function to open food menu window
    def menu_window(self):
        self.app = MenuWindow(self.root)
# function to open food menu window
    def ratings_window(self):
        self.app = RatingsWindow(self.root)
# function to open sign up window
    def sign_up_window(self):
        self.app = SignUpWindow(self.root)

#class to show what appears after "View Top 3 Popular Dishes" button pressed
class TopPopularDishesWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        topPopDishesLabel = tk.Label(frame, text="You chose to view top 3 \npopular dishes!", font=('Times New Roman', 16), bg="#e6e6e6")
        topPopDishesLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.
        # TODO: Saiful, include comment for how to fulfill this window
#class to show what appears after "View Top 3 Highest Rated Dishes" button pressed
class TopRatedDishesWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        topRatedDishesLabel = tk.Label(frame, text="You chose to view top 3 \nrated dishes!", font=('Times New Roman', 16), bg="#e6e6e6")
        topRatedDishesLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, you already made a similar window for this, remember? Maybe that info help can be helpful so that you don't have to recreate things.

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

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using view_menu() from all_user_operations.py (if it's already implemented)
#class to show what appears after "Sign Up" button pressed
class RatingsWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        ratingsLabel = tk.Label(frame, text="You chose to open to view ratings!", font=('Times New Roman', 16), bg="#e6e6e6")
        ratingsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "Sign Up" button pressed
class SignUpWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        infoFrame = tk.Frame(frame, bg='#d9d9d9')
        infoFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.75)

        signUpLabel = tk.Label(frame, text="Enter Information", font=('Times New Roman', 16), bg="#e6e6e6")
        signUpLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        userNameLabel = tk.Label(infoFrame, text="Enter Username", font=('Times New Roman', 12), bg="#d9d9d9")
        userNameLabel.place(relx=0.06, rely=0.15, relwidth=0.3, relheight=0.05)
        userNameText = tk.Text(infoFrame, width=30, height=30)
        userNameText.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.05)
        getUsernameButton = tk.Button(infoFrame, text="Confirm",bg='#cccccc',borderwidth=2)
        getUsernameButton.place(relx=0.65, rely=0.2, relwidth=0.12, relheight=0.05)

        passWordLabel = tk.Label(infoFrame, text="Enter Password", font=('Times New Roman', 12), bg="#d9d9d9")
        passWordLabel.place(relx=0.06, rely=0.45, relwidth=0.3, relheight=0.05)
        passWordText = tk.Text(infoFrame, width=30, height=30)
        passWordText.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.05)
        getPasswordButton = tk.Button(infoFrame, text="Confirm",bg='#cccccc',borderwidth=2)
        getPasswordButton.place(relx=0.65, rely=0.5, relwidth=0.12, relheight=0.05)

        depositLabel = tk.Label(infoFrame, text="Enter Deposit Amount", font=('Times New Roman', 12), bg="#d9d9d9")
        depositLabel.place(relx=0.08, rely=0.75, relwidth=0.35, relheight=0.05)
        depositText = tk.Text(infoFrame, width=30, height=30)
        depositText.place(relx=0.1, rely=0.8, relwidth=0.5, relheight=0.05)
        getDepositButton = tk.Button(infoFrame, text="Confirm",bg='#cccccc',borderwidth=2)
        getDepositButton.place(relx=0.65, rely=0.8, relwidth=0.12, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)

        # TODO: Dante, fulfill this window by using surfer_apply_for_registered_customer() from surfer_operations.py (if it's already implemented)

main()

# TODO: Hafsa,
# look through the specifications.docx (in the repo) from start to end, and identify all the buttons that Dante missed out on for the Surfer screen
# let him know what buttons he has to add by specifying in the hafsa_comments_for_dante.txt file (in the repo, comments/hafsa_comments_for_dante.txt).
# you can run the Surfer screen by running $ python3 surfer_screen.py