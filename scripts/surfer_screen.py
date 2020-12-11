''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen

from all_user_operations import view_menu
from surfer_operations import surfer_apply_for_registered_customer, view_top_3_rated_dishes


# def main():
#     root = tk.Tk()
#     app = SurferScreen(root)

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

        forSurferLabel = tk.Label(frame, text="Surfer", font=('Times New Roman', 20), bg="white")
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

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = SurferScreen(self.root)

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

        titleLabel = tk.Label(frame, text="Top 3 Highest \nRated Dishes", font=('Times New Roman', 12), bg="#d9d9d9")
        titleLabel.place(relx=0.35, rely=0.1, relwidth=0.3, relheight=0.1)

        topRatedDishesLabel = tk.Label(frame, text=view_top_3_rated_dishes(),font=('Times New Roman', 10), bg="#d9d9d9",wraplength=250)
        topRatedDishesLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = SurferScreen(self.root)

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
        self.root.geometry("700x700")

        menuframe = tk.Frame(self.root, bg='#e6e6e6')
        menuframe.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        titleLabel = tk.Label(menuframe, text="Menu", font=('Times New Roman', 16), bg="#d9d9d9")
        titleLabel.place(relx=0.35, rely=0.15, relwidth=0.3, relheight=0.05)

        menuLabel = tk.Label(menuframe, text=view_menu(),font=('Times New Roman', 10), bg="#d9d9d9",wraplength=250)
        menuLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

        signOutButton = tk.Button(menuframe, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(menuframe, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = SurferScreen(self.root)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
#class to show what appears after "Sign Up" button pressed
class RatingsWindow:
    def __init__(self, master):
        self.root = master
        canvas = tk.Canvas(self.root, height=700, width=800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.root.geometry("700x700")

        ratingsLabel = tk.Label(frame, text="Ratings", font=('Times New Roman', 16), bg="#e6e6e6")
        ratingsLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2,command=self.sign_out_window)
        signOutButton.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.05)

        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2, command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
    # function to return to home screen
    def home_window(self):
        self.app = SurferScreen(self.root)

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
        backButton = tk.Button(frame, text="Home", bg="white", font=('Times New Roman', 14), borderwidth=2,command=self.home_window)
        backButton.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

        userNameLabel = tk.Label(infoFrame, text="Enter Username", font=('Times New Roman', 12), bg="#d9d9d9")
        userNameLabel.place(relx=0.06, rely=0.15, relwidth=0.3, relheight=0.05)
        userNameEntry = tk.Entry(infoFrame)
        userNameEntry.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.05)
        userNameEntry.focus_set()

        passWordLabel = tk.Label(infoFrame, text="Enter Password", font=('Times New Roman', 12), bg="#d9d9d9")
        passWordLabel.place(relx=0.06, rely=0.45, relwidth=0.3, relheight=0.05)
        passWordEntry = tk.Entry(infoFrame)
        passWordEntry.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.05)
        passWordEntry.focus_set()

        depositLabel = tk.Label(infoFrame, text="Enter Deposit Amount", font=('Times New Roman', 12), bg="#d9d9d9")
        depositLabel.place(relx=0.08, rely=0.75, relwidth=0.35, relheight=0.05)
        depositEntry = tk.Entry(infoFrame)
        depositEntry.place(relx=0.1, rely=0.8, relwidth=0.5, relheight=0.05)
        depositEntry.focus_set()

        getInfoButton = tk.Button(infoFrame, text="Confirm",bg='#cccccc',borderwidth=2,command=lambda: self.is_entries_valid(userNameEntry.get(),passWordEntry.get(),depositEntry.get()))
        getInfoButton.place(relx=0.8, rely=0.9, relwidth=0.12, relheight=0.05)

    # function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
    # function to return to home screen
    def home_window(self):
        self.app = SurferScreen(self.root)
    # function to open signout window
    def is_entries_valid(self,username,password,deposit):

        try:

            if surfer_apply_for_registered_customer(username, password, int(deposit)) == True :
                root = tk.Tk()
                canvas = tk.Canvas(root)
                canvas.pack()
                frame = tk.Frame(root, bg='#F5F5F5')
                frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
                root.geometry("200x200")
                successLabel = tk.Label(frame, text="Sign Up Successful!")
                successLabel.pack()
            elif surfer_apply_for_registered_customer(username, password, int(deposit)) == False :
                root = tk.Tk()
                canvas = tk.Canvas(root)
                canvas.pack()
                frame = tk.Frame(root, bg='#F5F5F5')
                frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
                root.geometry("200x200")
                failedLabel = tk.Label(frame, text="Sign Up Failed! Try other entries")
                failedLabel.pack()
        except ValueError:
            root = tk.Tk()
            canvas = tk.Canvas(root)
            canvas.pack()
            frame = tk.Frame(root, bg='#F5F5F5')
            frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
            root.geometry("200x200")
            failedLabel = tk.Label(frame, text="Please enter \nnumerical values \nfor deposit!")
            failedLabel.pack()

# main()

# you can run the Surfer screen by running $ python3 surfer_screen.py