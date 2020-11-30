# This file is used to handle operations which registered and VIP customers are allowed to do

def add_to_cart(username, menu_item):
    '''
    username: username of customer
    menu_item: name of item (not guaranteed to match conditions)
    Output: Returns true/false if menu_item is successfully added to username's cart in CartItems table
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # if menu_item is not in the Menu table, then return false
    cur.execute("SELECT item_name FROM Menu")
    menu = []
    items = cur.fetchall()
    for [x] in items:
        menu.append(x)
    if(menu_item not in menu):
        return False


    # if menu_item does not exist in the username's cart, then insert as new row in CartItems table
    cur.execute("SELECT item_name FROM CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    user_cart = []
    for [x] in cart:
        user_cart.append(x)
    if(menu_item not in user_cart):
        cur.execute("INSERT INTO CartItems(cust_username, item_name) VALUES (%s,%s)", (username, menu_item))
    # if menu_item already exists in the username's cart, then update the value in the column that stores the quantity of the item (by incrementing it by 1), and return true
    else:
        cur.execute("UPDATE CartItems Set quantity = quantity + 1 WHERE cust_username = %s and item_name = %s",(username, menu_item))
    save_db_changes()
    return True

def cart_total_price(username):
    '''
    username: username of customer
    Output: Returns the total of username's cart and applies a 10% discount if they are a VC
    '''
    cnx = connect_to_db
    cur = get_cursor(cnx)
    total_cart = 0
    # look at Accounts table to see if they are a VC and apply discount if they are
    cur.execute("SELECT type FROM Accounts WHERE username = '%s'"  %username)
    accType = cur.fetchone()[0]
    cur.execute("SELECT item_name, price FROM Menu")
    menu = cur.fetchall()
    menuList = []
    for x in menu:
        menuList.append([x[0],x[1]])
    cur.execute("SELECT item_name, quantity from CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    cartList = []
    for x in cart:
        cartList.append(x)
    if(accType == 'VC'):
        for x in cartList:
            for y in menuList:
                if(x[0] == y[0]):
                    total_cart+=(y[1]*.9*x[1])
    else:
                for x in cartList:
                    for y in menuList:
                        if(x == y[0]):
                            total_cart+=(y[1]*x[1])
    close_db(cur,cnx)
    return total_cart
    # otherwise apply no discount
    # add the prices of all items in the cart by using information from CartItems and Menu
    # make sure to multiply price for each item in the cart by the quantity of each item in the cart

def feedback_for_chef(username_of_customer, username_of_chef, complaint_or_compliment, feedback):
    '''
    username_of_customer: username of customer who makes feedback (guaranteed to match conditions)
    username_of_chef: username of chef feedback is for (not guaranteed to match conditions)
    complaint_or_compliment: has either of two values: "complaint" or "compliment" (guaranteed to match conditions)
    feedback: description customer gives for their complaint or compliment (guaranteed to match conditions)
    Output: Returns true/false if 1 row (username_of_customer is RC) or 2 rows (username_of_customer is VC) is successfully added to ChefComplaintsAndCompliments table
    '''
    cnx = connect_to_db
    cur = get_cursor(cnx)
    if(len(username_of_customer)>15):
        return False
    if(len(username_of_chef)>15):
        return False
    cur.execute("SELECT username FROM Accounts WHERE type = 'C' AND username = '%s'" %username)
    chef = cur.fetchall()
    if(len(chef)==0):
        return False
    else:
        if(len(feedback)>150):
            feedback = feedback[:150]
        cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_chef, username_of_customer, complaint_or_compliment, feedback))
        save_db_changes(cur,cnx)
        return True
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # make sure username_of_chef is actually a chef by looking at Accounts table, and return false if not
    # shorten feedback to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def feedback_for_delivery(username_of_customer, username_of_delivery, complaint_or_compliment, feedback):
    '''
    username_of_customer: username of customer who makes feedback (guaranteed to match conditions)
    username_of_delivery: username of delivery person feedback is for (not guaranteed to match conditions)
    complaint_or_compliment has either of two values: "complaint" or "compliment" (guaranteed to match conditions)
    Output: Returns true/false if 1 row (username_of_customer is RC) or 2 rows (username_of_customer is VC) is succesfully added to DeliveryComplaintsAndCompliments table
    '''
    cnx = connect_to_db
    cur = get_cursor(cnx)
    if(len(username_of_customer)>15):
        return False
    if(len(username_of_delivery)>15):
        return False
    cur.execute("SELECT username FROM Accounts WHERE type = 'D' AND username = '%s'" %username)
    chef = cur.fetchall()
    if(len(chef)==0):
        return False
    else:
        if(len(feedback)>150):
            feedback = feedback[:150]
        cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_delivery, username_of_customer, complaint_or_compliment, feedback))
        save_db_changes(cur,cnx)
        return True
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # make sure username_of_delivery is actually a delivery person by looking at Accounts table, and return false if not
    # shorten feedback to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def delete_cart_item(username, menu_item):
    '''
    username: username of customer (guaranteed to match conditions)
    menu_item: name of menu item that is in cart (not guaranteed to match conditions)
    Output: Returns true/false if row that matches username and menu_item is deleted successfully in CartItems table
    '''
    cur = get_cursor()
    cur.execute("SELECT item_name FROM CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    user_cart = []
    for [x] in cart:
        user_cart.append(x)
    if(menu_item in user_cart):
        cur.execute("DELETE FROM CartItems WHERE cust_username = %s AND item_name = %s", (username, menu_item))
        save_db_changes()
        return True
    else:
        return False
    # if menu_item is not in cart, then return false
    # otherwise perform actions and return true

def make_order(username, delivery_or_pickup, address): # TODO: Daniel, implement this function
    '''
    username: username of customer (guaranteed to match conditions)
    delivery_or_pickup: has either of two values: "deliver" or "pickup" (guaranteed to match conditions)
    address: address customer wants delivery sent to if they chose delivery, otherwise this would be an empty string (guaranteed to match conditions)
    Output: If username does not have enough money as deposit to fulfill order, returns false. If username has enough money as deposit to fulfill order, adds a row to Deliveries table, adds/modfies rows to OrderedItems table, modifies row in CustomerAccounts table, possibly modifies rows in Accounts and CustomerAccounts tables, and deletes all rows that match username in CartItems table, and returns true.
    '''
    cnx = connect_to_db
    cur = get_cursor(cnx)
    # to see if username has enough money: compare cart_total_price with deposit information from CustomerAccounts (if not, return false)
    total_cart = cart_total_price(username)
    cur.execute("SELECT amt_of_deposit FROM CustomerAccounts where username = '%s'" %username)
    amt = cur.fetchone()[0]
    if(amt < total_cart):
        return False
    # if delivery_or_pickup is "delivery", add a row to Deliveries table: look at db_handling.py to see how a row in Deliveries table looks like and use the information from CartItems to make the row
    # if delivery_or_pickup is "pickup", add a row to Pickups table: look at db_handling.py to see how a row in Pickups table looks like and use the information from CartItems to make the row
    cur.execute("SELECT item_name FROM OrderedItems WHERE cust_username = '%s'" %username)
    ordered = cur.fetchall()
    ordList = []
    for [x] in ordered:
        ordList.append(x)
    cur.execute("SELECT item_name, quantity FROM CartItems WHERE cust_username = '%s'" %username)
        cart = cur.fetchall()
        user_cart = []
        for x in cart:
            user_cart.append([x[0],x[1]])
    if(delivery_or_pickup.equals("delivery")):
        cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES (%s,%s,JSON_ARRAY())", (username, address))
        for x in user_cart:
            cur.execute("Update Deliveries SET items_ordered = JSON_ARRAY_APPEND(items_ordered, '$', JSON_ARRAY(%s,%s))", (x[0],x[1]))


    # to add/modify rows in OrderedItems: look at db_handling.py to see how a row in OrderedItems table looks like and use the information from CartItems to make the row
    # for each of username's cart items in CartItems: if the item has never been ordered before by username, insert it as a new row in OrderedItems
    for x in user_cart:
        if(x not in ordList):
            cur.execute("INSERT INTO OrderedItems(cust_username, item_name, quanity) VALUES (%s,%s,%s)", (username, x[0],x[1]))
        else:
            cur.execute("UPDATE OrderedItems SET quanity = quantity + %s WHERE cust_username = %s", (x[1], username))
    # for each of username's cart items in CartItems: if the item has been ordered before by username, increment the value in the last column in OrderedItems by the quantity ordered which is found in the last column of CartItems

    # to modify row in CustomerAccounts table: increment the value in the "total spent so far" column of CustomerAccounts by cart_total_price
    # to modify row in CustomerAccounts table: increment the value in the last column by 1 since they made a new order
    cur.execute("Update CustomerAccounts SET total_spents = total_spents + %s WHERE username = %s", (total_cart, username))
    cur.execute("Update CustomerAccounts SET total_num_orders = total_num_orders + 1 WHERE username = '%s'" %username)
    # to modify rows in Accounts and CustomerAccounts: if they username is an RC (check Accounts table), and have spent more than $500 or made more than 50 orders (check CustomerAccounts table), upgrade them to VC by modifying rows in Accounts and CustomerAccounts
    if(total_cart > 500):
        cur.execute("UPDATE Accounts SET type = 'VC' WHERE username = '%s'" %username)
    # delete all rows that match username from CartItem table since all items in the cart have been dealt with accordingly and delivery order has been made

    cur.execute("DELETE FROM CartItems WHERE cust_username = '%s'" %username)
    save_db_changes(cur,cnx)
    return True
    # return true

def view_cart(username):
    '''
    username: username of customer (guaranteed to match conditions)
    Output: Return a nested list of all of the username's cart items and the quantity of each item from the CartItems table (i.e. [['Water', 1], ['Soda',2]])
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # remember about the column that stores the quantity of the item added to the cart
    if(len(username)<=15):
        cur.execute("SELECT item_name, quantity from CartItems WHERE cust_username = '%s'" %username)
        cart = cur.fetchall()
        cartList = []
        for x in cart:
            cartList.append(x)
        return cartList
    else:
        return False

def vote_menu_item(username, menu_item, vote):
    '''
    username: username of customer who voted (guaranteed to match conditions)
    menu_item: name of menu item that customer voted (not guaranteed to match conditions)
    vote: vote that customer made where vote is an integer such that 1 <= vote <= 5 (not guaranteed to match conditions)
    Output: Returns true/false if the username's vote was successfully added to the MenuVotes table '''
    # if menu_item does not exist on menu, then return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>15):
        return False
    cur.execute("SELECT item_name FROM Menu WHERE item_name = '%s'" %menu_item)
    item = cur.fetchall()
    if(len(item)==0):
        return False
    if(vote <= 1 or vote>=5):
        return False
    # remember to check that 1 <= vote <= 5, if it's not then return false
    if(vote <= 1 or vote>=5):
        return False
    # if the username has never ordered the item before, then return false (check by looking at OrderedItems table)
    cur.execute("SELECT item_name FROM OrderedItems WHERE cust_username = '%s'" %username)
    order = cur.fetchall()
    orderList = []
    for x in order:
        orderList.append(x)
    if(menu_item not in orderList):
        return False
    # otherwise perform operations and return true
    cur.execute("INSERT INTO MenuVotes(item_name, username, rating) VALUES (%s,%s,%s)", (menu_item, username, vote))
    close_db(cur,cnx)
