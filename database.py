import sqlite3
from cryptography.fernet import Fernet
import sys

key = "Be1PA8snHgb1DS6oaWek62WLE9nxipFw3o3vB4uJ8ZI="  # "secret key" This must be kept secret
cipher_suite = Fernet(key)  # This class provides both encryption and decryption facilities.
key2 = 5

def conectionDB(func):
    """This is a decorator to open and close the database"""
    def wrapper(*args, **kwargs):
        global myConection
        global myCursor
        myConection = sqlite3.connect("encryptit.db")
        myCursor = myConection.cursor()
        result = func(*args, **kwargs)
        myConection.commit()
        myConection.close()
        return result
    return wrapper

@conectionDB
def crearBD():
    """This is a function to create the database if is not yet created"""
    try:
        myCursor.execute('''
            CREATE TABLE USERS (
            MAIL text UNIQUE,
            PASSWORD text,
            NOMBRE text,
            CLAVE text)
            ''')

        myCursor.execute('''
            CREATE TABLE PASSWORDS_DATA (
            USER text,
            NAME text,
            PASSWORD text,
            NOTES text,
            TIPO text)
            ''')

    except sqlite3.OperationalError:
        pass

@conectionDB
def loginUser(mail, password):
    """ Function to login
        @Return: "yes" if the password is correct, "no" if it is incorrect, "error"  if it does not exist"""
    myCursor.execute("SELECT PASSWORD FROM USERS WHERE MAIL='"+mail+"'")
    passwordDB = myCursor.fetchall()

    try:
        passwordDB = cipher_suite.decrypt(passwordDB[0][0])
        passwordDB = passwordDB.decode("utf-8")
        if passwordDB == password:
            return "yes"
        else:
            return "no"

    except IndexError:
        return "error"

@conectionDB
def createUser(mail, password, nombre, clave):
    """Function to create new user"""
    password = cipher_suite.encrypt(bytes(password, encoding='utf-8'))
    data = (mail, password, nombre, clave)
    myCursor.execute("INSERT INTO USERS VALUES (:MAIL, :PASSWORD, :NOMBRE, :CLAVE)", {
    'MAIL': mail,
    'PASSWORD': password,
    'NOMBRE': nombre,
    'CLAVE': clave
    })
    myConection.commit()

@conectionDB
def insertPasswordData(mail, name, password, notes, tipo):
    """Function to save new password in the storage"""
    password = cipher_suite.encrypt(bytes(password, encoding='utf-8'))
    data = (mail, name, password, notes, tipo)
    # myCursor.execute("INSERT INTO PASSWORDS_DATA VALUES(?,?,?,?)", data)
    myCursor.execute("INSERT INTO PASSWORDS_DATA VALUES (:USER, :NAME, :PASSWORD, :NOTES, :TIPO)", {
    'USER': mail,
    'NAME': name,
    'PASSWORD': password,
    'NOTES': notes,
    'TIPO':tipo
    })
    myConection.commit()

@conectionDB
def readPasswords(mail):
    """ Read all passwords from the user storage
        @return: A list, in each row there is a password with its corresponding name and notes"""
    myCursor.execute("SELECT NAME,PASSWORD,NOTES,TIPO FROM PASSWORDS_DATA WHERE USER='"+mail+"'")
    passwords = myCursor.fetchall()
    return passwords

@conectionDB
def deletePassword(mail, name):
    """ Delete a password from the user storage
        @param: the user and the name associated with the password"""
    myCursor.execute("DELETE FROM PASSWORDS_DATA WHERE USER='"+mail+"' AND NAME='"+name+"'")

@conectionDB
def deleteallPassword(mail):
    myCursor.execute("DELETE FROM PASSWORDS_DATA WHERE USER='"+mail+"'")

@conectionDB
def readNotes(user, name):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT NOTES FROM PASSWORDS_DATA WHERE USER='"+user+"' AND NAME='"+name+"'")
    notes = myCursor.fetchall()
    return notes

@conectionDB
def readName(user, name):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT NAME FROM PASSWORDS_DATA WHERE USER='"+user+"' AND NAME='"+name+"'")
    notes = myCursor.fetchall()
    return notes

@conectionDB
def loginClave(mail, clave):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT CLAVE FROM USERS WHERE MAIL='"+mail+"'")
    claveDB = myCursor.fetchall()

    try:
        claveDB = claveDB[0][0]
        if claveDB == clave:
            return "yes"
        else:
            return "no"

    except IndexError:
        return "error"

@conectionDB
def readContradesencriptada(user, name):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT PASSWORD FROM PASSWORDS_DATA WHERE USER='"+user+"' AND NAME='"+name+"'")
    notes = myCursor.fetchall()
    return notes


@conectionDB
def readmail(user):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT MAIL FROM USERS WHERE NOMBRE='"+user+"'")
    notes = myCursor.fetchall()
    return notes

@conectionDB
def readnombre(user):
    """ Read a password notes
        @param: the user and the name associated with the password"""
    myCursor.execute("SELECT MAIL FROM USERS WHERE MAIL='"+user+"'")
    notes = myCursor.fetchall()
    return notes

@conectionDB
def seleccionarnombre(user):
    myCursor.execute("SELECT NAME FROM PASSWORDS_DATA WHERE USER ='"+user+"'")
    notes = myCursor.fetchall()
    return notes


@conectionDB
def readPasswords2(mail):
    """ Read all passwords from the user storage
        @return: A list, in each row there is a password with its corresponding name and notes"""
    myCursor.execute("SELECT PASSWORD,NOTES,TIPO FROM PASSWORDS_DATA WHERE USER='"+mail+"'")
    passwords = myCursor.fetchall()
    return passwords
