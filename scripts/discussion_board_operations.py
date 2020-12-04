''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db
# TODO: Daniel, if you have already checked to see that these functions work properly, then ignore this comment. Otherwise, check to see if these functions work properly through a separate file on your machine.

def view_discussion_boards(): 
    ''' Shows all rows in DiscussionBoardForDishes, DiscussionBoardForChefs, and DiscussionBoardForDelivery '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("SELECT * FROM DiscussionBoardForDishes")
    dbfd = cur.fetchall()
    cur.execute("SELECT * FROM DiscussionBoardForChefs")
    dbfc = cur.fetchall()
    cur.execute("SELECT * FROM DiscussionBoardForDelivery")
    dbfdl = cur.fetchall()
    dscb_str = ''
    print("Dishes Discussion Board:")
    for x in dbfd:
        dscb_str += x
    print("Chefs Discussion Board:")
    for x in dbfc:
        dscb_str += x
    print("Delivery Discussion Board:")
    for x in dbfdl:
        dscb_str += x
    cur.close()
    cnx.close()
    return dscb_str
