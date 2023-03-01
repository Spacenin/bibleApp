import json
from twilio.rest import Client
import bible

#Send message with the obtained verse
def sendMsg():
    #Get twilio information
    with open("/home/pi/Code/pys/bibleApp/secrets.json") as secretsFile:
        secretData = json.load(secretsFile)

    #Get random verse
    verse = bible.getVerse(secretData["bible"]["api_key"])

    #Setup connection
    client = Client(secretData["twilio"]["account_sid"], secretData["twilio"]["auth_token"])

    #Send message
    client.messages.create(
        body=composeMsg(verse),
        from_=secretData["twilio"]["twi_number"],
        to=secretData["twilio"]["my_number"]
    )

#Create the message string
def composeMsg(verse):
    message = \
        "Good morning! Today's Bible verse:\n\n" + \
        verse["title"] + "\n" + \
        verse["text"] + "\n\n" + \
        "Hope you have a blessed day!"
    
    return(message)