import time, os
from datetime import datetime
from twilio.rest import TwilioRestClient 


# Temporary Global Variables
ACCOUNT_SID = os.environ.get('TWILIO_SID')
AUTH_TOKEN = os.environ.get('TWILIO_TOKEN')
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

all_chunks = []

class MessageChunk(object):
	question = ""
	response = []
	lastInteraction = datetime.min



# Initiate Message Cycle
def questionCycle(question):
	chunk = MessageChunk()
	all_chunks.append(chunk)
	chunk.question = question

	# Initialize lastInteraction before sending question
	messages = client.messages.list()
	for m in messages:
			if (m.date_sent > chunk.lastInteraction):
				chunk.lastInteraction = m.date_sent

	# Send question
	sendQuestion(question)

	# Accumulate new responses
	while (True):
		print("Check for new incoming message...")

		messages = client.messages.list(from_="17036786728",)

		for m in messages:
			if (m.date_sent > chunk.lastInteraction):
				chunk.lastInteraction = m.date_sent
				chunk.response.append(m.body)
				print m.body


		print chunk.response
		time.sleep(3)




def sendQuestion(question):

	out = client.messages.create(
		to="+17036786728", 
		from_="+13474785618",
		body=question, 
	)

	print "We sent the user a question! \n"


# MAIN
questionCycle("How is the presentation going?")