from fbchat import Client, log
from fbchat.models import *
import requests

def sendMsg(email, password, name, msg):

	client = Client(email, password)

	if not client.isLoggedIn():
		print("Client not logged in.")

	users = client.searchForUsers(str(name))
	user = users[0]

	#print(user)

	client.send(Message(str(msg)), user.uid, thread_type=ThreadType.USER)

	client.logout()

def sendSms(email, password, phone, platform):
	class EchoBot(Client):
	    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
	        self.markAsDelivered(thread_id, message_object.uid)
	        self.markAsRead(thread_id)

	        url = "https://xingluke.api.stdlib.com/wuphf-twilio@dev/"

	        
			#requests.post(url, data={"phone": phone, "sender": sender, "sender": sender})
	        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
	        #print(type(message_object))
	        #print(message_object.text)

	        msg = message_object.text
	        #print(self.fetchAllUsersFromThreads([thread_id]))
	        #print(type(author_id))
	        #print(author_id)
	        #print(type(thread_type))
	        obj = {'msg': msg, 'platform': platform, 'author': author_id, 'phone': phone}

	        requests.post(url, data=obj)

	        # If you're not the author, echo
	        #if author_id != self.uid:
	        #    self.send(message_object, thread_id=thread_id, thread_type=thread_type)
#1105803422

	client = EchoBot(email, password)
	client.listen()
