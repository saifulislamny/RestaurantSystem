# This file is used to handle operations which managers are allowed to do
''' @authors: daniellichter, saifulislam '''
from account_management import delete_account_as_manager
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
    if(len(username <=15)):
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
        cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = %s" %username)
        save_db_changes(cur,cnx)
        return True
    else:
        return False
    # return true

def close_customer_account(username):
    '''
    username: username of customer (not guaranteed to meet conditions)
    Output: Returns true/false if username's deposit is cleared and account is closed for a customer who gets kicked out or quits the system
    '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username <= 15)):

    # for this function you only have to check if the username exists in the Accounts table AS A CUSTOMER and return false if not, everything else should be fine
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('RC','VC')" %username)
        acc = cur.fetchone()[0]
        if(len(acc)==0):
            return False
        if delete_account_as_manager(username):
            return True
        else:
            return False
    else:
        return False


def close_employee_account(username):
    '''
    username: username of employee (not guaranteed to meet conditions)
    Output: Returns true/false if closing the account of a chef or delivery person is successful '''
    # make sure that the username exists as a chef or delivery person by checking Accounts table
    # if username does not exist as a chef or delivery person, then return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username <= 15)):
            cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('C','D')" %username)
            acc = cur.fetchall()
            if(len(acc)==0):
                return False
            if delete_account_as_manager(username):
                return True
            else:
                return False
    else:
        return False


    # if username exists as a chef or delivery person, then use delete_account_as_manager to delete all rows in all tables that match the username

def cut_employee_pay(username, decrement):
    '''
    username: username of employee (not guaranteed to meet conditions)
    decrement: integer value that the current pay should be deducted by (not guaranteed to meet conditions)
    Output: Returns true/false if decreasing the pay of a chef or delivery person by decrement is successful '''
    # make sure that username exists as a chef or delivery person (if not, return false)
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username <= 15)):
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('C','D')" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        cur.execute("SELECT pay FROM EmployeeAccounts WHERE username = '%s'" %username)
        pay = cur.fetchone()[0]
        if(decrement < 0 or decrement > pay):
            return False
        else:
            cur.execute("UPDATE Employee Set pay = pay - %s WHERE cust_username = %s",(pay, username))
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
    if(len(username <= 15)):
        cur.execute("SELECT cust_username FROM CustomerRegistrations WHERE cust_username = '%s'" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        else:
            cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = %s" %username)
            save_db_changes(cur,cnx)
            return True
    else:
        return False


    # if so, delete row in CustomerRegistrations and return true

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
    if(len(username <= 15)):
        cur.execute("SELECT username FROM Accounts WHERE username = '%s' AND type in ('C','D')" %username)
        acc = cur.fetchall()
        if(len(acc)==0):
            return False
        cur.execute("SELECT pay FROM EmployeeAccounts WHERE username = '%s'" %username)
        pay = cur.fetchone()[0]
        if(increment < 0):
            return False
        else:
            cur.execute("UPDATE Employee Set pay = pay + %s WHERE cust_username = %s",(pay, username))
            save_db_changes(cur,cnx)
            return True
    else:
        return False

def view_chef_complaints_and_compliments(): 
    ''' Output: Returns a string of all entries in the ChefComplaintsAndCompliments table '''
    if(len(username)>15 or len(username)==0):
        return False
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM ChefComplaintsandCompliments")
    chef_complaints = cur.fetchall()
    cc_list = []
    cc_str = ''
    for x in chef_complaints:
        cc_list.append(x)
    for x in mr_list:
        cc_str += x
    return cc_str

def view_delivery_complaints_and_compliments(): 
    ''' Output: Returns a string of all entries in the DeliveryComplaintsAndCompliments table '''
    if(len(username)>15 or len(username)==0):
        return False
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM DeliveryComplaintsandCompliments")
    delivery_complaints = cur.fetchall()
    dc_list = []
    dc_str = ''
    for x in delivery_complaints:
        dc_list.append(x)
    for x in mr_list:
        dc_str += x
    return dc_str

def view_customer_registrations():
    ''' Output: Returns a string of all usernames and deposit information in the CustomerRegistrations table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT cust_username, amt_of_deposit FROM CustomerRegistrations")
    cust_reg = cur.fetchall()
    cr_str = ''
    for x in cust_reg:
        cr_str += x
    return cr_str
        
