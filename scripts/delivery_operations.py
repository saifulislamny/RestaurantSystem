# This file is used to handle operations which delivery people are allowed to do
''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))




def complete_delivery(delivery_order_id):
    '''
    delivery_order_id: ID number of the delivery order (not guaranteed to match conditions)
    Output: Returns true/false if delivery_order_id is successfully removed from Deliveries table
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
    # otherwise perform actions and return true
    else:
        cur.execute("DELETE FROM Deliveries WHERE delivery_order_num = %s" %delivery_order_id)
        save_db_changes(cur,cnx)
        return True

def view_deliveries():
    ''' Output: Returns string of all deliveries in the Deliveries table with username and delivery address information '''
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
    deliv_str = ''
    for x in deliv_rating:
        deliv_list.append(x)
    for x in deliv_list:
        deliv_str += (x[0]+" "+str(x[1])+"\n")
    return deliv_str
