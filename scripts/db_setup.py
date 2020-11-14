import mysql.connector

def connect_to_db():
    cnx = mysql.connector.connect(host = '104.198.229.87', user = 'root', password = '322f20TuTh', database = 'project322') 
    # TODO: name db to "FDS", or "FoodDeliverySystem", etc. instead of "project322"
    # TODO: need to find out how to hide DB info (host, user, and password) through environmental variables
    return cnx

def get_cursor():
    cur = cnx.cursor()
    return cur

def create_tables():   
    ''' creates all tables used in this application '''
    cur = get_cursor()
    cur.execute("CREATE TABLE Chefs(name VARCHAR(64), password VARCHAR(25))") 
    cur.execute("CREATE TABLE Customers(name VARCHAR(64), password VARCHAR(25))")
    cur.execute("CREATE TABLE Managers(name VARCHAR(64), password VARCHAR(25))")
    
    # TODO: create table for Accounts which stores the account information for everyone on the system 
    # (the table has a column which specifies their password and a column which specifies the type of user they are)

