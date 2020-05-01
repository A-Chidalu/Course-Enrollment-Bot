from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, PHONE_NUMER
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("message_to_send")
p = parser.parse_args()
message_body = p.message_to_send

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure



client = Client(ACCOUNT_SID, AUTH_TOKEN)


message = client.messages \
    .create(
         body=message_body,
         from_=TWILIO_NUMBER,
         to=PHONE_NUMER
     )

print(message.sid)

