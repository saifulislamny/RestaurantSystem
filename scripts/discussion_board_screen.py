''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen

from discussion_board_operations import view_discussion_boards

# def main():
#     root = tk.Tk()
#     app = DiscussionBoardScreen(root,"test8")

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

        discussionBoardLabel = tk.Label(frame, text="Discussion Board", font=('Times New Roman', 20), bg="white")
        discussionBoardLabel.place(relx=0.05, rely=0.05, relwidth=0.6, relheight=0.1)

        textAreaLabel = tk.Label(frame,text=view_discussion_boards(), font=('Times New Roman', 12), bg="white",wraplength=250)
        textAreaLabel.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

# function to open signout window
    def sign_out_window(self):
        self.app = login_screen(self.root)
        #self.root.mainloop()
# main()