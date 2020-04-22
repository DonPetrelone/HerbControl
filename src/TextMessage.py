#Herb Control - Senior Design Project
#Western Michigan University
#Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
#Faculty Advisor: Dr. John Kapenga
#This file defines the function for sending text messages using Twilio account and Raspberry Pi

from twilio.rest import Client

def text(str):
    
    #Twilio account information
    account_sid ="ACc4fe0c6eca7b0d3419fb6d6715970708"
    auth_token = "db5f2a5518117ac95c9f6967bfcae3cb"

    #create a client object
    client = Client(account_sid, auth_token)

    #message information
    #these phone numbers are attached to the Twilio account
    #do not try to change them here before modifying the account settings
    message = client.messages.create(
        to ="+12489312705",
        from_="+12055259682",
        body = str)

    return;
