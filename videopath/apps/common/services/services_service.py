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

#
# connection
#
connection = pika.BlockingConnection(url_parameters)
def get_channel():
	return connection.channel()


#
# message receiving
#
receivers = {}
def receive_messages(queue, handler):

	if receivers.get(queue,None):
		return

	def callback(ch, method, properties, body):
		receivers[queue](body)
		ch.basic_ack(method.delivery_tag)

	receivers[queue] = handler
	channel = get_channel()
	channel.basic_consume(callback, queue=queue)

	def start_consuming(channel):
		channel.start_consuming()

	start_new_thread(start_consuming, (channel,))

	
def receive(result):
	print 'received'
	print result
receive_messages('q-transcoder', receive)




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
			channel = get_channel()
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
