import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def databaseConexion():
    try:
        conexion = sqlite3.connect('db/database.db')
        return conexion
    except Error:
        print(Error)

def createUser (name, lastname, email, password):
    conexion = databaseConexion()
    cursor = conexion.cursor()
    strsql = "INSERT INTO Users (Name, Lastname, Email, Password) VALUES ('{}', '{}', '{}', '{}')".format(name, lastname, email, password)
    cursor.execute(strsql)
    conexion.commit()
    conexion.close()

def getLogs (table, condition):
    conexion = databaseConexion()
    cursor = conexion.cursor()
    if condition == None:
        strql = 'SELECT * FROM {}'.format(table)
    else:
        strql = 'SELECT *FROM {} WHERE {}'.format(table, condition)
    cursor.execute(strql)
    data = cursor.fetchall()
    conexion.close()
    return data
    