# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('853a9a70bd2c42508bfcb17a60105477')

# Send the value 100 to a feed called 'Foo'.
for i in range(10):
	aio.send('testGraph', i)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
for i in range(10):
	data = aio.receive('testGraph')
	print('Received value: {0}'.format(data.value))

