from config.py import *
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


client = Client(ACCOUNT_SID, AUTH_TOKEN)



message = client.messages \
    .create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
         to='+15558675310'
     )

print(message.sid)

