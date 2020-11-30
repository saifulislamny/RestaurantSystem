# This file has features which are available for most (or all) users on the system

def search_menu(keywords): # don't worry about this method for now
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items on system that match keywords '''
    # essentially: visually show all rows in the Menu DB where the keywords are a substring of the menu item name
    # if you can't figure out how to do the image, don't worry about it for now

def view_menu(): 
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items in Menu table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # essentially: visually show all rows in the Menu table
    cur.execute("SELECT * FROM Menu")
    menu = cur.fetchall()
    menuList = []
    for x in menu:
        imageFile = byte_to_imageFile(x[1])
        menuList.append([x[0],imageFile], x[2], x[3], x[4])
    #all images are ready to be outputted using tkinter, their values are in x[1]
    # if you can't figure out how to do the image, don't worry about it for now
