import tkinter as tk
from tkinter import font

# TODO: Dante, specify that you worked on this file in the header (look at Daniel's code in db_handling.py when he adds the header)
# TODO: Dante, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Dante, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Dante, check these errors that I get with VSCode
# TODO: Dante, add in-line documentation to show what each class/function does where it may not be immediately understood

# def main():
#     root = tk.Tk()
#     app = Window_Top3_Screen(root)

class Window_Top3_Screen: # TODO: Dante, link the buttons on Registered Customers and VIP Customers screens to this window
    def __init__(self,master):
        self.root=master
        canvas = tk.Canvas(self.root, height=700, width = 800)
        canvas.pack()

        frame = tk.Frame(self.root, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        popLabel = tk.Label(frame, text="Top 3 most popular dishes", bg='white', font=('Times New Roman', 14), relief="solid")
        popLabel.place(relx=0.1, rely=0.1, relwidth=0.35, relheight=0.1)

        popFrame = tk.Frame(frame, bg="white", highlightbackground="black", highlightthickness=2)
        popFrame.place(relx=0.1, rely=0.25, relwidth=0.35, relheight=0.7)

        pop1 = tk.Message(popFrame, text="1.", bg="white", font=('Times New Roman', 16))
        pop1.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

        pop2 = tk.Message(popFrame, text="2.", bg="white", font=('Times New Roman', 16))
        pop2.place(relx=0.05, rely=0.35, relwidth=0.1, relheight=0.05)

        pop3 = tk.Message(popFrame, text="3.", bg="white", font=('Times New Roman', 16))
        pop3.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.05)

        highRatedLabel = tk.Label(frame, text="Top 3 highest rated dishes", bg="white", font=('Times New Roman', 14), relief="solid")
        highRatedLabel.place(relx=0.55, rely=0.1, relwidth=0.35, relheight=0.1)

        highRatedFrame = tk.Frame(frame, bg="white", highlightbackground="black", highlightthickness=2)
        highRatedFrame.place(relx=0.55, rely=0.25, relwidth=0.35, relheight=0.7)

        hr1 = tk.Message(highRatedFrame, text="1.", bg="white", font=('Times New Roman', 16))
        hr1.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

        hr2 = tk.Message(highRatedFrame, text="2.", bg="white", font=('Times New Roman', 16))
        hr2.place(relx=0.05, rely=0.35, relwidth=0.1, relheight=0.05)

        hr3 = tk.Message(highRatedFrame, text="3.", bg="white", font=('Times New Roman', 16))
        hr3.place(relx=0.05, rely=0.65, relwidth=0.1, relheight=0.05)

        self.root.mainloop()
# main()