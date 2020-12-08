# This file is used to handle operations which managers are allowed to do
''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.



def accept_customer_registrations(username):
    '''
    username: username of a customer registration (not guaranteed to meet conditions)
    Output: Returns true/false if row is added to Accounts and CustomerAccounts tables with respective information from CustomerRegistrations table, and row is deleted in CustomerRegistrations table
    '''
    # if username is not in CustomerRegistrations table, return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)<=15):
        cur.execute("SELECT cust_username FROM CustomerRegistrations")
        cust_reg = cur.fetchall()
        cr_list = []
        for [x] in cust_reg:
            cr_list.append(x)
        if(username not in cr_list):
            return False
    # otherwise:
    # add username, password, and "RC" (stands for "Registered Customer") to Accounts table by taking info from CustomerRegistrations table
        cur.execute("SELECT password, amt_of_deposit FROM CustomerRegistrations where cust_username = '%s'" %username)
        cust_inf = cur.fetchall()
        ci_list = []
        for x in cust_inf:
            ci_list.append(x)
        cur.execute("INSERT INTO Accounts(username, password, type) VALUES (%s,%s,'RC')", (username, ci_list[0][0]))
    # add username, amount of deposit, number of warnings (set to 0 since a new account) to CustomerAccounts table by taking info from CustomerRegistrations table
        cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES (%s,%s)", (username, ci_list[0][1]))
    # delete row from CustomerRegistrations table that matches username
        cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = '%s'" %username)
        save_db_changes(cur,cnx)
        return True
    else:
        return False
    # return true

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
            cur.execute("DELETE FROM Accounts WHERE username = '%s'" %username)
            cur.execute("DELETE FROM EmployeeAccounts WHERE username = '%s'" %username)
            cur.execute("DELETE FROM CustomerAccounts WHERE username = '%s'" %username)
            cur.execute("DELETE FROM Menu WHERE chef_username = '%s'" %username)
            cur.execute("DELETE FROM MenuVotes WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM CartItems WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM Deliveries WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM Pickups WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM OrderedItems WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM ChefComplaintsAndCompliments WHERE chef_username = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DeliveryComplaintsAndCompliments WHERE delivery_username = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DiscussionBoardForChefs WHERE chef_name = %s or cust_username = %s", (username,username))
            cur.execute("DELETE FROM DiscussionBoardForDishes WHERE cust_username = '%s'" %username)
            cur.execute("DELETE FROM DiscussionBoardForDelivery WHERE delivery_username = %s or cust_username = %s", (username,username))
            save_db_changes(cur,cnx)
            #may have to do some conditions depending on SQL syntax

    # TODO: Daniel, you may have missed some tables here, remember that we need to wipe out their existence from all tables and we need to check each column that have a username
    # keep this comment for later: TODO: if new tables are created in the future, then deal with the table here as well
    

def cut_employee_pay(username, decrement):
    '''
    username: username of employee (not guaranteed to meet conditions)
    decrement: integer value that the current pay should be deducted by (not guaranteed to meet conditions)
    Output: Returns true/false if decreasing the pay of a chef or delivery person by decrement is successful '''
    # make sure that username exists as a chef or delivery person (if not, return false)
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username) <= 15):
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('C','D')" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        cur.execute("SELECT pay FROM EmployeeAccounts WHERE username = '%s'" %username)
        pay = cur.fetchone()[0]
        if(decrement < 0 or decrement > pay):
            return False
        else:
            cur.execute("UPDATE EmployeeAccounts Set pay = pay - %s WHERE username = %s",(decrement, username))
            save_db_changes(cur,cnx)
            return True
    else:
        return False
    # make sure that decrement is a positive number that is not greater than the current pay (otherwise return false)
    # othewise change row in EmployeeAccounts and return true

def decline_customer_registrations(username):
    '''
    username: username of customer registration (not guaranteed to meet conditions)
    Output: Returns true/false if row in CustomerRegistrations table associated with username is deleted successfully
    '''
    # if username does not exist in the CustomerRegistrations table, return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username) <= 15):
        cur.execute("SELECT cust_username FROM CustomerRegistrations WHERE cust_username = '%s'" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        else:
            cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = '%s'" %username)
            save_db_changes(cur,cnx)
            return True
    else:
        return False


    # if so, delete row in CustomerRegistrations and return true

def give_warning(username): # TODO: Daniel, implement this function
    '''
    username: username of a registered customer, VIP customer, chef, or delivery person (not guaranteed to match conditions)
    Output: Returns true/false if incrementing number of warnings is successful in respective CustomerAccounts or EmployeeAccounts table for username depending on what type of user they are
    '''
    # use Accounts, CustomerAccounts, and EmployeeAccounts to fulfill this function's implementation (but you must check if the username exists first as an RC, VC, C, or D)
    # increment number of warnings in either CustomerAccounts or EmployeeAccounts

    # after incrementing, check the number of warnings they now have
    # if username is a registered customer having 3 warnings, deregister/kick them by adding row to AccountrDeregistrations which the manager will later approve
    # or if the username is a VIP customer having 2 warnings, put them back to being a registered customer (with warnings set back to 0) by updating rows in Accounts and CustomerAccounts

def raise_employee_pay(username, increment):
    '''
    username: username of employee (not guaranteed to meet conditions)
    decrement: integer value that the current pay should be incremented by (not guaranteed to meet conditions)
    Output: Returns true/false if username's pay is successfully incremented
    '''
    # make sure that username exists as a chef or delivery person (if not, return false)
    # make sure that increment is a positive number (otherwise return false)
    # otherwise change row in EmployeeAccounts and return true
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username) <= 15):
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('C','D')" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        if(increment < 0):
            return False
        else:
            cur.execute("UPDATE EmployeeAccounts Set pay = pay + %s WHERE username = %s",(increment, username))
            save_db_changes(cur,cnx)
            return True
    else:
        return False

def view_customer_complaints_by_customers(): # TODO: Daniel, implement this function
    ''' Output: Returns a string of all entries in the CustomerToCustomerComplaints table '''


def view_chef_complaints_and_compliments(): 
    ''' Output: Returns a string of all entries in the ChefComplaintsAndCompliments table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM ChefComplaintsAndCompliments")
    chef_complaints = cur.fetchall()
    cc_list = []
    cc_str = ''
    for x in chef_complaints:
        cc_list.append(x)
    for x in cc_list:
        cc_str += (x[0]+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    return cc_str

def view_delivery_complaints_and_compliments(): 
    ''' Output: Returns a string of all entries in the DeliveryComplaintsAndCompliments table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM DeliveryComplaintsAndCompliments")
    delivery_complaints = cur.fetchall()
    dc_list = []
    dc_str = ''
    for x in delivery_complaints:
        dc_list.append(x)
    for x in dc_list:
        dc_str += (x[0]+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    return dc_str

def view_customer_registrations():
    ''' Output: Returns a string of all usernames and deposit information in the CustomerRegistrations table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT cust_username, amt_of_deposit FROM CustomerRegistrations")
    cust_reg = cur.fetchall()
    cr_str = ''
    for x in cust_reg:
        cr_str += (x[0]+" "+str(x[1])+"\n")
    return cr_str

def view_customer_deregistrations(): # TODO: Daniel, implement this function
    ''' Output: Returns a string of all usernames and their reason for leaving the system in the CustomerDeregistrations table '''

print(view_customer_registrations())