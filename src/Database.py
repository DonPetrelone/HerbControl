#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This file contains a method that connects to the database, performs an insert query than disconnects.

import sqlite3

def dbInsert(airTemp, airHum, soil):

    #create database connection
    conn = sqlite3.connect('flask-webpage/instance/flaskr.sqlite')

    #cursor object which allows the execution of queries
    c = conn.cursor()

    #Execute the insert query with the parameters
    c.execute('INSERT INTO values (soilMoisture, airTemperature, airHumidity)', soil, airTemp, airHum)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

    return

def dbGetRanges():

    #create a connection to the db
    conn = sqlite3.connect('flask-webpage/instance/flaskr.sqlite')

    #create a cursor object to allow for queries
    c = conn.cursor()

    #query the values from the air temperatue ranges
    c.execute('SELECT airTempHighDanger FROM ranges')
    airTempHighDanger = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airTempHighWarning FROM ranges')
    airTempHighWarning = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airTempGood FROM ranges')
    airTempHighGood = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airTempLowWarning FROM ranges')
    airTempLowWarning = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airTempLowDanger FROM ranges')
    airTempLowDanger = int(''.join(map(str, c.fetchone())))

    # query the values from the air humidity ranges
    c.execute('SELECT airHumHighDanger FROM ranges')
    airHumHighDanger = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airHumHighWarning FROM ranges')
    airHumHighWarning = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airHumGood FROM ranges')
    airHumHighGood = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airHumLowWarning FROM ranges')
    airHumLowWarning = int(''.join(map(str, c.fetchone())))

    c.execute('SELECT airHumLowDanger FROM ranges')
    airHumLowDanger = int(''.join(map(str, c.fetchone())))

    #close the connection with the db
    conn.close()

    return airTempHighDanger, airTempHighWarning, airTempHighGood, airTempLowWarning, airTempLowDanger, airHumHighDanger, \
           airHumHighWarning, airHumHighGood, airHumLowWarning, airHumLowDanger
