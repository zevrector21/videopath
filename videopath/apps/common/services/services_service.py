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


def test_connection():
	return connection and connection.is_open

#
# connection
#
send_channel = None
receive_channel = None
try:
	connection = pika.BlockingConnection(url_parameters)
	send_channel = connection.channel()
	receive_channel = connection.channel()
except:
	raven_client.captureException()


# start consuming receive channel
def start_consuming(channel):
	channel.start_consuming()
if receive_channel:
	start_new_thread(start_consuming, (receive_channel,))


#
# message receiving
#
receivers = {}
def receive_messages(queue, handler):

	if receivers.get(queue,None):
		return

	def callback(ch, method, properties, body):
		try:
			receivers[queue](json.loads(body))
			ch.basic_ack(method.delivery_tag)
		except:
			raven_client.captureException()
			ch.basic_nack(method.delivery_tag, False, False)

	receivers[queue] = handler
	if receive_channel:
		receive_channel.basic_consume(callback, queue=queue)



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
			if len(message_queue) and send_channel:
				message = message_queue.pop(0)
				send_channel.publish(
					exchange=message['exchange'], 
					routing_key='', 
					body=json.dumps(message['message']),
					properties=properties
				)
		except:
			message_queue.insert(0, message)
			raven_client.captureException()

		time.sleep(1)

start_new_thread(process_messages, ())
