# This file is used to handle main functionalities of the DB
#Daniel - get the insert photos working
import mysql.connector
import io
from PIL import Image, ImageTk

def connect_to_db():
    cnx = mysql.connector.connect(host = '35.193.212.231', user = 'root', password = '322f20TuTh', database = 'fooddeliverysystem')
    # TODO: need to find out how to hide DB info (host, user, and password) through environmental variables (not so important, can be done when there's nothing else to do)
    return cnx

def get_cursor(cnx):
    cur = cnx.cursor()
    return cur

def close_db(cur,cnx):
    cur.close()
    cnx.close()

def save_db_changes(cur, cnx):
    cnx.commit()
    cur.close()
    cnx.close()
    return'Saved Changes'

def byte_to_imageFile(bytes):
    imageStream = io.BytesIO(pic)
    imageFile = Image.open(imageStream)


def create_tables():
    ''' Creates all tables used in this application '''
    cnx = connect_to_db()
    cur = get_cursor(cnx)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(item_name, photo, chef_username, item_desc, price):
    print("Inserting BLOB into Menu table")
    try:
        cnx = mysql.connector.connect(host = '35.193.212.231', user = 'root',
                                      password = '322f20TuTh', database = 'fooddeliverysystem')

        cursor = cnx.cursor()
        sql_insert_blob_query = """ INSERT INTO Menu
                          (item_name, image, chef_username, item_desc, price) VALUES (%s,%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (item_name, empPicture, chef_username, item_desc, price)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        cnx.commit()
        print("Image and file inserted successfully as a BLOB into Menu table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (cnx.is_connected()):
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")


    # create table Accounts which stores the account information for everyone on the system
    # the table has columns which specify their username (primary key), password, full name, and the type of user they are
    cur.execute("CREATE TABLE Accounts(username VARCHAR(15) PRIMARY KEY, password VARCHAR(15), full_name varchar(64), type CHAR(2))")
    # add 2 random rows for RC
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('barzy13', 'LGIbelmont4', 'Mat Barzal', 'RC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('jmish51', 'RHmich21', 'Jason Mishkin', 'RC')")
    # add 2 random rows for VC
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('biznasty', 'nBd12', 'Paul Bissonette', 'VC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('judgefudge96','baskiceball','Marshal Erikson', 'VC')")
    # add 2 random rows for C
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('byrdeman','Laundromat3','Marty Byrde', 'C')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('piedpiper', 'middleOut28', 'Richard Hendricks', 'C')")
    # add 2 random rows for D
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('littleCub18','pointBlanc2', 'Alex Rider', 'D')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('Canary77','SupeComp5','Hughie Campbell', 'D')")
    # add 1 random row for M
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('BrotherChicken', 'LosPollos2?', 'Gustavo Fring', 'M')")


    # create table CustomerAccounts which stores the deposit and warning information for each customer on the system
    # the table has columns which specify their username (primary key), amount of deposit, the number of warnings they have (set to 0 by default), total they have spent so far (set to 0 by default), and total number of orders so far (set to 0 by default)
    cur.execute('''CREATE TABLE CustomerAccounts(username VARCHAR(15) PRIMARY KEY, amt_of_deposit INT(9), num_of_warnings INT(3) DEFAULT 0,
                  total_spents CHAR(5) DEFAULT 0, total_num_orders INT(5) DEFAULT 0)''')
    # take the 4 users you added for RC and VC from Accounts and add it to this table as well
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('barzy13', 100)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('jmish51', 48)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('biznasty', 12)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('judgefudge96', 50)")


    # create table EmployeeAccounts which stores the type of employee, pay, and warnings for each employee on the system
    # the table has columns which specify their username (primary key), type of employee (C, D, M), their pay, and the number of warnings they have (set to 0 by default)
    cur.execute("CREATE TABLE EmployeeAccounts(username VARCHAR(15) PRIMARY KEY, emp_type CHAR(2), pay INT(10), nume_of_warnings CHAR(5) DEFAULT 0)")
    # take the 5 users you added for C, D, and M from Accounts and add it to this table as well
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('byrdeman','C', 25)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('piedpiper', 'C', 25)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('littleCub18', 'D', 18)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('Canary77', 'D',18)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('BrotherChicken', 'M', 50)")

    # TODO: create table Menu which stores the information for items on the menu for all customers to view
    # this table has columns which specify the name of the item (primary key, limit to 50 characters), image of the item, chef username who made the menu item, description of the item (limit to 150 characters), and price of the item
    cur.execute("CREATE TABLE Menu(item_name VARCHAR(50) PRIMARY KEY, image BLOB NOT NULL, chef_username VARCHAR(15), item_desc VARCHAR(150), price REAL)")
    # add 2 random rows (that match C username from Accounts and EmployeeAccounts tables)
#    cur.execute("INSERT INTO Menu(item_name, image, chef_username, item_desc, price) VALUES ('Bacon Avocado Burger',"INSERT PICTURE", 'byrdeman', 'Burger topped with Avocado, Crispy Bacon, Sauteed Mushrooms and Garlic Mayo.', 13.99)")
#    cur.execute("INSERT INTO Menu(item_name, image, chef_username, item_desc, price) VALUES ('Fettuccine Alfredo',"INSERT PICTURE", 'piedpiper', 'Bechamel, roast garlic, parmesan.', 12.99)")
#    cur.execute("INSERT INTO Menu(item_name, image, chef_username, item_desc, price) VALUES ('NY Style Cheese Pizza Slice', "INSERT PICTURE", 'piedpiper', 'Thin crust, topped with our homemade tomato sauce and imported finest grande mozzarella.', 2.50)")
#    cur.execute("INSERT INTO Menu(item_name, image, chef_username, item_desc, price) VALUES ('Cappuccino', "INSERT PICTURE", 'byrdeman', 'Dark, rich espresso under a layer of thick milk foam.', 3.59)")

    # create table MenuVotes which stores the customer's votes for each item on the menu
    # this table has the name of the menu item that is being voted, the customer's username who voted this menu item, and the rating they gave out of 5
    cur.execute("CREATE TABLE AllowedVotes(vote_range TINYINT NOT NULL, PRIMARY KEY(vote_range))")
    cur.execute("INSERT INTO AllowedVotes VALUES (0),(1),(2),(3),(4),(5)")
    cur.execute("CREATE TABLE MenuVotes(item_name VARCHAR(50), cust_username VARCHAR(15), rating TINYINT NOT NULL, foreign key(rating) REFERENCES AllowedVotes(vote_range))")


    #sample data
    cur.execute("INSERT INTO MenuVotes(item_name, username, rating) VALUES ('Bacon Avocado Burger','jmish51', 3)")
    cur.execute("INSERT INTO MenuVotes(item_name, username, rating) VALUES ('Fettuccine Alfredo','judgefudge96', 5)")

    # create table MenuForVC which stores the information for items on the menu specially made for VC customers only
    # this table columns which specify the name of the item (primary key, limit to 50 characters), image of the item,
    #chef username who made the menu item, description of the item (limit to 150 characters), and price of the item
    cur.execute("CREATE TABLE MenuForVC(item_name VARCHAR(50), item_desc VARCHAR(150), price REAL)")

    #sample data
    cur.execute("INSERT INTO MenuForVC(item_name, item_desc, price) VALUES ('Pinot Noir Braised Short Rib','Truffle Mushrooms Risotto, Pearl Onion', 37.99)")
    cur.execute("INSERT INTO MenuForVC(item_name, item_desc, price) VALUES ('Sesame-Crusted Ahi Tuna','Miso-Marinated, Served on a bed of Black Rice with Shitake Mushrooms and a Ginger-Soy Glaze', 31.99)")

    # create table CartItems which stores the cart items for ALL customers
    # the table has columns which specify the username of the customer (composite key), the name of the item added to cart (composite key), and the quantity of the item added to the cart (default set to 1)
    cur.execute("CREATE TABLE CartItems(cust_username VARCHAR(15), item_name VARCHAR(50), quantity INT(3) DEFAULT 1, PRIMARY KEY(cust_username, item_name))")

    #sample data
    cur.execute("INSERT INTO CartItems(cust_username, item_name, quantity) VALUES ('barzy13','NY Style Cheese Pizza Slice', 3)")
    cur.execute("INSERT INTO CartItems(cust_username, item_name) VALUES ('biznasty','Bacon Avocado Burger')")

    # create table Deliveries which stores the pending orders that need to be delivered
    # the table has columns which specify the delivery order number (primary key, starts at 1, and automatically increments), the username of the customer who made the order, the delivery address of the order, and the items ordered along with the quantity of each item (as a nested array i.e. [['Water',1], ['Soda', 2]])
    cur.execute("CREATE TABLE Deliveries(delivery_order_num INT AUTO_INCREMENT, cust_username VARCHAR(15), delivery_addr VARCHAR(256), items_ordered json, PRIMARY KEY(delivery_order_num))")

    #sample data
    cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES ('barzy13','1255 Hempstead Turnpike', JSON_ARRAY(JSON_ARRAY('NY Style Cheese Pizza Slice',3),JSON_ARRAY('Cappuccino',1)))")
    cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES ('biznasty','13 W 27th St', JSON_ARRAY(JSON_ARRAY('Bacon Avocado Burger',1)))")

    # create table Pickups which store the pending orders that need to be picked up
    # the table has columns which specify the pickup order number (primary key, starts at 1, and automatically increments), the username of the customer who made the order, and the items ordered along with the quanity of each item (as a nested array i.e. [['Water',1], ['Soda', 2]])
    cur.execute("CREATE TABLE Pickups(pickup_order_num INT AUTO_INCREMENT, cust_username VARCHAR(15), items_ordered json, PRIMARY KEY(pickup_order_num))")

    #sample data
    cur.execute("INSERT INTO Pickups(cust_username, items_ordered) VALUES ('jmish51', JSON_ARRAY(JSON_ARRAY('Bacon Avocado Burger',1)))")
    cur.execute("INSERT INTO Pickups(cust_username, items_ordered) VALUES ('judgefudge96', JSON_ARRAY(JSON_ARRAY('NY Style Cheese Pizza Slice',3),JSON_ARRAY('Cappuccino',1)))")

    # create table DeliveryVotes which stores the customer's votes for the deliveries they received
    # the table has columns which specify the delivery order number and the rating the customer gave out of 5
    cur.execute("CREATE TABLE DeliveryVotes(delivery_order_num INT, rating TINYINT NOT NULL, foreign key(rating) REFERENCES AllowedVotes(vote_range))")

    #sample data
    cur.execute("INSERT INTO DeliveryVotes(delivery_order_num, rating) VALUES (1, 2)")
    cur.execute("INSERT INTO DeliveryVotes(delivery_order_num, rating) VALUES (2, 5)")

    # create table OrderedItems which stores the quantity of each item that each customer has ordered
    # the table has columns which specify the username of the customer (composite key), name of the menu item (composite key), and the total quantity they have ordered of this item

    cur.execute("CREATE TABLE OrderedItems(cust_username VARCHAR(15), item_name VARCHAR(50), quantity INT(3) DEFAULT 1, PRIMARY KEY(cust_username, item_name))")

    #sample data
    cur.execute("INSERT INTO OrderedItems(cust_username, item_name, quantity) VALUES ('barzy13','NY Style Cheese Pizza Slice', 3)")
    cur.execute("INSERT INTO OrderedItems(cust_username, item_name, quantity) VALUES ('biznasty','Bacon Avocado Burger')")

    # create table CustomerRegistrations which stores the account information for surfers who registered to be customers, but have not been approved yet by manager
    # the table has columns which specify the username (primary key), password, and deposit information of username (how much they set for deposit)

    cur.execute("CREATE TABLE CustomerRegistrations(cust_username VARCHAR(15) PRIMARY KEY, password VARCHAR(64), amt_of_deposit INT(9)))")

    #sample data
    cur.execute("INSERT INTO CustomerRegistrations(cust_username, password, amt_of_deposit) VALUES ('whitdog4','ANHstatGuy', 123)")
    cur.execute("INSERT INTO CustomerRegistrations(cust_username, password, amt_of_deposit) VALUES ('mando','ThisIsTheWay', 87)")

    # create table ChefComplaintsAndCompliments which stores the compliments and complaints made by customers for chefs
    # the table has columns which specify the username of the chef who received the feedback, the username of the customer who made the feedback, type of feedback (compliment or complaint), and the compliment/complaint itself (limit to 150 characters)

    cur.execute("CREATE TABLE ChefComplaintsAndCompliments(chef_username VARCHAR(15) PRIMARY KEY, cust_username VARCHAR(15), type_of_feedback VARCHAR(10), feedback VARCHAR(150)))")

    #sample data
    cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback,  feedback) VALUES ('byrdeman','judgefudge96','complaint','Undercooked my food.')")
    cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback,  feedback) VALUES ('piedpiper','jmish51','compliment','This chef makes the best pizza in NY. Will recommend to all of my friends.')")

    # create table DeliveryComplaintsAndCompliments which stores the compliments and complaints made by customers for delivery people
    # the table has columns which specify the username of the delivery person who received the feedback, the username of the customer made the feedback, type of feedback (compliment or complaint), and the compliment/complaint itself (limit to 150 characters)

    cur.execute("CREATE TABLE DeliveryComplaintsAndCompliments(delivery_username VARCHAR(15) PRIMARY KEY, cust_username VARCHAR(15), type_of_feedback VARCHAR(10), feedback VARCHAR(150)))")

    #sample data
    cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback,  feedback) VALUES ('Canary77','barzy13','compliment','Food got here so quick. Felt like I got it at a sit down place.')")
    cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback,  feedback) VALUES ('littleCub18','biznasty','complaint','My burger fell apart in delivery and I had to put it back together before I could eat it.')")

    # create table DiscussionBoardForChefs which stores the discussion topics for all chefs
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the chef who the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    cur.execute("CREATE TABLE DiscussionBoardForChefs(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), chef_name VARCHAR(15), message VARCHAR(150)))")

     #sample data
    cur.execute("INSERT INTO DiscussionBoardForChefs(discussion_topic_num, cust_username, chef_username,  message) VALUES ('13593','judgefudge96','byrdeman','How did you get that sear on my steak? It looked and tasted unbelivable.')")
    cur.execute("INSERT INTO DiscussionBoardForChefs(discussion_topic_num, cust_username, chef_username,  message) VALUES ('96781','biznasty','piedpiper','If you need a hand I can help you cook. Doesn't seem like you know what you are doing.')")

    # create table DiscussionBoardForDishes which stores the discussion topics for all dishes/menu items
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the menu item the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    cur.execute("CREATE TABLE DiscussionBoardForDishes(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), menu_item VARCHAR(50), message VARCHAR(150)))")

    #sample data
    cur.execute("INSERT INTO DiscussionBoardForDishes(discussion_topic_num, cust_username, menu_item,  message) VALUES ('31037','jmish51','NY Style Cheese Pizza Slice','I need to buy this 'za in bulk. I can eat it all day. REH!')")
    cur.execute("INSERT INTO DiscussionBoardForDishes(discussion_topic_num, cust_username, menu_item,  message) VALUES ('02371','barzy13','Pinot Noir Braised Short Rib','How do I become a VC because I need to try this')")

    # create table DiscussionBoardForDelivery which stores the discussion topics for all delivery people
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the delivery person who the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    cur.execute("CREATE TABLE DiscussionBoardForDelivery(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), delivery_userhname VARCHAR(15), message VARCHAR(150)))")

    #sample data
    cur.execute("INSERT INTO DiscussionBoardForDelivery(discussion_topic_num, cust_username, delivery_username,  message) VALUES ('92716','barzy13','littleCub18','Guy doesnt know how to open a twist-off drink')")
    cur.execute("INSERT INTO DiscussionBoardForDelivery(discussion_topic_num, cust_username, delivery_username,  message) VALUES ('20296','biznasty','Canary77','IDK WHAT TO SAY HERE')")
