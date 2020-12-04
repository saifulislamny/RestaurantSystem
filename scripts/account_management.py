''' @authors: daniellichter, saifulislam '''
# This file is used to create, find, and delete accounts in the system

from db_handling import connect_to_db, get_cursor, save_db_changes, close_db

# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.

def create_account(username, password, type_of_user):
    '''
    username: username of user (not guaranteed to meet conditions)
    password: password of user (not guaranteed to meet conditions)
    type_of_user: account type of user (can only be 'RC', 'VC', 'C', 'D', or 'M') (not guaranteed to meet conditions)
    Output: Returns true/false after successfully inserting new account into Accounts table
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    allowed_types = ['RC','VC','C','D','M']
    # make sure username and password match the limit that is set in Account table
    # if username is 0 letters, return false (0 < len(username) <= 15)
    if(len(username) == 0):
        return False,'(0 < len(username) <= 15)'
    # if password is 0 letters, return false (0 < len(password) <= 15)
    if(len(password)==0):
        return False,'(0 < len(username) <= 15)'
    # if username is more than 15 letters, return false (0 < len(username) <= 15)
    if(len(username)>15):
        return False,'(0 < len(username) <= 15)'
    # if password is more than 15 letters, return false (0 < len(password) <= 15)
    if(len(password)>15):
        return False,'(0 < len(username) <= 15)'
    # if username already exists in table, return false
    cur.execute("Select username FROM Accounts WHERE username = '%s'" %username)
    usr = cur.fetchall()
    if(len(usr)>0): 
        return False
    # for your own understanding: type_of_user can only be one of the following things: 'RC' (registered customer), 'VC' (VIP customer), 'C' (chef), 'D' (delivery person), 'M' (manager)

    # otherwise insert a new row into Accounts table and return true
    if(type_of_user not in allowed_types):
        return False
    cur.execute("INSERT INTO Accounts(username, password, type) VALUES (%s,%s,%s)",(username,password,type_of_user))
    save_db_changes(cur,cnx)
    return True


def delete_account_as_customer(username, password):
    '''
    username: username of customer (not guaranteed to meet conditions)
    password: password of customer (not guaranteed to meet conditions)
    Output: Returns true/false after successfully deleting account in Accounts and CustomerAccounts tables
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>0 and len(username)<=15):
    # if username and password do not match a row in the Accounts and CustomerAccounts tables, return false
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND password = '%'", (username,password))
        acc_usr = cur.fetchall()
        cur.execute("SELECT username FROM CustomerAccounts WHERE username = '%s' AND password = '%'", (username,password))
        cust_acc_usr = cur.fetchall()
        if(len(acc_usr)==0 and len(cust_acc_usr)==0):
            return False

    # otherwise delete the rows in Accounts and CustomerAccounts table that matches username and password, and return true
        else:
            cur.execute("DELETE FROM CustomerAccounts WHERE username = %s" %username)
            cur.execute("DELETE FROM Accounts WHERE username = %s" %username)
            save_db_changes(cur,cnx)
            return True
    else:
        return False

def delete_account_as_manager(username): # TODO: Daniel, implement this function
    '''
    username: username of account (not guaranteed to meet conditions)
    Output: Returns true/false if account is removed from the Accounts table and all other tables
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>0 and len(username)<=15):
    # if username does not exist in the Accounts table, return false
        cur.execute("SELECT username FROM Accounts WHERE username = '%s'" %username)
        acc_usr = cur.fetchall()
        if(len(acc_usr)==0):
            return False
    # otherwise delete the rows in ALL tables that have the username in any of its columns (Accounts, EmployeeAccounts (if they are an employee), CustomerAccounts (if they are a customer), Menu, MenuVotes,
    #MenuForVC, CartItems, Deliveries, Pickups, DeliveryVotes, OrderedItems, ChefComplaintsAndCompliments,
    #DeliveryComplaintsAndCompliments, DiscussionBoardForChefs, DiscussionBoardForDishes, DiscussionBoardForDeliveries)
        else:
            cur.execute("DELETE FROM Accounts WHERE username = %s" %username)
            cur.execute("DELETE FROM EmployeeAccounts WHERE username = %s" %username)
            cur.execute("DELETE FROM CustomerAccounts WHERE username = %s" %username)
            cur.execute("DELETE FROM Menu WHERE chef_username = %s" %username)
            cur.execute("DELETE FROM MenuVotes WHERE username = %s" %username)
            cur.execute("DELETE FROM CartItems WHERE cust_username = %s" %username)
            cur.execute("DELETE FROM Deliveries WHERE cust_username = %s" %username)
            cur.execute("DELETE FROM Pickups WHERE cust_username = %s" %username)
            cur.execute("DELETE FROM OrderedItems WHERE cust_username = %s" %username)
            cur.execute("DELETE FROM ChefComplaintsAndCompliments WHERE chef_username = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DeliveryComplaintsAndCompliments WHERE delivery_username = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DiscussionBoardForChefs WHERE chef_username = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DiscussionBoardForDishes WHERE username = %s" %username)
            cur.execute("DELETE FROM DiscussionBoardForDelivery WHERE delivery_username = %s or cust_username = %s", (username,username))
            save_db_changes(cur,cnx)
            #may have to do some conditions depending on SQL syntax


    # keep this comment for later: TODO: if new tables are created in the future, then deal with the table here as well
