# This file is used to handle operations which delivery people are allowed to do

# TODO: Daniel, specify that you and I worked on this file in the header (you had it when you gave me your first ever code, which I should have kept, my mistake)
# TODO: Daniel, you forgot to import the functions here as well
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.
# TODO: Daniel, use proper naming conventions (I think everything in Python is snake_case except for classes (Pascal), exceptions (Pascal), constants (CAPS_WITH_UNDER), global constants (CAPS_WITH_UNDER))
# TODO: Daniel, check these errors that I get with VSCode
# TODO: Daniel, make sure your indentations are correct

def complete_delivery(delivery_order_id):
    '''
    delivery_order_id: ID number of the delivery order (not guaranteed to match conditions)
    Output: Returns true/false if delivery_order_id is successfully removed from Deliveries table
    '''
    # if delivery_order_id does not exist in the Deliveries table, return false
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    delOrd = []
    cur.execute("SELECT delivery_order_num FROM Deliveries")
    del_ord = cur.fetchall()
    for [x] in del_ord:
        delOrd.append(x)
    if(delivery_order_id not in delOrd):
        return False
    # otherwise perform actions and return true
    else:
        cur.execute("DELETE FROM Deliveries WHERE delivery_order_num = %s" %delivery_order_id))
        save_db_changes(cur,cnx)
        return True

def view_deliveries():
    ''' Output: Return string of all deliveries in the Deliveries table with username and delivery address information '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM Deliveries")
    deliv = cur.fetchall()
    for x in deliv:
        print(x)
    cur.close()
    cnx.close()
