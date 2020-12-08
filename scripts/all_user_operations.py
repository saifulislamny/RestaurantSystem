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


def search_menu(keyword): # TODO: Daniel, implement this function (use previous function to help you but delete it after you're done, we don't need it anymore)
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items on system that match the keyword '''
    # essentially: visually show all rows in the Menu DB where the keyword is in the array/JSON of the last column of Menu 

def view_menu():
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items in Menu table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # essentially: visually show all rows in the Menu table
    cur.execute("SELECT * FROM Menu")
    menu = cur.fetchall()
    menu_list = []
    #menu_str = ''
    for x in menu:
        imagefile = byte_to_imagefile(x[1])
        menu_list.append([x[0],imagefile, x[2], x[3], x[4]])
    return menu_list
    #all images are ready to be outputted using tkinter, their values are in x[1] 
    #for x in menu_list:
     #   menu_str += (x[0]+x[1]+x[2]+x[3]+x[4]+'\n\n')
    #return menu_str

def view_my_complaints(username): # TODO: Daniel, implement this function
    '''
    username: username of any user on the system (guaranteed to match conditions)
    Output: Returns a string of username's complaints 
    ''' 
    # first you have to figure out what type of user they are by looking at Accounts table
    # once you figure out what type of user they are look in the respective tables (CustomerToCustomerComplaints, ChefComplaintsAndCompliments, DeliveryComplaintsAndCompliments, and other complaint tables that may exist)
    # TODO (for later): we might add more complaint tables in the future so deal with them here as well

print(search_menu('Pizza'))