from thread import start_new_thread
from django.conf import settings
import pika, time, json

RABBIT_MQ_URL = settings.CLOUDAMQP_URL
url_parameters = pika.connection.URLParameters(RABBIT_MQ_URL)

properties = pika.BasicProperties(
   content_type='application/json',
   content_encoding='utf-8',
   delivery_mode=2,
)


def message_callback(queue, callback):
	pass


def test_connection():
	connection = pika.BlockingConnection(url_parameters)
	is_open = connection.is_open
	connection.close()
	return is_open



def receive_messages():
	pass

#
# queue message
#
message_queue = []

def send_message(exchange, message):
	message_queue.append({
		'exchange': exchange,
		'message': message
		})

#
# manage processing of messages
#
def process_messages():

	def connect():
		connection = pika.BlockingConnection(url_parameters) 
		return connection.channel()

	channel = None
	while True:
		
		if not channel:
			try:
				channel = connect()
			except pika.exceptions.ConnectionClosed:
				pass

		try:
			if len(message_queue) and channel:
				message = message_queue.pop(0)
				channel.publish(
					exchange=message['exchange'], 
					routing_key='', 
					body=json.dumps(message['message']),
					properties=properties
				)
		except pika.exceptions.ConnectionClosed:
			channel = None
			message_queue.insert(0, message)

		time.sleep(1)

start_new_thread(process_messages, ())
start_new_thread(receive_messages, ())
