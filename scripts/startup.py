import tkinter as tk

def login_screen(root):
    canvas = tk.Canvas(root)
    canvas.pack()
    frame = tk.Frame(root, bg='#F5F5F5')
    frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
    username_label = tk.Label(frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    password_label = tk.Label(frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(frame)
    password_entry.pack()
    login_button = tk.Button(frame, text="login", bg='white')
    login_button.pack()
    register_button = tk.Button(frame, text="register here", bg='white')
    register_button.pack()
    
    # TODO: organize elements above
    pass