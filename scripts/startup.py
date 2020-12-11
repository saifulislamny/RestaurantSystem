# This file is used to handle what happens at application startup
''' @authors: daniellichter, saifulislam '''
import tkinter as tk
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db


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

    # function to open surfer window
def surfer_window(root):
    from scripts.surfer_screen import SurferScreen
    canvas = tk.Canvas(root, height=700, width=800)
    canvas.pack()

    frame = tk.Frame(root, bg='#e6e6e6')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    root.geometry("700x700")
    app = SurferScreen(root)


def login_screen(root): 
    canvas = tk.Canvas(root)
    canvas.pack()
    frame = tk.Frame(root, bg='#F5F5F5')
    frame.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
    root.geometry("500x500")
    username_label = tk.Label(frame, text="Username:")
    username_label.place(relx=0.3, rely=0.25, relwidth=0.15, relheight=0.07)
    username_entry = tk.Entry(frame)
    username_entry.place(relx=0.3, rely=0.35, relwidth=0.3, relheight=0.07)
    username_entry.focus_set()
    password_label = tk.Label(frame, text="Password:")
    password_label.place(relx=0.3, rely=0.45, relwidth=0.15, relheight=0.07)
    password_entry = tk.Entry(frame)
    password_entry.place(relx=0.3, rely=0.55, relwidth=0.3, relheight=0.07)
    password_entry.focus_set()
    login_button = tk.Button(frame, text="Login", bg='white',command=lambda: check_user(username_entry.get(),password_entry.get(),username_entry.get()))
    login_button.place(relx=0.4, rely=0.65, relwidth=0.1, relheight=0.07)
    surfer_button = tk.Button(frame, text="View as Surfer", bg='white',command=lambda: surfer_window(root))
    surfer_button.place(relx=0.35, rely=0.72, relwidth=0.2, relheight=0.07)

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

