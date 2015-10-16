from thread import start_new_thread
from django.conf import settings
from raven import Client

import pika, time, json

raven_client = Client(settings.RAVEN_CONFIG['dsn'])

RABBIT_MQ_URL = settings.CLOUDAMQP_URL
url_parameters = pika.connection.URLParameters(RABBIT_MQ_URL)
properties = pika.BasicProperties(
   content_type='application/json',
   content_encoding='utf-8',
   delivery_mode=2,
)

connection = None
in_channel = None
out_channel = None

def test_connection():
	return connection != None and connection.is_open

#
# start consuming incoming events
#
def start_consuming():
	global in_channel, out_channel, connection
	try:
		# start consuming messaged
		in_channel.start_consuming()
	except:
		# reconnect when connection is lost
		in_channel = None
		out_channel = None
		connection = None
		connect()

	return connection and connection.is_open

#
# 
#
def connect():
	time.sleep(5)

	global connection, in_channel, out_channel
	connection = pika.BlockingConnection(url_parameters)
	in_channel = connection.channel()
	out_channel = connection.channel()

	# attach receiving handlers to channel
	for queue in receivers:
		handler = receivers[queue]
		attach_handler(queue, handler)
	start_new_thread(start_consuming, ());

start_new_thread(connect, ())


#
# message receiving
#
def attach_handler(queue, handler):
	def callback(ch, method, properties, body):
		try:
			receivers[queue](json.loads(body))
			ch.basic_ack(method.delivery_tag)
		except:
			raven_client.captureException()
			ch.basic_nack(method.delivery_tag, False, False)
	if in_channel:
		in_channel.basic_consume(callback, queue=queue)


receivers = {}
def receive_messages(queue, handler):

	if receivers.get(queue,None):
		return
	receivers[queue] = handler

	attach_handler(queue,handler)



#
# message sending
#
message_queue = []

def send_message(exchange, message):
	message_queue.append({
		'exchange': exchange,
		'message': message
		})

#
# 
#
def process_messages():
	while True:
		try:
			if len(message_queue) and out_channel:
				message = message_queue.pop(0)
				out_channel.publish(
					exchange=message['exchange'], 
					routing_key='', 
					body=json.dumps(message['message']),
					properties=properties
				)
		except:
			message_queue.insert(0, message)
			raven_client.captureException()

		time.sleep(2)

start_new_thread(process_messages, ())
