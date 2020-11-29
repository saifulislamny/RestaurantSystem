import tkinter as tk
from tkinter import font

def main():
    root = tk.Tk()
    app = Window_Surfer_Screen(root)

class Window_Surfer_Screen:
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
main()