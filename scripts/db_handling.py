# This file is used to handle main functionalities of the DB
''' @authors: daniellichter, saifulislam '''
import mysql.connector
import io
from PIL import Image, ImageTk

#Daniel - get the insert photos working
#It works! -Daniel

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

def byte_to_imagefile(bytes):
    image_stream = io.BytesIO(bytes)
    imagefile = Image.open(image_stream)
    return imagefile


def create_tables():
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("CREATE TABLE Accounts(username VARCHAR(15) PRIMARY KEY, password VARCHAR(15), full_name varchar(64), type CHAR(2))")
    cur.execute("CREATE TABLE CustomerAccounts(username VARCHAR(15) PRIMARY KEY, amt_of_deposit INT(9), num_of_warnings INT(3) DEFAULT 0, total_spents INT(9) DEFAULT 0, total_num_orders INT(5) DEFAULT 0)")
    cur.execute("CREATE TABLE EmployeeAccounts(username VARCHAR(15) PRIMARY KEY, emp_type CHAR(2), pay INT(10), num_of_warnings INT(3) DEFAULT 0)")
    cur.execute("CREATE TABLE Menu(item_name VARCHAR(50) PRIMARY KEY, image BLOB, chef_username VARCHAR(15), item_desc VARCHAR(150), price REAL)")
    cur.execute("CREATE TABLE AllowedVotes(vote_range TINYINT NOT NULL, PRIMARY KEY(vote_range))")
    cur.execute("INSERT INTO AllowedVotes VALUES (0),(1),(2),(3),(4),(5)")
    cur.execute("CREATE TABLE MenuVotes(item_name VARCHAR(50), cust_username VARCHAR(15), rating TINYINT NOT NULL, foreign key(rating) REFERENCES AllowedVotes(vote_range))")
    cur.execute("CREATE TABLE MenuForVC(item_name VARCHAR(50), item_desc VARCHAR(150), price REAL, chef_username VARCHAR(15))") 
    cur.execute("CREATE TABLE CartItems(cust_username VARCHAR(15), item_name VARCHAR(50), quantity INT(3) DEFAULT 1, PRIMARY KEY(cust_username, item_name))")
    cur.execute("CREATE TABLE Deliveries(delivery_order_num INT AUTO_INCREMENT, cust_username VARCHAR(15), delivery_addr VARCHAR(256), items_ordered json, PRIMARY KEY(delivery_order_num))")
    cur.execute("CREATE TABLE Pickups(pickup_order_num INT AUTO_INCREMENT, cust_username VARCHAR(15), items_ordered json, PRIMARY KEY(pickup_order_num))")
    cur.execute("CREATE TABLE DeliveryVotes(delivery_order_num INT NOT NULL PRIMARY KEY, delivery_username VARCHAR(15), rating TINYINT NOT NULL, cust_username VARCHAR(15), foreign key(rating) REFERENCES AllowedVotes(vote_range))")
    cur.execute("CREATE TABLE OrderedItems(cust_username VARCHAR(15), item_name VARCHAR(50), quantity INT(3) DEFAULT 1, PRIMARY KEY(cust_username, item_name))")
    cur.execute("CREATE TABLE CustomerRegistrations(cust_username VARCHAR(15) PRIMARY KEY, password VARCHAR(64), amt_of_deposit INT(9))")
    cur.execute("CREATE TABLE AccountDeregistrations(username VARCHAR(15), reason_for_dereg VARCHAR(6) CHECK (reason_for_dereg IN ('kicked', 'quit')))")
    cur.execute("CREATE TABLE ChefComplaintsAndCompliments(chef_username VARCHAR(15) PRIMARY KEY, cust_username VARCHAR(15), type_of_feedback VARCHAR(10), feedback VARCHAR(150))")
    cur.execute("CREATE TABLE CustomerToCustomerComplaints(complainer_username VARCHAR(15), complainee_username VARCHAR(15), complaint VARCHAR(150))")
    cur.execute("CREATE TABLE DeliveryComplaintsAndCompliments(delivery_username VARCHAR(15) PRIMARY KEY, cust_username VARCHAR(15), type_of_feedback VARCHAR(10), feedback VARCHAR(150))")
    cur.execute("CREATE TABLE DiscussionBoardForChefs(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), chef_name VARCHAR(15), message VARCHAR(150))")
    cur.execute("CREATE TABLE DiscussionBoardForDishes(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), menu_item VARCHAR(50), message VARCHAR(150))")
    cur.execute("CREATE TABLE DiscussionBoardForDelivery(discussion_topic_num INT PRIMARY KEY, cust_username VARCHAR(15), delivery_username VARCHAR(15), message VARCHAR(150))")
    cur.execute("CREATE TABLE TabooWords(taboo_word VARCHAR(25)")
    save_db_changes(cur,cnx)


def insert_random_table_entries():

    # TODO: Daniel, make sure that each table has a relevant number of entries

    cnx = connect_to_db()
    cur = get_cursor(cnx)
    cur.execute("INSERT INTO TabooWords VALUES ('frick'),('stupid'),('BS'),('butt')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('barzy13', 'LGIbelmont4', 'Mat Barzal', 'RC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('jmish51', 'RHmich21', 'Jason Mishkin', 'RC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('biznasty', 'nBd12', 'Paul Bissonette', 'VC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('judgefudge96','baskiceball','Marshal Erikson', 'VC')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('byrdeman','Laundromat3','Marty Byrde', 'C')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('piedpiper', 'middleOut28', 'Richard Hendricks', 'C')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('littleCub18','pointBlanc2', 'Alex Rider', 'D')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('Canary77','SupeComp5','Hughie Campbell', 'D')")
    cur.execute("INSERT INTO Accounts(username, password, full_name, type) VALUES ('BrotherChicken', 'LosPollos2?', 'Gustavo Fring', 'M')")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('barzy13', 100)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('jmish51', 48)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('biznasty', 12)")
    cur.execute("INSERT INTO CustomerAccounts(username, amt_of_deposit) VALUES ('judgefudge96', 50)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('byrdeman','C', 25)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('piedpiper', 'C', 25)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('littleCub18', 'D', 18)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('Canary77', 'D',18)")
    cur.execute("INSERT INTO EmployeeAccounts(username, emp_type, pay) VALUES ('BrotherChicken', 'M', 50)")
    cur.execute("INSERT INTO MenuVotes(item_name, cust_username, rating) VALUES ('Bacon Avocado Burger','jmish51', 3)")
    cur.execute("INSERT INTO MenuVotes(item_name, cust_username, rating) VALUES ('Fettuccine Alfredo','judgefudge96', 5)")
    cur.execute("INSERT INTO MenuForVC(item_name, item_desc, price) VALUES ('Pinot Noir Braised Short Rib','Truffle Mushrooms Risotto, Pearl Onion', 37.99)")
    cur.execute("INSERT INTO MenuForVC(item_name, item_desc, price) VALUES ('Sesame-Crusted Ahi Tuna','Miso-Marinated, Served on a bed of Black Rice with Shitake Mushrooms and a Ginger-Soy Glaze', 31.99)")
    cur.execute("INSERT INTO CartItems(cust_username, item_name, quantity) VALUES ('barzy13','NY Style Cheese Pizza Slice', 3)")
    cur.execute("INSERT INTO CartItems(cust_username, item_name) VALUES ('biznasty','Bacon Avocado Burger')")
    cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES ('barzy13','1255 Hempstead Turnpike', JSON_ARRAY(JSON_ARRAY('NY Style Cheese Pizza Slice',3),JSON_ARRAY('Cappuccino',1)))")
    cur.execute("INSERT INTO Deliveries(cust_username, delivery_addr, items_ordered) VALUES ('biznasty','13 W 27th St', JSON_ARRAY(JSON_ARRAY('Bacon Avocado Burger',1)))")
    cur.execute("INSERT INTO Pickups(cust_username, items_ordered) VALUES ('jmish51', JSON_ARRAY(JSON_ARRAY('Bacon Avocado Burger',1)))")
    cur.execute("INSERT INTO Pickups(cust_username, items_ordered) VALUES ('judgefudge96', JSON_ARRAY(JSON_ARRAY('NY Style Cheese Pizza Slice',3),JSON_ARRAY('Cappuccino',1)))")
    cur.execute("INSERT INTO DeliveryVotes(delivery_order_num, delivery_username, rating) VALUES (1, 'littleCub18', 2)")
    cur.execute("INSERT INTO DeliveryVotes(delivery_order_num, delivery_username, rating) VALUES (2, 'littleCub18', 5)")
    cur.execute("INSERT INTO OrderedItems(cust_username, item_name, quantity) VALUES ('barzy13','NY Style Cheese Pizza Slice', 3)")
    cur.execute("INSERT INTO OrderedItems(cust_username, item_name) VALUES ('biznasty','Bacon Avocado Burger')")
    cur.execute("INSERT INTO CustomerRegistrations(cust_username, password, amt_of_deposit) VALUES ('whitdog4','ANHstatGuy', 123)")
    cur.execute("INSERT INTO CustomerRegistrations(cust_username, password, amt_of_deposit) VALUES ('mando','ThisIsTheWay', 87)")
    cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback,  feedback) VALUES ('byrdeman','judgefudge96','complaint','Undercooked my food.')")
    cur.execute("INSERT INTO ChefComplaintsAndCompliments(chef_username, cust_username, type_of_feedback,  feedback) VALUES ('piedpiper','jmish51','compliment','This chef makes the best pizza in NY. Will recommend to all of my friends.')")
    cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback,  feedback) VALUES ('Canary77','barzy13','compliment','Food got here so quick. Felt like I got it at a sit down place.')")
    cur.execute("INSERT INTO DeliveryComplaintsAndCompliments(delivery_username, cust_username, type_of_feedback,  feedback) VALUES ('littleCub18','biznasty','complaint','My burger fell apart in delivery and I had to put it back together before I could eat it.')")
    cur.execute("INSERT INTO DiscussionBoardForChefs(discussion_topic_num, cust_username, chef_name,  message) VALUES ('13593','judgefudge96','byrdeman','How did you get that sear on my steak? It looked and tasted unbelivable.')")
    cur.execute("INSERT INTO DiscussionBoardForChefs(discussion_topic_num, cust_username, chef_name,  message) VALUES ('96781','biznasty','piedpiper','If you need a hand I can help you cook. Doesnt seem like you know what you are doing.')")
    cur.execute("INSERT INTO DiscussionBoardForDishes(discussion_topic_num, cust_username, menu_item,  message) VALUES ('31037','jmish51','NY Style Cheese Pizza Slice','I need to buy this za in bulk. I can eat it all day. REH!')")
    cur.execute("INSERT INTO DiscussionBoardForDishes(discussion_topic_num, cust_username, menu_item,  message) VALUES ('02371','barzy13','Pinot Noir Braised Short Rib','How do I become a VC because I need to try this')")
    cur.execute("INSERT INTO DiscussionBoardForDelivery(discussion_topic_num, cust_username, delivery_username,  message) VALUES ('92716','barzy13','littleCub18','Guy doesnt know how to open a twist-off drink')")
    cur.execute("INSERT INTO DiscussionBoardForDelivery(discussion_topic_num, cust_username, delivery_username,  message) VALUES ('20296','biznasty','Canary77','IDK WHAT TO SAY HERE')")
    save_db_changes(cur,cnx)



def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insertBLOB(item_name, photo, chef_username, item_desc, price):
    '''Used to insert a row into a menu with an image'''
    cnx = connect_to_db()
    cur = get_cursor(cnx)
    sql_insert_blob_query = """ INSERT INTO Menu(item_name, image, chef_username, item_desc, price) VALUES (%s,%s,%s,%s,%s)"""
    emp_picture = convertToBinaryData(photo)
    # Convert data into tuple format
    insert_blob_tuple = (item_name, emp_picture, chef_username, item_desc, price)
    cur.execute(sql_insert_blob_query, insert_blob_tuple)
    save_db_changes(cur,cnx)
