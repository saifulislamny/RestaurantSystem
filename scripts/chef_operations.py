# This file is used to handle operations which chefs are allowed to do
''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db, insertBLOB
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, remove TODOs that you have already completed (leave them if you haven't completed yet)

def add_keyword(menu_item, keyword):
    ''' 
    menu_item: menu item that keyword is going to get added to (not guaranteed to match conditions)
    keyword: keyword to be added in the last column of menu_item (not guaranteed to match conditions)
    Output: Returns true/false if the keyword is successfully added to the menu_item in Menu table
    '''
    # check if menu_item exists in the table (return false if not)
    # check if keyword is already a keyword for menu_item (return false if so)
    # otherwise insert keyword (return true)
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT keywords FROM Menu WHERE item_name = 'bacon avocado burger'")
    keywords = cur.fetchall()
    if(len(keywords)==0):
       return False
    key_list = []
    for [x] in keywords:
        key_list.append(x)    
    key = key_list[0]
    get_rid = ['[',']',' ','"']
    for x in get_rid:
        key = key.replace(x, '')
    key = key.split(',')
    if(keyword in key):
        return False
    else:
        cur.execute("UPDATE Menu SET keywords = JSON_ARRAY_APPEND(keywords,'$',%s) WHERE item_name = %s", (keyword, menu_item))
        save_db_changes(cur,cnx)
        return True
    
def create_menu_item(item_name, username_of_chef, description, price): 
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
    if((len(item_name) == 0) or (len(item_name)>50)):
        return (False,'(0 < len(item_name) <= 50)')
    # if item_name is more than 50 characters, return false (0 < len(item_name) <= 50)
    # if username_of_chef does not exist in the Accounts table, return false
    cur.execute("SELECT username, type FROM Accounts WHERE username = '%s' and type = 'C'" %username_of_chef)
    usr = cur.fetchall()
    if(len(usr)==0):
        return False
    # if username_of_chef exists in the Account table, but not as a chef, return false
    # if description is more than 150 characters, return false
    if(len(description)>150):
        return False
    # if price cannot be converted to a float or error arises when converting to float, return false
    # otherwise create the menu item and return true
    cur.execute("INSERT INTO Menu(item_name, chef_username, item_desc, price, keywords) VALUES (%s,%s,%s,%s, JSON_ARRAY())", (item_name, username_of_chef, description, price))
    save_db_changes(cur,cnx)
    return True

def delete_menu_item(item_name): 
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

def update_menu_item(item_name, new_item_name, new_username_of_chef, new_description, new_price): 
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
    if(len(usr)==0):
        return False
    # if new_description is more than 150 characters, return false
    if(len(new_description)>150):
        return False
    # if new_price cannot be converted to a float or error arises when converting to float, return false
    # otherwise update the menu item and return true
    cur.execute("Update Menu SET item_name = %s, chef_username = %s, item_desc = %s, price = %s WHERE item_name = %s", (new_item_name, new_username_of_chef, new_description, new_price, item_name))
    save_db_changes(cur,cnx)
    return True

def view_menu_ratings_of_chef(username):
    '''
    username: username of chef who created the menu items (guaranteed to match conditions)
    Output: Returns string of the average rating for each menu item made by username_of_chef
    '''
    if(len(username)>15 or len(username)==0):
        return False
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT m.item_name, mv.rating FROM Menu m JOIN MenuVotes mv ON m.item_name = mv.item_name WHERE m.chef_username = '%s'" %username)
    menu_rating = cur.fetchall()
    mr_list = []
    mr_str = ''
    for x in menu_rating:
        mr_list.append(x)
    for x in mr_list:
        mr_str += (x[0]+" "+str(x[1])+"\n")
    return mr_str

