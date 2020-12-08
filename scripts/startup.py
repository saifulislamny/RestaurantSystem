# This file is used to handle what happens at application startup
''' @authors: daniellichter, saifulislam '''
import tkinter as tk
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.


def verify_login_details(username, password):
    ''' Returns true/false if the login information is registered on the system by checking Accounts table ''' 
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT username, password FROM Accounts WHERE username = %s and password = %s", (username, password))
    login = cur.fetchall()
    close_db(cur,cnx)
    if(len(login) == 0):
        return False
    else:
        return True

def find_user_type(username): 
    '''Returns the type of the user from the Accounts table'''
    #SQL Statement that gets the type, set to a variable and return that variable
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT type FROM Accounts WHERE username = '%s'" %username)
    usrType = cur.fetchone()[0]
    return usrType

def login_screen(root): 
    canvas = tk.Canvas(root)
    canvas.pack()
    frame = tk.Frame(root, bg='#F5F5F5')
    frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
    root.geometry("500x500")
    username_label = tk.Label(frame, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(frame)
    username_entry.pack()
    username_entry.focus_set()
    password_label = tk.Label(frame, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(frame)
    password_entry.pack()
    password_entry.focus_set()
    login_button = tk.Button(frame, text="Login", bg='white',command=lambda: check_user(username_entry.get(),password_entry.get(),username_entry.get()))
    login_button.pack()
    surfer_button = tk.Button(frame, text="View as Surfer", bg='white') # TODO (for later): Dante, link this button the Surfer Screen
    surfer_button.pack()

    # TODO: organize elements above

def check_user(username,password,currentUser):

    if verify_login_details(username,password) == True :

        if find_user_type(username) == "RC" :
            from registered_customer_screen import RegisteredCustomerScreen
            root = tk.Tk()
            RegisteredCustomerScreen(root,currentUser)

        elif find_user_type(username) == "VC":
            from VIP_customer_screen import VIPCustScreen
            root = tk.Tk()
            VIPCustScreen(root,currentUser)

        elif find_user_type(username) == "C":
            from chef_screen import ChefScreen
            root = tk.Tk()
            ChefScreen(root,currentUser)

        elif find_user_type(username) == "D":
            from delivery_screen import DeliveryScreen
            root = tk.Tk()
            DeliveryScreen(root,currentUser)

        elif find_user_type(username) == "M":
            from manager_screen import ManagerScreen
            root = tk.Tk()
            ManagerScreen(root,currentUser)

    else :
        root = tk.Tk()
        canvas = tk.Canvas(root)
        canvas.pack()
        frame = tk.Frame(root, bg='#F5F5F5')
        frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        root.geometry("200x200")
        tryAgainLabel = tk.Label(frame, text="Bad Login! Try again")
        tryAgainLabel.pack()

