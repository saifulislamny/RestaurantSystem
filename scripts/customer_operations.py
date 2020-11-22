# This file is used to handle operations which customers are allowed to do

def add_to_cart(username, menu_item):
    ''' Adds menu_item to username's cart through CartItems table '''
    # if the menu_item already exists in the username's cart, then update the value in the column that stores the quantity of the item (by incrementing it by 1)

def cart_total_price(username):
    ''' Returns the total of username's cart and applies a 10% discount if they are a VC '''
    # look at Accounts table to see if they are a VC
    # add the prices of all items in the cart by using information from CartItems and Menu
    # make sure to multiply price for each item in the cart by the quantity of each item in the cart

def feedback_for_chef(username_of_customer, username_of_chef, complaint_or_compliment):
    ''' 
    complaint_or_compliment has either of two values: "complaint" or "compliment"
    Returns true/false if 1 row (if username_of_customer is RC) or 2 rows (if username_of_customer is VC since counted twice twice as much) is added to ChefComplaintsAndCompliments table 
    '''
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # check if username_of_customer is RC or VC by looking at Accounts table, and return false if neither
    # make sure username_of_chef is actually a chef by looking at Accounts table, and return false if not
    # shorten compliment to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def feedback_for_delivery(username_of_customer, username_of_delivery, complaint_or_compliment):
    ''' 
    complaint_or_compliment has either of two values: "complaint" or "compliment"
    Returns true/false if 1 row (if username_of_customer is RC) or 2 rows (if username_of_customer is VC since counted twice twice as much) is added to DeliveryComplaintsAndCompliments table 
    '''
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # check if username_of_customer is RC or VC by looking at Accounts table, and return false if neither
    # make sure username_of_delivery is actually a delivery person by looking at Accounts table, and return false if not
    # shorten compliment to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def delete_cart_item(username, menu_item):
    ''' Delete row that matches username and menu_item in CartItems table '''

def make_order(username, address, delivery_or_pickup):
    ''' 
    delivery_or_pickup has either of two values: "delivery" or "pickup"
    If username does not have enough money as deposit to fulfill order, returns false.
    If username has enough money as deposit to fulfill order, adds a row to Deliveries table, adds/modfies rows to OrderedItems table, modifies row in CustomerAccounts table, possibly modifies rows in Accounts and CustomerAccounts tables, and deletes all rows that match username in CartItems table, and returns true.
    '''

    # to see if username has enough money: compare cart_total_price with deposit information from CustomerAccounts

    # if delivery_or_pickup is "delivery", add a row to Deliveries table: look at db_handling.py to see how a row in Deliveries table looks like and use the information from CartItems to make the row
    # if delivery_or_pickup is "pickup", add a row to Pickups table: look at db_handling.py to see how a row in Pickups table looks like and use the information from CartItems to make the row

    # to add/modify rows in OrderedItems: look at db_handling.py to see how a row in OrderedItems table looks like and use the information from CartItems to make the row
    # for each of username's cart items in CartItems: if the item has never been ordered before by username, insert it as a new row in OrderedItems
    # for each of username's cart items in CartItems: if the item has been ordered before by username, increment the value in the last column in OrderedItems by the quantity ordered which is found in the last column of CartItems

    # to modify row in CustomerAccounts table: increment the value in the "total spent so far" column of CustomerAccounts by cart_total_price
    # to modify row in CustomerAccounts table: increment the value in the last column by 1 since they made a new order

    # to modify rows in Accounts and CustomerAccounts: if they username is an RC (check Accounts table), and have spent more than $500 or made more than 50 orders (check CustomerAccounts table), upgrade them to VC by modifying rows in Accounts and CustomerAccounts

    # delete all rows that match username from CartItem table since all items in the cart have been dealt with accordingly and delivery order has been made

def view_cart(username):
    ''' Return a nested list of all of the username's cart items and the quantity of each item from the CartItems table (i.e. [['Water', 1], ['Soda',2]]) '''
    # remember about the column that stores the quantity of the item added to the cart

def vote_menu_item(username, menu_item, vote):
    ''' Returns true/false if the username's vote was successfully added to the MenuVotes table '''
    # remember to check that 1 <= vote <= 5, if it's not then return false
    # remember to check if the username has actually ordered the item before and not voting an item they have never ordered before by checking OrderedItems table
