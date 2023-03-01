import sms

#This is kinda just a wrapper for the sending of the message
def sendVerse():
    sms.sendMsg()

#Ensure it runs the correct function if called
if __name__ == "__main__":
    sendVerse()