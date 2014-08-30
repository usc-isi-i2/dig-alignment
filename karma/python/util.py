def documentUrl(x):
	"Return the original document URL from the URL in the document version"
	i = x.find('churl')
	return 'http://'+x[x.find('/',i+6)+1:]


def countryUri(x):
	"Return a URI for a country given its name."
	import re
	x = re.sub('[^A-Za-z0-9]+', '', getValue("Country"))
	return x.lower()