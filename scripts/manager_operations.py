# This file is used to handle operations which managers are allowed to do

from account_management import delete_account_as_manager

# TODO: Daniel, specify that you and I worked on this file in the header (you had it when you gave me your first ever code, which I should have kept, my mistake)
# TODO: Daniel, you forgot to import functions here as well
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Daniel, check these errors that I get with VSCode
# TODO: Daniel, make sure your indentations are correct

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
        custReg = []
        for [x] in cust_reg:
            cust.append(x)
        if(username not in custReg):
            return False
    # otherwise:
    # add username, password, and "RC" (stands for "Registered Customer") to Accounts table by taking info from CustomerRegistrations table
        cur.execute("SELECT password, amt_of_deposit FROM CustomerRegistrations where cust_username = '%s'" %username)
        cust_inf = cur.fetchall()
        custInfo = []
        for x in cust_inf:
            custInfo.append(x)
        cur.execute("INSERT INTO Accounts(username, password, type) VALUES (%s,%s,'RC')", (username, custInfo[0][0]))
    # add username, amount of deposit, number of warnings (set to 0 since a new account) to CustomerAccounts table by taking info from CustomerRegistrations table
        cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES (%s,%s)", (username, custInfo[0][1]))
    # delete row from CustomerRegistrations table that matches username
        cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = %s" %username))
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
        if(len(a)==0):
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
                cur.execute("DELETE FROM CustomerRegistrations WHERE cust_username = %s" %username))
                save_db_changes(cur,cnx)
                return True


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

def view_customer_registrations():
    ''' Output: Returns a string of all usernames and deposit information in the CustomerRegistrations table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT cust_username, amt_of_deposit FROM CustomerRegistrations")
    custReg = cur.fetchall()
    for x in custReg:
        print(x)
