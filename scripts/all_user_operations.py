# This file has features which are available for most (or all) users on the system

# TODO: Daniel, specify that you and I worked on this file in the header (you had it when you gave me your first ever code, which I should have kept, my mistake)
# TODO: Daniel, you forgot to import functions here as well
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Daniel, check these errors that I get with VSCode
# TODO: Daniel, make sure your indentations are correct
# TODO: Daniel, remove TODOs that you have already completed (leave them if you haven't completed yet)

def search_menu(keywords): # TODO: implement this function later (don't worry about it for now)
    ''' Returns a string of name, image (using Tkinter syntax to include images), chef name, description, and price for all menu items on system that match keywords '''
    # essentially: visually show all rows in the Menu DB where the keywords are a substring of the menu item name

def view_menu(): # TODO: Daniel, implement this function
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
    
    # TODO: Daniel, you didn't return anything here
