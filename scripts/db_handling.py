# This file is used to handle main functionalities of the DB

import mysql.connector

def connect_to_db(): # TODO: Daniel, implement this function
    cnx = mysql.connector.connect(host = '104.198.229.87', user = 'root', password = '322f20TuTh', database = 'project322') 
    # TODO: name db to "FDS", or "FoodDeliverySystem", etc. instead of "project322"
    # TODO: need to find out how to hide DB info (host, user, and password) through environmental variables (not so important, can be done when there's nothing else to do)
    return cnx

def get_cursor():
    cur = connect_to_db.cursor()
    return cur

def create_tables(): # TODO: Daniel, implement all TODOs in this function
    # TODO: delete ALL the tables you already have on the DB and add all of the ones shown below
    ''' Creates all tables used in this application '''
    cur = get_cursor()
    # i deleted the code you had here before but look at the email you sent me if you want to look at it again
    
    # TODO: create table Accounts which stores the account information for everyone on the system 
    # the table has columns which specify their username (primary key), password, full name, and the type of user they are
    # add 2 random rows for RC
    # add 2 random rows for VC
    # add 2 random rows for C
    # add 2 random rows for D
    # add 1 random row for M

    # TODO: create table CustomerAccounts which stores the deposit and warning information for each customer on the system
    # the table has columns which specify their username (primary key), amount of deposit, the number of warnings they have (set to 0 by default), total they have spent so far (set to 0 by default), and total number of orders so far (set to 0 by default)
    # take the 4 users you added for RC and VC from Accounts and add it to this table as well

    # TODO: create table EmployeeAccounts which stores the type of employee, pay, and warnings for each employee on the system
    # the table has columns which specify their username (primary key), type of employee (C, D, M), their pay, and the number of warnings they have (set to 0 by default)
    # take the 5 users you added for C, D, and M from Accounts and add it to this table as well

    # TODO: create table Menu which stores the information for items on the menu for all customers to view
    # this table has columns which specify the name of the item (primary key, limit to 50 characters), image of the item, chef username who made the menu item, description of the item (limit to 150 characters), and price of the item
    # add 2 random rows (that match C username from Accounts and EmployeeAccounts tables)

    # TODO: create table MenuVotes which stores the customer's votes for each item on the menu
    # this table has the name of the menu item that is being voted, the customer's username who voted this menu item, and the rating they gave out of 5

    # TODO: create table MenuForVC which stores the information for items on the menu specially made for VC customers only
    # this table columns which specify the name of the item (primary key, limit to 50 characters), image of the item, chef username who made the menu item, description of the item (limit to 150 characters), and price of the item

    # TODO: create table CartItems which stores the cart items for ALL customers
    # the table has columns which specify the username of the customer (composite key), the name of the item added to cart (composite key), and the quantity of the item added to the cart (default set to 1)

    # TODO: create table Deliveries which stores the pending orders that need to be delivered
    # the table has columns which specify the delivery order number (primary key, starts at 1, and automatically increments), the username of the customer who made the order, the delivery address of the order, and the items ordered along with the quantity of each item (as a nested array i.e. [['Water',1], ['Soda', 2]])

    # TODO: create table Pickups which store the pending orders that need to be picked up
    # the table has columns which specify the pickup order number (primary key, starts at 1, and automatically increments), the username of the customer who made the order, and the items ordered along with the quanity of each item (as a nested array i.e. [['Water',1], ['Soda', 2]])

    # TODO: create table DeliveryVotes which stores the customer's votes for the deliveries they received 
    # the table has columns which specify the delivery order number and the rating the customer gave out of 5

    # TODO: create table OrderedItems which stores the quantity of each item that each customer has ordered
    # the table has columns which specify the username of the customer (composite key), name of the menu item (composite key), and the total quantity they have ordered of this item 

    # TODO: create table CustomerRegistrations which stores the account information for surfers who registered to be customers, but have not been approved yet by manager
    # the table has columns which specify the username (primary key), password, and deposit information of username (how much they set for deposit)

    # TODO: create table ChefComplaintsAndCompliments which stores the compliments and complaints made by customers for chefs
    # the table has columns which specify the username of the chef who received the feedback, the username of the customer who made the feedback, type of feedback (compliment or complaint), and the compliment/complaint itself (limit to 150 characters)

    # TODO: create table DeliveryComplaintsAndCompliments which stores the compliments and complaints made by customers for delivery people
    # the table has columns which specify the username of the delivery person who received the feedback, the username of the customer made the feedback, type of feedback (compliment or complaint), and the compliment/complaint itself (limit to 150 characters)

    # TODO: create table DiscussionBoardForChefs which stores the discussion topics for all chefs
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the chef who the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    # TODO: create table DiscussionBoardForDishes which stores the discussion topics for all dishes/menu items
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the menu item the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    # TODO: create table DiscussionBoardForDelivery which stores the discussion topics for all delivery people
    # the table has columns which specify the discussion topic number (primary key), the customer who made the discussion topic, the delivery person who the discussion topic is about, and the message in the discussion topic (limit to 150 characters)

    # TODO: make sure to populate each one of the tables with a reasonable number of rows