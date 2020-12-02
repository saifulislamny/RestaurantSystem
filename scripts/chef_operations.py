# This file is used to handle operations which chefs are allowed to do

# TODO: Daniel, specify that you and I worked on this file in the header (you had it when you gave me your first ever code, which I should have kept, my mistake)
# TODO: Daniel, you forgot to import the functions here as well
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Daniel, check these errors that I get with VSCode
# TODO: Daniel, get rid of TODOs that you already have completed, if you have not finished them yet, it's okay to keep
# TODO: Daniel, make sure your indentations are correct
# TODO: Daniel, remove TODOs that you have already completed (leave them if you haven't completed yet)
# TODO: Daniel, there's an error when I run python3 on this file


def create_menu_item(item_name, item_image, username_of_chef, description, price): # TODO: Daniel, implement this function
    '''
    item_name: name of menu item (not guaranteed to match conditions)
    item_image: image associated with menu item
    username_of_chef: name of chef who created the menu item (not guaranteed to match conditions)
    description: description of menu item (not guaranteed to match conditions)
    price: price of menu item (not guaranteed to match conditions)
    Output: Returns true/false if new item is created in the Menu table
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # don't worry about item_image for now if it's difficult
    # if item_name already exists in the Menu table, return false
    cur.execute("SELECT item_name FROM Menu where item_name = '%s'" %item_name)
    item = cur.fetchall()
    if(len(item)>0):
        return False
    # if item_name is 0 characters, return false (0 < len(item_name) <= 50)
    if((len(item_name) == 0) or (len(item_name)>50):
        return (False,'(0 < len(item_name) <= 50)')
    # if item_name is more than 50 characters, return false (0 < len(item_name) <= 50)
    # if username_of_chef does not exist in the Accounts table, return false
    cur.execute("SELECT username, type FROM Accounts WHERE username = '%s' and type = 'C'" %username_of_chef)
    usr = cur.fetchall()
    if(len(user)==0):
        return False
    # if username_of_chef exists in the Account table, but not as a chef, return false
    # if description is more than 150 characters, return false
    if(len(description)>150):
        return False
    # if price cannot be converted to a float or error arises when converting to float, return false
    # otherwise create the menu item and return true
    insertBLOB(item_name, item_image, username_of_chef, description, price)

def delete_menu_item(item_name): # TODO: Daniel, implement this function
    '''
    item_name: name of menu item (not guaranteed to match conditions)
    Output: Returns true/false if item on the menu is deleted
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT item_name FROM Menu WHERE item_name = '%s'" %item_name)
    menu = cur.fetchall()
    if(len(menu)==0):
        return False
    else:
        cur.execute("DELETE FROM Menu WHERE item_name = '%s'" %item_name)
        save_db_changes(cur,cnx)
        return True
    # if item_name does not exist on the menu, then return false
    # otherwise delete the menu item and return true

def update_menu_item(item_name, new_item_name, new_item_image, new_username_of_chef, new_description, new_price): # TODO: Daniel, implement this function
    '''
    item_name: name of menu item (not guaranteed to match conditions)
    new_item_name: updated name of menu item (not guaranteed to match conditions)
    new_item_image: image associated with menu item
    new_username_of_chef: name of chef who created the menu item (not guaranteed to match conditions)
    new_description: description of menu item (not guaranteed to match conditions)
    new_price: price of menu item (not guaranteed to match conditions)
    Output: Returns true/false if item on the menu is altered
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # if item_name does not exist on the menu, then return false
    cur.execute("SELECT item_name FROM Menu WHERE item_name = '%s'" %item_name)
    menu = cur.fetchall()
    if(len(menu)==0):
        return False
    # don't worry about item_image for now if it's difficult
    # if new_item_name is 0 characters, return false (0 < len(new_item_name) <= 50)
    if((len(new_item_name)==0) or (len(new_item_name)>50)):
        return (False,'(0 < len(new_item_name) <= 50)')
    # if new_item_name is more than 50 characters, return false (0 < len(new_item_name) <= 50)
    # if new_username_of_chef does not exist in the Accounts table, return false
    # if new_username_of_chef exists in the Account table, but not as a chef, return false
    cur.execute("SELECT username, type FROM Accounts WHERE username = '%s' and type = 'C'" %new_username_of_chef)
    usr = cur.fetchall()
    if(len(user)==0):
        return False
    # if new_description is more than 150 characters, return false
    if(len(new_description)>150):
        return False
    # if new_price cannot be converted to a float or error arises when converting to float, return false
    # otherwise update the menu item and return true
    cur.execute("Update Menu SET item_name = %s, chef_username = %s, item_desc = %s, new_price = %s WHERE item_name = %s", (new_item_name, new_username_of_chef, new_description, new_price, item_name))
    save_db_changes(cur,cnx)

def view_menu_ratings_of_chef(username): # TODO: Daniel, implement this function
    '''
    username: username of chef who created the menu items (guaranteed to match conditions)
    Output: Returns string of the average rating for each menu item made by username_of_chef
    '''
    # use MenuVotes and Menu tables 