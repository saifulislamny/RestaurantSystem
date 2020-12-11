# This file has features which are available for most (or all) users on the system
''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db, byte_to_imagefile

# TODO: Saiful, rename this file later to "most_user_operations.py" (name is inconsistent)

# def search_menu(keywords): # TODO: implement this function later (don't worry about it for now)
#     ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items on system that match keywords '''
#     # essentially: visually show all rows in the Menu DB where the keywords are a substring of the menu item name
#     cnx = connect_to_db()
#     cur = get_cursor(cnx)
#     cur.execute("SELECT * FROM Menu WHERE item_name LIKE '%s'" %("%" + keywords + "%"))
#     menu = cur.fetchall()
#     menu_list = []
#     for x in menu:
#         imagefile = byte_to_imagefile(x[1])
#         menu_list.append([x[0],imagefile, x[2], x[3], x[4]])
#     return menu_list

def search_menu(keyword): 
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items on system that match the keyword '''
    # essentially: visually show all rows in the Menu DB where the keyword is in the array/JSON of the last column of Menu 
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT item_name, keywords FROM Menu")
    keywords = cur.fetchall()
    if(len(keywords)==0):
       return False
    key_list = []
    cleaned_list = []
    for x in keywords:  
        key_list.append(x)
   # print(key_list)
    menu_list = []
    for y in range(len(key_list)):
        key = key_list[y][1]
        get_rid = ['[',']',' ','"']
        for x in get_rid:
           key = key.replace(x, '')
        key = key.split(',')
        cleaned_list.append([key_list[y][0],key])
    for y in (range(len(cleaned_list))):
        if(keyword in cleaned_list[y][1]):
            print(keyword)
            print(cleaned_list[y][1])
            cur.execute("SELECT * FROM Menu WHERE item_name = '%s'" %cleaned_list[y][0])
            menu = cur.fetchall()
            for x in menu:
                imagefile = byte_to_imagefile(x[1])
                menu_list.append([x[0],imagefile, x[2], x[3], x[4]])
    return menu_list





    #if(keyword in key):
    #    return False
    #else:
    #    cur.execute("UPDATE Menu SET keywords = JSON_ARRAY_APPEND(keywords,'$',%s) WHERE item_name = %s", (keyword, menu_item))
    #    save_db_changes(cur,cnx)
    #    return True



def view_menu():
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items in Menu table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # essentially: visually show all rows in the Menu table
    cur.execute("SELECT * FROM Menu")
    menu = cur.fetchall()
    menu_list = []
    # menu_str = ''
    menu_str = 'Item name, chef name, description, and price\n'
    for x in menu:
        # imagefile = byte_to_imagefile(x[1]) # insert later
        menu_list.append([x[0], x[2], x[3], x[4]]) # image was taken away here
    # return menu_list
    #all images are ready to be outputted using tkinter, their values are in x[1] 
    for x in menu_list:
       menu_str += ("Item name: " + str(x[0])+ ", Chef name: " + str(x[1])+ ", Description:" + str(x[2])+ ", Price: " + str(x[3])+'\n\n')
    return menu_str

def view_my_complaints(username):
    '''
    username: username of any user on the system (guaranteed to match conditions)
    Output: Returns a string of username's complaints 
    ''' 
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM DeliveryComplaintsAndCompliments WHERE type_of_feedback = 'complaint' and cust_username = '%s'" %username)
    dcc = cur.fetchall()
    cur.execute("SELECT * FROM ChefComplaintsAndCompliments WHERE type_of_feedback = 'complaint' and cust_username = '%s'" %username)
    ccc = cur.fetchall()
    cur.execute("SELECT * FROM CustomerToCustomerComplaints WHERE complainer_username = '%s'" %username)
    ctcc = cur.fetchall()
    complaint_str = ''
    for x in dcc:
        complaint_str += (x[0]+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    for x in ccc:
        complaint_str += (x[0]+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    for x in ctcc:
        complaint_str += (x[0]+" "+x[1]+" "+x[2]+"\n")
    cur.close()
    cnx.close()
    return complaint_str
    # first you have to figure out what type of user they are by looking at Accounts table
    # once you figure out what type of user they are look in the respective tables (CustomerToCustomerComplaints, ChefComplaintsAndCompliments, DeliveryComplaintsAndCompliments, and other complaint tables that may exist)
    # TODO (for later): we might add more complaint tables in the future so deal with them here as well

def view_menu_ratings():
    ''' Output: Returns a string of average ratings for each menu item using the MenuVotes table'''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT item_name, rating FROM MenuVotes")
    mv = cur.fetchall()
    ratings_str = 'Ratings for each menu item:\n'
    for x in mv:
        ratings_str += (x[0]+" "+str(x[1])+"\n")
    return ratings_str

def view_my_warnings(username): 
    ''' 
    username: username of an RC, VC, chef, or delivery person (guaranteed to match conditions)
    Output: Returns the number of warnings that the username has using the Accounts, CustomerAccounts, and EmployeeAccounts tables
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT type FROM Accounts WHERE username = '%s'" %username)
    acc_type = cur.fetchone()[0]
    if(acc_type == 'RC' or acc_type == 'VC'):
        cur.execute("SELECT num_of_warnings FROM CustomerAccounts WHERE username = '%s'" %username)
        warning = cur.fetchone()[0]
    else:
        cur.execute("SELECT num_of_warnings FROM EmployeeAccounts WHERE username = '%s'" %username)
        warning = cur.fetchone()[0]
    return warning
    # have to check what type of user they are by looking at Accounts table
    # based on the type of user they are look at the respective CustomerAccounts or EmployeeAccounts table and return the number of warnings they have


