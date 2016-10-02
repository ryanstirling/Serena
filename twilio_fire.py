import os
from twilio import twiml
from twilio.rest import TwilioRestClient

TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
USER_NUMBER = os.environ.get('USER_NUMBER', None)

twilio_client = TwilioRestClient()

# response = twiml.Response()
    
    # if request.form['From'] == USER_NUMBER:
    #     message = request.form['Body']

    #     if message == "Hi":
    # 		response.message("Hey there, how is your day going?")
    # 		return str(response)

def sendText():

	twilio_client.messages.create(
		to="+17329270311", 
		from_="+13474785618",
		body="Sorry, Devin! Have a great day!"
	)

	print "Sent!\n"


sendText()
