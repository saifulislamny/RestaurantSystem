''' @authors: dantebetancourt, saifulislam '''
import tkinter as tk
from tkinter import font
from startup import login_screen


def startUpAnimation(root):
    app = AnimationStartupScreen(root)

class AnimationStartupScreen:
    def __init__(self,master):

        canvas = tk.Canvas(master, height=500, width=800)
        canvas.pack()
        frame = tk.Frame(master, bg='#e6e6e6')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        TitleLabel = tk.Label(frame, text="", font=('Times New Roman', 24), bg="white")
        TitleLabel.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)
        TeamLabel = tk.Label(frame, text="", font=('Times New Roman', 20), bg="white")
        TeamLabel.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)

        title_string = "Food Delivery System"
        team_string = "Team X"

        #Time delay between chars appearing on screen
        delta = 150
        delay = 0
        for i in range(len(title_string) + 1) :
            oneAtATime = title_string[:i]
            update_text = lambda oneAtATime=oneAtATime: TitleLabel.config(text=oneAtATime)
            canvas.after(delay, update_text)
            delay += delta
        for j in range(len(team_string) + 1) :
            oneAtATime = team_string[:j]
            update_text = lambda oneAtATime=oneAtATime: TeamLabel.config(text=oneAtATime)
            canvas.after(delay, update_text)
            delay += delta
