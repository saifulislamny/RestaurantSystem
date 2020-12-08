# This file is used to handle operations which delivery people are allowed to do
''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db





def complete_delivery(username, delivery_order_id): # TODO: Daniel, implement this function (modification made)
    '''
    delivery_order_id: ID number of the delivery order (not guaranteed to match conditions)
    Output: Returns true/false if modifies row in Deliveries table
    '''
    # if delivery_order_id does not exist in the Deliveries table, return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    do_list = []
    cur.execute("SELECT delivery_order_num FROM Deliveries")
    del_ord = cur.fetchall()
    for [x] in del_ord:
        do_list.append(x)
    if(delivery_order_id not in do_list):
        return False
    # TODO: Daniel, make sure delivery is not already completed by someone else (return false if it is)

    # otherwise perform actions and return true
    else:

        # we don't delete anymore so this line is unnecessary# cur.execute("DELETE FROM Deliveries WHERE delivery_order_num = %s" %delivery_order_id)
        # TODO: Daniel, modify row in Deliveries table by updating the delivery username in the row that matches the delivery_order_id (the delivery username entity will originally be empty)

        save_db_changes(cur,cnx)
        return True

def view_deliveries():
    ''' Output: Returns string of all deliveries in the Deliveries table '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM Deliveries")
    deliv = cur.fetchall()
    deliv_list = []
    deliv_str = ''
    for x in deliv:
        deliv_list.append(x)
    for x in deliv_list:
        deliv_str += (str(x[0])+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    cur.close()
    cnx.close()
    return deliv_str

def view_incomplete_deliveries(): # TODO: Daniel, implement this function
    ''' Output: Returns string of all incomplete deliveries in the Deliveries table '''
    # essentially, all rows where the delivery person column is NULL/empty 

def view_ratings_of_delivery_person(username):
    '''
    username: username of delivery person
    Output: Returns average rating of delivery person for all deliveries they made
    '''
    # use DeliveryVotes table
    if(len(username)>15 or len(username)==0):
        return False
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT delivery_username, rating FROM DeliveryVotes")
    deliv_rating = cur.fetchall()
    deliv_list = []
    avg = 0
    for x in deliv_rating:
        deliv_list.append(x)
    for x in deliv_list:
        avg+= x[1]
    avg/=len(deliv_list)
    return avg
    
print(view_ratings_of_delivery_person('littleCub18'))