from thread import start_new_thread
from django.conf import settings
from raven import Client

import pika, time, json

raven_client = Client(settings.RAVEN_CONFIG['dsn'])

RABBIT_MQ_URL = settings.CLOUDAMQP_URL
properties = pika.BasicProperties(
   content_type='application/json',
   content_encoding='utf-8',
   delivery_mode=2,
)

connection = None

def test_connection():
	return connection != None and connection.is_open

#
# 
#
def connect():

	if not RABBIT_MQ_URL: return

	while True:
		time.sleep(5)
		try:

			if not RABBIT_MQ_URL:
				return
			global connection

			url_parameters = pika.connection.URLParameters(RABBIT_MQ_URL)
			connection = pika.BlockingConnection(url_parameters)
			channel = connection.channel()

			# attach receiving handlers to channel
			for queue in receivers:
				handler = receivers[queue]
				attach_handler(queue, handler, channel)
		except:
			pass

start_new_thread(connect, ())


#
# message receiving
#
def attach_handler(queue, handler, channel):
	def callback(ch, method, properties, body):
		try:
			receivers[queue](json.loads(body))
			ch.basic_ack(method.delivery_tag)
		except:
			raven_client.captureException()
			
	channel.basic_consume(callback, queue=queue)


receivers = {}
def receive_messages(queue, handler):

	if receivers.get(queue,None):
		return
	receivers[queue] = handler




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
			if len(message_queue):

				message = message_queue.pop(0)

				url_parameters = pika.connection.URLParameters(RABBIT_MQ_URL)
				connection = pika.BlockingConnection(url_parameters)
				channel = connection.channel()

				channel.publish(
					exchange=message['exchange'], 
					routing_key='', 
					body=json.dumps(message['message']),
					properties=properties
				)

				connection.close()
		except:
			message_queue.insert(0, message)
			raven_client.captureException()

		time.sleep(2)

start_new_thread(process_messages, ())
