# This file is used to handle operations which registered and VIP customers are allowed to do
''' @authors: daniellichter, saifulislam '''

from db_handling import connect_to_db, get_cursor, save_db_changes, close_db



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
        save_db_changes(cur,cnx)
        return True
    # if menu_item already exists in the username's cart, then update the value in the column that stores the quantity of the item (by incrementing it by 1), and return true
    else:
        cur.execute("UPDATE CartItems Set quantity = quantity + 1 WHERE cust_username = %s and item_name = %s",(username, menu_item))
        save_db_changes(cur,cnx)
        return True

def add_to_chef_discussion_board(customer, chef, message): # TODO: Daniel, implement this function
    '''
    customer: username of customer (guaranteed to match conditions)
    chef: username of chef that customer wants to talk about in the message (not guaranteed to match conditions)
    message: message that customer wants to add (not guaranteed to match conditions)
    Output: Returns true/false if discussion is successfully added to DiscussionBoardForChefs
    '''
    # check stuff that is not guaranteed to match conditions (return False)

    # if taboo words appear in the message...
    # if taboo words appear more than 3 times (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark whole string with ***, add to table, and return True
    # if taboo words appear 1 <= and <=3 (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark each taboo word as ***, add to table, and return True

    # otherwise add to table and return True

def add_to_menu_discussion_board(customer, menu_item, message): # TODO: Daniel, implement this function
    '''
    customer: username of customer (guaranteed to match conditions)
    menu_item: menu item that customer wants to talk about in the message (not guaranteed to match conditions)
    message: message that customer wants to add (not guaranteed to match conditions)
    Output: Returns true/false if discussion is successfully added to DiscussionBoardForDishes
    '''
    # check stuff that is not guaranteed to match conditions (return False)

    # if taboo words appear in the message...
    # if taboo words appear more than 3 times (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark whole string with ***, add to table, and return True
    # if taboo words appear 1 <= and <=3 (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark each taboo word as ***, add to table, and return True

    # otherwise add to table and return True

def add_to_delivery_discussion_board(customer, delivery_person, message): # TODO: Daniel, implement this function
    '''
    customer: username of customer (guaranteed to match conditions)
    delivery_person: username of delivery person that customer wants to talk about in the message (not guaranteed to match conditions)
    message: message that customer wants to add (not guaranteed to match conditions)
    Output: Returns true/false if discussions is successfully added to DiscussionBoardForDelivery
    '''

    # check stuff that is not guaranteed to match conditions (return False)

    # if taboo words appear in the message...
    # if taboo words appear more than 3 times (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark whole string with ***, add to table, and return True
    # if taboo words appear 1 <= and <=3 (can be the same or different taboo words), increment number of warnings for customer by 1 using give_warning() from manager_operations, mark each taboo word as ***, add to table, and return True

    # otherwise add to table and return True

def cart_total_price(username):
    '''
    username: username of customer
    Output: Returns the total of username's cart and applies a 10% discount if they are a VC
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    total_cart = 0
    # look at Accounts table to see if they are a VC and apply discount if they are
    cur.execute("SELECT type FROM Accounts WHERE username = '%s'"  %username)
    acc_type = cur.fetchone()[0]
    cur.execute("SELECT item_name, price FROM Menu")
    menu = cur.fetchall()
    menu_list = []
    for x in menu:
        menu_list.append([x[0],x[1]])
    cur.execute("SELECT item_name, quantity from CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    cart_list = []
    for x in cart:
        cart_list.append(x)
    if(acc_type == 'VC'):
        for x in cart_list:
            for y in menu_list:
                if(x[0] == y[0]):
                    total_cart+=(y[1]*.9*x[1])
    else:
        for x in cart_list:
            for y in menu_list:
                if(x[0] == y[0]):
                    total_cart+=(y[1]*x[1])
    close_db(cur,cnx)
    return total_cart

def complaints_for_customers(complainer, complained, complaint): 
    ''' 
    complainer: username of customer who made the complaint (guaranteed to match conditions)
    complained: username of customer who the complaint was made against (not guaranteed to match conditions)
    complaint: the complaint made by the complainer (not guaranteed to match conditions)
    Output: Returns true/false if the complaint is successfully added to CustomerToCustomerComplaints table
    ''' 
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT username FROM CustomerAccounts WHERE username = '%s'" %complained)
    cmpld = cur.fetchall()
    cur.exexute("SELECT type FROM Accounts WHERE username = '%s'" %complainer)
    acc_type = cur.fetchone()[0]
    if(len(cmpld)==0):
        return False
    if(len(complaint)>150):
        complaint = complaint[:150]
    if(acc_type=='RC'):
        cur.execute("INSERT INTO CustomerToCustomerComplaints VALUES (%s,%s,%s)", (complainer, complained, complaint))
    else:
        cur.execute("INSERT INTO CustomerToCustomerComplaints VALUES (%s,%s,%s)", (complainer, complained, complaint))
        cur.execute("INSERT INTO CustomerToCustomerComplaints VALUES (%s,%s,%s)", (complainer, complained, complaint))
    save_db_changes(cur,cnx)
    return True
    

def delete_cart_item(username, menu_item):
    '''
    username: username of customer (guaranteed to match conditions)
    menu_item: name of menu item that is in cart (not guaranteed to match conditions)
    Output: Returns true/false if row that matches username and menu_item is deleted successfully in CartItems table
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT item_name FROM CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    user_cart = []
    for [x] in cart:
        user_cart.append(x)
    if(menu_item in user_cart):
        cur.execute("DELETE FROM CartItems WHERE cust_username = %s AND item_name = %s", (username, menu_item))
        save_db_changes(cur,cnx)
        return True
    else:
        return False
    # if menu_item is not in cart, then return false
    # otherwise perform actions and return true

def feedback_for_chef(username_of_customer, username_of_chef, complaint_or_compliment, feedback):
    '''
    username_of_customer: username of customer who makes feedback (guaranteed to match conditions)
    username_of_chef: username of chef feedback is for (not guaranteed to match conditions)
    complaint_or_compliment: has either of two values: "complaint" or "compliment" (guaranteed to match conditions)
    feedback: description customer gives for their complaint or compliment (guaranteed to match conditions)
    Output: Returns true/false if 1 row (username_of_customer is RC) or 2 rows (username_of_customer is VC) is successfully added to ChefComplaintsAndCompliments table, and checks to see if the customer actually ordered one of the chef's items before by taking information from the OrderedItems and Menu tables 
    '''
    cnx = connect_to_db
    cur = get_cursor(cnx)
    if(len(username_of_customer)>15):
        return False
    if(len(username_of_chef)>15):
        return False
    cur.execute("SELECT cust_username FROM OrderedItems oi JOIN Menu m ON oi.item_name = m.item_name WHERE m.chef_username = %s and oi.cust_username = %s ", (username_of_chef, username_of_customer))
    ord = cur.fetchall()
    if (len(ord)==0):
        return False
    cur.execute("SELECT username FROM Accounts WHERE type = 'C' AND username = '%s'" %username_of_chef)
    chef = cur.fetchall()
    if(len(chef)==0):
        return False
    else:
        cur.execute("SELECT type FROM Accounts WHERE username = '%s'" %username_of_customer)
        type = cur.fetchone()[0]
        if(len(feedback)>150):
            feedback = feedback[:150]
        if(type == 'RC'):
            cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_chef, username_of_customer, complaint_or_compliment, feedback))
        else:
            cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_chef, username_of_customer, complaint_or_compliment, feedback))
            cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_chef, username_of_customer, complaint_or_compliment, feedback))
        save_db_changes(cur,cnx)
        return True


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
    cur.execute("SELECT username FROM Accounts WHERE type = 'D' AND username = '%s'" %username_of_delivery)
    deliv = cur.fetchall()
    cur.exexute("SELECT type FROM Accounts WHERE username = '%s'" %username_of_customer)
    acc_type = cur.fetchone()[0]
    cur.execute("SELECT cust_username FROM Deliveries WHERE cust_username = %s AND delivery_username = %s", (username_of_customer,username_of_delivery))
    ordered = cur.fetchall()
    if(len(deliv)==0):
        return False
    elif(len(ordered)==0):
        return False
    else:
        if(len(feedback)>150):
            feedback = feedback[:150]
        if(acc_type == 'RC'):
            cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_delivery, username_of_customer, complaint_or_compliment, feedback))
        else:
            cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_delivery, username_of_customer, complaint_or_compliment, feedback))
            cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback, feedback) VALUES (%s,%s,%s,%s)", (username_of_delivery, username_of_customer, complaint_or_compliment, feedback))
        save_db_changes(cur,cnx)
        return True
    # no need to check if arguments are properly passed in for complaint_or_compliment (assume you're always given proper values for this parameter)
    # make sure username_of_delivery is actually a delivery person by looking at Accounts table, and return false if not
    # shorten feedback to fit character limit in table (150 characters)
    # otherwise perform actions and return true

def increase_deposit(customer, increment):
    ''' 
    customer: username of customer (guaranteed to match conditions)
    increment: addition added to current deposit (not guaranteed to match conditions)
    Output: Returns true/false after successfully incrementing the deposit for customer by modifying row in CustomerAccounts
    '''
    # check to see if increment is a positive number
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(increment <= 0):
        return False
    else:
        cur.execute("UPDATE CustomerAccounts SET amt_of_deposit = amt_of_deposit + %s WHERE username = %s", (increment, customer))
        save_db_changes(cur,cnx)
        return True

def make_order(username, delivery_or_pickup, address): 
    '''
    username: username of customer (guaranteed to match conditions)
    delivery_or_pickup: has either of two values: "deliver" or "pickup" (guaranteed to match conditions)
    address: address customer wants delivery sent to if they chose delivery, otherwise this would be an empty string (guaranteed to match conditions)
    Output: If username does not have enough money as deposit to fulfill order, returns false. If username has enough money as deposit to fulfill order, adds a row to Deliveries table, adds/modfies rows to OrderedItems table, modifies row in CustomerAccounts table, possibly modifies rows in Accounts and CustomerAccounts tables, and deletes all rows that match username in CartItems table, and returns true.
    '''
    cnx = connect_to_db()
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
    ord_list = []
    for [x] in ordered:
        ord_list.append(x)
    cur.execute("SELECT item_name, quantity FROM CartItems WHERE cust_username = '%s'" %username)
    cart = cur.fetchall()
    user_cart = []
    for x in cart:
        user_cart.append([x[0],x[1]])
    if(delivery_or_pickup == "delivery"):
        cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES (%s,%s,JSON_ARRAY())", (username, address))
        for x in user_cart:
            cur.execute("Update Deliveries SET items_ordered = JSON_ARRAY_APPEND(items_ordered, '$', JSON_ARRAY(%s,%s))", (x[0],x[1]))
    else:
        cur.execute("INSERT INTO Pickups(cust_username, items_ordered) VALUES ('%s',JSON_ARRAY())" %username)
        for x in user_cart:
            cur.execute("Update Pickups SET items_ordered = JSON_ARRAY_APPEND(items_ordered, '$', JSON_ARRAY(%s,%s))", (x[0],x[1]))
    # to add/modify rows in OrderedItems: look at db_handling.py to see how a row in OrderedItems table looks like and use the information from CartItems to make the row
    # for each of username's cart items in CartItems: if the item has never been ordered before by username, insert it as a new row in OrderedItems
    for x in user_cart:
        if(x[0] not in ord_list):
            cur.execute("INSERT INTO OrderedItems(cust_username, item_name, quantity) VALUES (%s,%s,%s)", (username, x[0],x[1]))
        else:
            cur.execute("UPDATE OrderedItems SET quantity = quantity + %s WHERE cust_username = %s", (x[1], username))
    
    # for each of username's cart items in CartItems: if the item has been ordered before by username, increment the value in the last column in OrderedItems by the quantity ordered which is found in the last column of CartItems

    # to modify row in CustomerAccounts table: increment the value in the "total spent so far" column of CustomerAccounts by cart_total_price
    # to modify row in CustomerAccounts table: increment the value in the last column by 1 since they made a new order
    cur.execute("UPDATE CustomerAccounts SET amt_of_deposit = amt_of_deposit - %s WHERE username = %s", (total_cart, username))
    cur.execute("Update CustomerAccounts SET total_spents = total_spents + %s WHERE username = %s", (total_cart, username))
    cur.execute("Update CustomerAccounts SET total_num_orders = total_num_orders + 1 WHERE username = '%s'" %username)
    # to modify rows in Accounts and CustomerAccounts: if they username is an RC (check Accounts table), and have spent more than $500 or made more than 50 orders (check CustomerAccounts table), upgrade them to VC by modifying rows in Accounts and CustomerAccounts
    cur.execute("SELECT total_spents FROM CustomerAccount WHERE username = '%s'" %username)
    total_spent = cur.fetchone()[0]
    cur.execute("SELECT total_num_orders FROM CustomerAccount WHERE username = '%s'" %username)
    num_orders = cur.fetchone()[0]
    if(total_spent > 500 or num_orders > 50):
        cur.execute("UPDATE Accounts SET type = 'VC' WHERE username = '%s'" %username)
    # delete all rows that match username from CartItem table since all items in the cart have been dealt with accordingly and delivery order has been made

    cur.execute("DELETE FROM CartItems WHERE cust_username = '%s'" %username)
    save_db_changes(cur,cnx)
    return True
    # return true

def quit_account_as_customer(username, password): 
    '''
    username: username of customer (not guaranteed to meet conditions)
    password: password of customer (not guaranteed to meet conditions)
    Output: Returns true/false after successfully adding row to AccountDeregistrations table
    '''
    
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>0 and len(username)<=15):
    # if username and password do not match a row in the Accounts and CustomerAccounts tables, return false
        cur.execute("SELECT username FROM Accounts WHERE username = %s AND password = %s", (username,password))
        acc_usr = cur.fetchall()
        cur.execute("SELECT username FROM CustomerAccounts WHERE username = '%s'" %username)
        cust_acc_usr = cur.fetchall()
        if(len(acc_usr)==0 or len(cust_acc_usr)==0):
            return False
        else:
            cur.execute("INSERT INTO AccountDeregistrations VALUES ('%s', 'quit')" %username)
            save_db_changes(cur,cnx)
            return True
    else:
        return False


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

def view_deposit(username):
    ''' 
    username: username of customer (guaranteed to match conditions)
    Output: Returns the deposit amount for username
    '''
    # use CustomerAccounts table
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>15):
        return False
    else:
        cur.execute("SELECT amt_of_deposit FROM CustomerAccounts WHERE username = '%s'" %username)
        dep = cur.fetchone()[0]
        return dep
        
def vote_delivery_order(customer, delivery_order_num, vote): 
    '''
    customer: username of customer who voted (guaranteed to match conditions)
    delivery_order_num: order number of delivery that customer is voting for (not guaranteed to match conditions)
    vote: vote that customer made where vote is an integer such that 1 <= vote <= 5 (not guaranteed to match conditions)
    Output: Returns true/false if the customer's vote was successfully added to the DeliveryVotes table
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    # remember to check that 1 <= vote <= 5, if it's not then return false
    if(vote < 1 or vote> 5):
        return False
    #check if the customer actually ordered from that order_num
    cur.execute("SELECT cust_username FROM Deliveries WHERE cust_username = %s and delivery_order_num = %s", (customer, delivery_order_num))
    ordered = cur.fetchall()
    if (len(ordered)==0):
        return False
    #get delivery username from Deliveries
    cur.execute("SELECT delivery_username FROM Deliveries WHERE delivery_order_num = '%s' AND delivery_username IS NOT NULL" %delivery_order_num)
    dlv = cur.fetchone()[0]

    cur.execute("SELECT cust_username FROM DeliveryVotes WHERE delivery_order_num = '%s'" %delivery_order_num)
    vot = cur.fetchone()[0]
    if(len(vot)>0):
        cur.execute("UPDATE DeliveryVotes SET rating = %s WHERE cust_username = %s AND delivery_order_num = %s", (vote, customer, delivery_order_num))
    # otherwise perform operations and return true
    else:
        cur.execute("INSERT INTO DeliveryVotes VALUES (%s,%s,%s,%s)", (delivery_order_num, dlv, vote, customer))
    save_db_changes(cur,cnx)
    return True

def vote_menu_item(username, menu_item, vote):
    '''
    username: username of customer who voted (guaranteed to match conditions)
    menu_item: name of menu item that customer voted (not guaranteed to match conditions)
    vote: vote that customer made where vote is an integer such that 1 <= vote <= 5 (not guaranteed to match conditions)
    Output: Returns true/false if the username's vote was successfully added/modified to the MenuVotes table 
    '''
    # if menu_item does not exist on menu, then return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>15):
        return False
    cur.execute("SELECT item_name FROM Menu WHERE item_name = '%s'" %menu_item)
    item = cur.fetchall()
    if(len(item)==0):
        return False
    # remember to check that 1 <= vote <= 5, if it's not then return false
    if(vote < 1 or vote> 5):
        return False
    # if the username has never ordered the item before, then return false (check by looking at OrderedItems table)


    cur.execute("SELECT item_name FROM OrderedItems WHERE cust_username = '%s'" %username)
    order = cur.fetchall()
    order_list = []
    for [x] in order:
        order_list.append(x)
    if(menu_item not in order_list):
        return False
    cur.execute("SELECT cust_username FROM MenuVotes WHERE item_name = %s AND cust_username = %s", (menu_item, username))
    vot = cur.fetchone()[0]
    if(len(vot)>0):
        cur.execute("UPDATE MenuVotes SET rating = %s WHERE item_name = %s AND cust_username = %s", (vote, menu_item, username))
    # otherwise perform operations and return true
    else:
        cur.execute("INSERT INTO MenuVotes(item_name, cust_username, rating) VALUES (%s,%s,%s)", (menu_item, username, vote))
    save_db_changes(cur,cnx)
    return True

def view_top_3_personal_dishes(username):
    '''
    username: username of customer (guaranteed to match conditions)
    Output: Returns an array of the username's top 3 dishes using the OrderedItems table 
    '''
    # take first 3 entries that appear when selecting username from the table and ordering by the quantity descending
    # if less than 3 entries appear then return as many entries as you can
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT item_name FROM OrderedItems WHERE cust_username = '%s' ORDER BY quantity desc LIMIT 3" %username)
    top_3 = cur.fetchall()
    top_3_list = []
    for [x] in top_3:
        top_3_list.append(x)
    return top_3_list

