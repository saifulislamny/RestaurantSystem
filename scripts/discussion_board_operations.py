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
