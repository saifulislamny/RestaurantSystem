''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.

def surfer_apply_for_registered_customer(username, password, deposit):
    '''
    username: username that surfer requests to have (not guaranteed to meet conditions)
    password: password that surfer requests to have (not guaranteed to meet conditions)
    deposit: deposit that surfer requests to set (not guaranteed to meet conditions)
    Output: Returns true/false if surfer's requested username, password, and deposit information is successfully added to CustomerRegistrations table
    '''
    # if username does not match conditions in Accounts table, then return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    if(len(username)>15):
        return False
    # if password does not match conditions in Accounts table, then return false
    elif(len(password)>15):
        return False
    # if deposit is not a positive number, then return false
    elif(deposit < 0):
        return False
    # otherwise perform the operations and return true
    else:
        cur.execute("INSERT INTO CustomerRegistrations(cust_username, password, amt_of_deposit) VALUES (%s,%s,%s)", (username, password, deposit))
        save_db_changes(cur,cnx)
        return True
