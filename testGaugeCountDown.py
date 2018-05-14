# Import library and create instance of REST client.
import time
from Adafruit_IO import Client
aio = Client('853a9a70bd2c42508bfcb17a60105477')

# Send the value 100 to a feed called 'Foo'.
for i in range(100,0,-1):
	aio.send('testGaugeCountDown', i)
	print(i)
	time.sleep(3)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
for i in range(10):
	data = aio.receive('testGaugeCountDown')
	print('Received value: {0}'.format(data.value))

data = aio.data('testGaugeCountDown')

for d in data:
	print(d)
