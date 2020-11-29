import tkinter as tk
from tkinter import font

from scripts.sign_out_screen import signOutWindow


def main():
    root = tk.Tk()
    app = Window_VIP_Cust_Screen(root)

class Window_VIP_Cust_Screen:
    def __init__(self,master):
        self.root=master

        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        signOutButton = tk.Button(frame, text="Sign Out", bg='white', font=('Times New Roman', 18), borderwidth=2, command=self.signOutWindow)
        signOutButton.place(relx=0.78, rely=0.02, relwidth=0.2, relheight=0.05)

        histLabel = tk.Label(frame, text="History of Prior Choices", bg='white', font=('Times New Roman', 20), relief="solid")
        histLabel.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.1)

        listDish = tk.Label(frame, text="3 Listing Dishes", bg="white", font=('Times New Roman', 18), relief="solid")
        listDish.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.1)

        listDishFrame = tk.Frame(frame, bg="white", highlightbackground="black", highlightthickness=2)
        listDishFrame.place(relx=0.225, rely=0.4, relwidth=0.55, relheight=0.55)

        ld1 = tk.Message(listDishFrame, text="1.", bg="white", font=('Times New Roman', 16))
        ld1.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.05)

        ld2 = tk.Message(listDishFrame, text="2.", bg="white", font=('Times New Roman', 16))
        ld2.place(relx=0.05, rely=0.4, relwidth=0.1, relheight=0.05)

        ld3 = tk.Message(listDishFrame, text="3.", bg="white", font=('Times New Roman', 16))
        ld3.place(relx=0.05, rely=0.7, relwidth=0.1, relheight=0.05)

        self.root.mainloop()
    def signOutWindow(self):
        self.openSignOutWindow = tk.Toplevel(self.root)
        self.app = signOutWindow(self.openSignOutWindow)

main()