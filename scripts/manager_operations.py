# This file is used to handle operations which managers are allowed to do

from account_management import delete_account_as_manager    

def accept_customer_registrations(username): # TODO: Daniel, implement this function
    ''' 
    username: username of a customer registration (not guaranteed to meet conditions)
    Output: Returns true/false if row is added to Accounts and CustomerAccounts tables with respective information from CustomerRegistrations table, and row is deleted in CustomerRegistrations table 
    ''' 
    # if username is not in CustomerRegistrations table, return false

    # otherwise:
    # add username, password, and "RC" (stands for "Registered Customer") to Accounts table by taking info from CustomerRegistrations table
    # add username, amount of deposit, number of warnings (set to 0 since a new account) to CustomerAccounts table by taking info from CustomerRegistrations table
    # delete row from CustomerRegistrations table that matches username
    # return true

def close_customer_account(username): # TODO: Daniel, implement this function
    ''' 
    username: username of customer (not guaranteed to meet conditions)
    Output: Returns true/false if username's deposit is cleared and account is closed for a customer who gets kicked out or quits the system 
    '''

    # for this function you only have to check if the username exists in the Accounts table AS A CUSTOMER and return false if not, everything else should be fine

    if delete_account_as_manager(username):
        return True
    else: 
        return False


def close_employee_account(username): # TODO: Daniel, implement this function
    ''' 
    username: username of employee (not guaranteed to meet conditions)
    Output: Returns true/false if closing the account of a chef or delivery person is successful '''
    # make sure that the username exists as a chef or delivery person by checking Accounts table
    # if username does not exist as a chef or delivery person, then return false
    # if username exists as a chef or delivery person, then use delete_account_as_manager to delete all rows in all tables that match the username

def cut_employee_pay(username, decrement): # TODO: Daniel, implement this function
    ''' 
    username: username of employee (not guaranteed to meet conditions)
    decrement: integer value that the current pay should be deducted by (not guaranteed to meet conditions)
    Output: Returns true/false if decreasing the pay of a chef or delivery person by decrement is successful '''
    # make sure that username exists as a chef or delivery person (if not, return false)
    # make sure that decrement is a positive number that is not greater than the current pay (otherwise return false)
    # othewise change row in EmployeeAccounts and return true

def decline_customer_registrations(username): # TODO: Daniel, implement this function
    ''' 
    username: username of customer registration (not guaranteed to meet conditions)
    Output: Returns true/false if row in CustomerRegistrations table associated with username is deleted successfully 
    '''
    # if username does not exist in the CustomerRegistrations table, return false
    # if so, delete row in CustomerRegistrations and return true

def raise_employee_pay(username, increment): # TODO: Daniel, implement this function
    ''' 
    username: username of employee (not guaranteed to meet conditions)
    decrement: integer value that the current pay should be incremented by (not guaranteed to meet conditions)
    Output: Returns true/false if username's pay is successfully incremented 
    '''
    # make sure that username exists as a chef or delivery person (if not, return false)
    # make sure that increment is a positive number (otherwise return false)
    # otherwise change row in EmployeeAccounts and return true

def view_customer_registrations(): # TODO: Daniel, implement this function
    ''' Output: Returns a string of all usernames and deposit information in the CustomerRegistrations table '''