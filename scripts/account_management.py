# This file is used to create, find, and delete accounts in the system

def create_account(username, password, type_of_user): # TODO: Daniel, implement this function
    ''' 
    username: username of user (not guaranteed to meet conditions)
    password: password of user (not guaranteed to meet conditions)
    type_of_user: account type of user (can only be 'RC', 'VC', 'C', 'D', or 'M') (not guaranteed to meet conditions)
    Output: Returns true/false after successfully inserting new account into Accounts table 
    '''
    # make sure username and password match the limit that is set in Account table
    # if username is 0 letters, return false (0 < len(username) <= 10)
    # if password is 0 letters, return false (0 < len(password) <= 10)
    # if username is more than 10 letters, return false (0 < len(username) <= 10)
    # if password is more than 10 letters, return false (0 < len(password) <= 10)

    # if username already exists in table, return false

    # for your own understanding: type_of_user can only be one of the following things: 'RC' (registered customer), 'VC' (VIP customer), 'C' (chef), 'D' (delivery person), 'M' (manager) 

    # otherwise insert a new row into Accounts table and return true

def delete_account_as_customer(username, password): # TODO: Daniel, implement this function
    ''' 
    username: username of customer (not guaranteed to meet conditions)
    password: password of customer (not guaranteed to meet conditions)
    Output: Returns true/false after successfully deleting account in Accounts and CustomerAccounts tables 
    ''' 
    # if username and password do not match a row in the Accounts and CustomerAccounts tables, return false
    # otherwise delete the rows in Accounts and CustomerAccounts table that matches username and password, and return true
    
def delete_account_as_manager(username): # TODO: Daniel, implement this function
    '''
    username: username of account (not guaranteed to meet conditions) 
    Output: Returns true/false if account is removed from the Accounts table and all other tables 
    ''' 
    # if username does not exist in the Accounts table, return false
    # otherwise delete the rows in ALL tables that have the username in any of its columns (Accounts, EmployeeAccounts (if they are an employee), CustomerAccounts (if they are a customer), Menu, MenuVotes, MenuForVC, CartItems, Deliveries, Pickups, DeliveryVotes, OrderedItems, ChefComplaintsAndCompliments, DeliveryComplaintsAndCompliments, DiscussionBoardForChefs, DiscussionBoardForDishes, DiscussionBoardForDeliveries)
    
    # keep this comment for later: TODO: if new tables are created in the future, then deal with the table here as well