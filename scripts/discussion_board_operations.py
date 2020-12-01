# TODO: Daniel, specify that you and I worked on this file in the header (you had it when you gave me your first ever code, which I should have kept, my mistake)
# TODO: Daniel, you forgot to import functions here as well
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
    print("Dishes Discussion Board:")
    for x in dbfd:
        print(x)
    print("Chefs Discussion Board:")
    for x in dbfc:
        print(x)
    print("Delivery Discussion Board:")
    for x in dbfdl:
        print(x)
    cur.close()
    cnx.close()
