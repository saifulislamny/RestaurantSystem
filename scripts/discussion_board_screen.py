import tkinter as tk
from tkinter import font
from startup import login_screen
# TODO: Dante,
# fulfill this screen by using view_discussion_boards() from discussion_board_operations.py (if implemented already)
# this screen will be linked to the chef, delivery person, registered customer, and VIP customer screens when the button "View Discussion Board" is clicked on these screens
def main():
    root = tk.Tk()
    app = DiscussionBoardScreen(root)
def test1():
    str1 = "test"
    return str1

#class to show what appears on the main screen of "Discussion Board"
class DiscussionBoardScreen:
    def __init__(self,master):
        self.root=master
        self.root.geometry("800x800")
        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='#999999', font=('Times New Roman', 18), borderwidth=2, command=self.sign_out_window)
        signOutButton.place(relx=0.7, rely=0.05, relwidth=0.25, relheight=0.1)

        discussionBoardLabel = tk.Label(frame, text="Discussion Board", font=('Times New Roman', 20), bg="white")
        discussionBoardLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        textBox = tk.Text(frame)
        textBox.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

        #This will be one way to insert text (from function that return string) into the textbox
        textBox.insert(tk.INSERT, test1())

        self.root.mainloop()
# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)