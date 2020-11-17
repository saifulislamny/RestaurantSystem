# This file is used to handle operations which managers are allowed to do

from account_management import delete_account

def clear_deposit(username): # TODO: implement this function
    ''' Clears deposit of customer who gets kicked out or quits the system '''
    # essentially, delete row from CustomerAccount DB

def close_customer_account(username): 
    ''' Clears deposit and closes the account of a customer who gets kicked out or quits the system '''
    clear_deposit(username)
    delete_account(username)

    
