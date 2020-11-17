# This file is used to handle main functionalities of the DB

import mysql.connector

def connect_to_db(): # TODO: implement this function
    cnx = mysql.connector.connect(host = '104.198.229.87', user = 'root', password = '322f20TuTh', database = 'project322') 
    # TODO: name db to "FDS", or "FoodDeliverySystem", etc. instead of "project322"
    # TODO: need to find out how to hide DB info (host, user, and password) through environmental variables
    return cnx

def get_cursor():
    cur = cnx.cursor()
    return cur

def create_tables(): # TODO: implement this function
    ''' Creates all tables used in this application '''
    cur = get_cursor()
    cur.execute("CREATE TABLE Chefs(username VARCHAR(64), password VARCHAR(25))") # TODO: table changed (username has to be distiguished from 'name')
    cur.execute("CREATE TABLE Customers(username VARCHAR(64), password VARCHAR(25))") # TODO: table changed (username has to be distiguished from 'name')
    cur.execute("CREATE TABLE Managers(username VARCHAR(64), password VARCHAR(25))") # TODO: table changed (username has to be distiguished from 'name')
    
    # TODO: create table Accounts which stores the account information for everyone on the system 
    # the table has columns which specify their username, password, and the type of user they are

    # TODO: create table CustomerAccounts which stores the deposit and warning information for each customer on the system
    # the table has columns which specify their username, amount of deposit, and the number of warnings they have (set to 0 by default)

    # TODO (not yet): create table Menu which stores the information for items on the menu
    # subject to change, so don't fulfill this part yet: (this table has name of the item, image of the item, description of the item, price of the time)

def view_menu_table(): # TODO: implement this function