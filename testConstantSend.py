# Import library and create instance of REST client.
import time
from Adafruit_IO import Client
aio = Client('853a9a70bd2c42508bfcb17a60105477')

def testConstantSend(status):
	# Send the ON/OFF status to a visible graph feed.
	aio.send('testConstantSend', status)
	print(status)
