# This file is used to handle operations which managers are allowed to do

from account_management import delete_account_as_manager    

def accept_customer_registrations(username):
    ''' Add row to Accounts table and CustomerAccounts with respective information from CustomerRegistrations table, and delete row in CustomerRegistrations table ''' 
    # add username, password, and "RC" (stands for "Registered Customer") to Accounts table by taking info from CustomerRegistrations table
    # add username, amount of deposit, number of warnings (set to 0 since a new account) from CustomerRegistrations table (in the table, if you were able to set it to 0 by default then don't worry about adding 0 to the row since it's automatically done)
    # delete row from CustomerRegistrations table that matches username

def close_customer_account(username): 
    ''' Clears deposit and closes the account of a customer who gets kicked out or quits the system '''
    delete_customer_account_as_manager(username)

def close_employee_account(username):
    ''' Returns true/false if closing the account of a chef or delivery person is successful '''
    # make sure that the username exists as a chef or delivery person
    # if username does not exist as a chef or delivery person, then return false
    # if username exists as a chef or delivery person, delete the row in Accounts and EmployeeAccounts that associate with the username
    # if usernames exists and they are a delivery person, delete all the rows in DeliveryComplaintsAndCompliments that associate with the username
    # if username exists and they are a chef, delete all the rows in ChefComplaintsAndCompliments that associate with the username

def cut_employee_pay(username, decrement):
    ''' Returns true/false if decreasing the pay of a chef or delivery person by decrement is successful '''
    # make sure that username exists as a chef or delivery person
    # if not, return false
    # if so, change row in EmployeeAccounts and return true

def decline_customer_registrations(username):
    ''' Returns true/false if row in CustomerRegistrations table associated with username is deleted successfully '''
    # make sure that the username exists in the CustomerRegistrations table
    # if not, return false
    # if so, delete row in CustomerRegistrations and return true

def raise_employee_pay(username, increment):
    ''' Returns true/false if username's pay is successfully incremented '''
    # make sure that the username exists in the EmployeeAccounts table
    # if not, return false
    # if so, change row in EmployeeAccounts and return true

def view_customer_registrations():
    ''' Returns a string of all usernames and deposit information in the CustomerRegistrations table '''