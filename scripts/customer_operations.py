# This file is used to handle operations which registered and VIP customers are allowed to do

def add_to_cart(username, menu_item): # TODO: Daniel, implement this function
    ''' 
    username: username of customer
    menu_item: name of item (not guaranteed to match conditions)
    Output: Returns true/false if menu_item is successfully added to username's cart in CartItems table 
    '''
    # if menu_item is not in the Menu table, then return false 
    # if menu_item does not exist in the username's cart, then insert as new row in CartItems table
    # if menu_item already exists in the username's cart, then update the value in the column that stores the quantity of the item (by incrementing it by 1), and return true

def cart_total_price(username): # TODO: Daniel, implement this function
    ''' 
    username: username of customer
    Output: Returns the total of username's cart and applies a 10% discount if they are a VC 
    '''
    # look at Accounts table to see if they are a VC and apply discount if they are
    # otherwise apply no discount
    # add the prices of all items in the cart by using information from CartItems and Menu
    # make sure to multiply price for each item in the cart by the quantity of each item in the cart

def feedback_for_chef(username_of_customer, username_of_chef, complaint_or_compliment, feedback): # TODO: Daniel, implement this function
    ''' 
    username_of_customer: username of customer who makes feedback (guaranteed to match conditions)
    username_of_chef: username of chef feedback is for (not guaranteed to match conditions)
    complaint_or_compliment: has either of two values: "complaint" or "compliment" (guaranteed to match conditions)
    feedback: description customer gives for their complaint or compliment (guaranteed to match conditions)
    Output: Returns true/false if 1 row (username_of_customer is RC) or 2 rows (username_of_customer is VC) is successfully added to ChefComplaintsAndCompliments table 
    '''
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # make sure username_of_chef is actually a chef by looking at Accounts table, and return false if not
    # shorten feedback to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def feedback_for_delivery(username_of_customer, username_of_delivery, complaint_or_compliment, feedback): # TODO: Daniel, implement this function
    ''' 
    username_of_customer: username of customer who makes feedback (guaranteed to match conditions)
    username_of_delivery: username of delivery person feedback is for (not guaranteed to match conditions)
    complaint_or_compliment has either of two values: "complaint" or "compliment" (guaranteed to match conditions)
    Output: Returns true/false if 1 row (username_of_customer is RC) or 2 rows (username_of_customer is VC) is succesfully added to DeliveryComplaintsAndCompliments table 
    '''
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # make sure username_of_delivery is actually a delivery person by looking at Accounts table, and return false if not
    # shorten feedback to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def delete_cart_item(username, menu_item): # TODO: Daniel, implement this function
    ''' 
    username: username of customer (guaranteed to match conditions)
    menu_item: name of menu item that is in cart (not guaranteed to match conditions)
    Output: Returns true/false if row that matches username and menu_item is deleted successfully in CartItems table 
    '''
    # if menu_item is not in cart, then return false
    # otherwise perform actions and return true

def make_order(username, delivery_or_pickup, address): # TODO: Daniel, implement this function
    ''' 
    username: username of customer (guaranteed to match conditions)
    delivery_or_pickup: has either of two values: "deliver" or "pickup" (guaranteed to match conditions)
    address: address customer wants delivery sent to if they chose delivery, otherwise this would be an empty string (guaranteed to match conditions)
    Output: If username does not have enough money as deposit to fulfill order, returns false. If username has enough money as deposit to fulfill order, adds a row to Deliveries table, adds/modfies rows to OrderedItems table, modifies row in CustomerAccounts table, possibly modifies rows in Accounts and CustomerAccounts tables, and deletes all rows that match username in CartItems table, and returns true.
    '''

    # to see if username has enough money: compare cart_total_price with deposit information from CustomerAccounts (if not, return false)

    # if delivery_or_pickup is "delivery", add a row to Deliveries table: look at db_handling.py to see how a row in Deliveries table looks like and use the information from CartItems to make the row
    # if delivery_or_pickup is "pickup", add a row to Pickups table: look at db_handling.py to see how a row in Pickups table looks like and use the information from CartItems to make the row

    # to add/modify rows in OrderedItems: look at db_handling.py to see how a row in OrderedItems table looks like and use the information from CartItems to make the row
    # for each of username's cart items in CartItems: if the item has never been ordered before by username, insert it as a new row in OrderedItems
    # for each of username's cart items in CartItems: if the item has been ordered before by username, increment the value in the last column in OrderedItems by the quantity ordered which is found in the last column of CartItems

    # to modify row in CustomerAccounts table: increment the value in the "total spent so far" column of CustomerAccounts by cart_total_price
    # to modify row in CustomerAccounts table: increment the value in the last column by 1 since they made a new order

    # to modify rows in Accounts and CustomerAccounts: if they username is an RC (check Accounts table), and have spent more than $500 or made more than 50 orders (check CustomerAccounts table), upgrade them to VC by modifying rows in Accounts and CustomerAccounts

    # delete all rows that match username from CartItem table since all items in the cart have been dealt with accordingly and delivery order has been made
    # return true

def view_cart(username): # TODO: Daniel, implement this function
    ''' 
    username: username of customer (guaranteed to match conditions)
    Output: Return a nested list of all of the username's cart items and the quantity of each item from the CartItems table (i.e. [['Water', 1], ['Soda',2]]) 
    '''
    # remember about the column that stores the quantity of the item added to the cart

def vote_menu_item(username, menu_item, vote): # TODO: Daniel, implement this function
    ''' 
    username: username of customer who voted (guaranteed to match conditions)
    menu_item: name of menu item that customer voted (not guaranteed to match conditions)
    vote: vote that customer made where vote is an integer such that 1 <= vote <= 5 (not guaranteed to match conditions)
    Output: Returns true/false if the username's vote was successfully added to the MenuVotes table '''
    # if menu_item does not exist on menu, then return false
    # remember to check that 1 <= vote <= 5, if it's not then return false
    # if the username has never ordered the item before, then return false (check by looking at OrderedItems table)
    # otherwise perform operations and return true