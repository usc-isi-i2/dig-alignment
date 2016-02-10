

#########################

def bd_makeDateUri(x):
	""""Return a string for a data that can be used as a URI.
	InferLink provides the dates in the format 'Mon, Mar 31, 2014, 12:38:14'
	without a timezone. We need a robust date parser.

	The current code just makes something that's unique even thoug it does not
	look like a date.
	"""
	import re
	x = re.sub('[^A-Za-z0-9]+', '', x)
	x = x.lower()
	return x


def dateToZulu(x):
	"""Return date in Zulu format

	NOT IMPLEMENTED.
	"""
	return x;