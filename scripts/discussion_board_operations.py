''' @authors: daniellichter, saifulislam '''
from db_handling import connect_to_db, get_cursor, save_db_changes, close_db

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
        dscb_str += (str(x[0])+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    print("Chefs Discussion Board:")
    for x in dbfc:
        dscb_str += (str(x[0])+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    print("Delivery Discussion Board:")
    for x in dbfdl:
        dscb_str += (str(x[0])+" "+x[1]+" "+x[2]+" "+x[3]+"\n")
    cur.close()
    cnx.close()
    return dscb_str

