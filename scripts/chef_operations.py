# This file is used to handle operations which chefs are allowed to do

def create_menu_item(item_name, item_image, username_of_chef, description, price): # TODO: Daniel, implement this function
    ''' 
    item_name: name of menu item (not guaranteed to match conditions)
    item_image: image associated with menu item
    username_of_chef: name of chef who created the menu item (not guaranteed to match conditions)
    description: description of menu item (not guaranteed to match conditions)
    price: price of menu item (not guaranteed to match conditions)
    Output: Returns true/false if new item is created in the Menu table 
    '''
    # don't worry about item_image for now if it's difficult
    # if item_name already exists in the Menu table, return false
    # if item_name is 0 characters, return false (0 < len(item_name) <= 50)
    # if item_name is more than 50 characters, return false (0 < len(item_name) <= 50)
    # if username_of_chef does not exist in the Accounts table, return false
    # if username_of_chef exists in the Account table, but not as a chef, return false
    # if description is more than 150 characters, return false
    # if price cannot be converted to a float or error arises when converting to float, return false
    # otherwise create the menu item and return true

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
    # if item_name does not exist on the menu, then return false
    # don't worry about item_image for now if it's difficult
    # if new_item_name is 0 characters, return false (0 < len(new_item_name) <= 50)
    # if new_item_name is more than 50 characters, return false (0 < len(new_item_name) <= 50)
    # if new_username_of_chef does not exist in the Accounts table, return false
    # if new_username_of_chef exists in the Account table, but not as a chef, return false
    # if new_description is more than 150 characters, return false
    # if new_price cannot be converted to a float or error arises when converting to float, return false
    # otherwise update the menu item and return true


def delete_menu_item(item_name): # TODO: Daniel, implement this function
    ''' 
    item_name: name of menu item (not guaranteed to match conditions)
    Output: Returns true/false if item on the menu is deleted
    ''' 
    # if item_name does not exist on the menu, then return false
    # otherwise delete the menu item and return true