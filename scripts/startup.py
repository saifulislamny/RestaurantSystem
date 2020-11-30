# This file is used to handle what happens at application startup

import tkinter as tk

def verify_login_details(username, password): # TODO: Daniel, implement this function
    ''' Returns true/false if the login information is registered on the system by checking Accounts table ''' 
        cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT username, password WHERE username = %s and password = %s", (username, password))
    login = cur.fetchall()
    close_db(cur,cnx)
    if(len(login) == 0):
        return False
    else:
        return True

def find_user_type(username):
    #SQL Statement that gets the type, set to a variable and return that variable
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT type FROM Accounts WHERE username = '%s'" %username)
    usrType = cur.fetchone()[0]
    return usrType

def login_screen(root): # TODO: implement this function
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
