#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This file contains a method that connects to the database, performs an insert query than disconnects.

import sqlite3

def dbConnect(airTemp, airHum, soil, dateTime):

    #create database connection
    conn = sqlite3.connect('HerbControl.db')

    #cursor object which allows the execution of queries
    c = conn.cursor()

    #Execute the insert query with the parameters
    c.execute("INSERT INTO ...")

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    return