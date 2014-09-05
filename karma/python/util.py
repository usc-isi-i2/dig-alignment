def documentUrl(x):
	"Return the original document URL from the URL in the document version"
	i = x.find('churl')
	return 'http://'+x[x.find('/',i+6)+1:]


def countryUri(x):
	"Return a URI for a country given its name."
	import re
	x = re.sub('[^A-Za-z0-9]+', '', x)
	return x.lower()


def personNameUri(x):
	"Return a URI for a person name."
	import re
	x = re.sub('[^A-Za-z0-9]+', '', x.strip())
	return x.lower()


def toTitleCaseIfUpper(x):
	"Return the string in title case if it is all upper, otherwise leave capitalization alone."
	x = x.strip()
	if x.isupper():
	    return x.title()
	else:
	    return x


def toTitleCaseCleaned(x):
	"Return the string in title case cleaning spaces."
	import re
	y = re.sub(r'\s+', ' ', x.strip())
	return y.title()


def phoneExchange(tenDigitPhone):
	"Return the first six digits of a phone if it is a 10-digit phone."
	if tenDigitPhone.isdigit() and len(tenDigitPhone.decode("utf-8")) == 10:
	    return tenDigitPhone[0:6]


def nonAsciiChars(x):
	"Return a set of the non-ascii chars in x"
	import re
	return set(re.sub('[\x00-\x7f]', '', x))

def nonAsciiCharsAsString(x):
	"Return a string containing a comma-separated list of non-ascii chars in x"
	y = list(nonAsciiChars(x))
	y.sort()
	return ', '.join(y)

def asciiChars(x):
	"Remove non-ascii chars in x replacing consecutive ones with a single space"
	import re
	return re.sub(r'[^\x00-\x7F]+',' ', x)

def alphaNumeric(x):
	"Replace consecutive non-alphanumeric bya single space"
	return re.sub('[^A-Za-z0-9]+', ' ', x)


def fingerprintString(x):
	"Make a fingerprint liek the one google refine makes"
	x = alphaNumeric(asciiChars(x)).lower()
	y = list(set(x.split()))
	y.sort()
	return '_'.join(y)

def selectInOutCall(x):
	res = True
	if (x == "incall" or x == "notincall" or x == "outcall" or x == "notoutcall" or x == "incalloutcall"):
		res = False
	return res

def inOutCallUri(x):
	"Return a URI for a In/Out Call Preference"
	import re
	x = re.sub('[^A-Za-z0-9]+', '', x)
	x = x.lower()
	return 'inOutCallPreference/' + x

def md5Hash(x):
	"Return md5 hash of x"
	import hashlib
	return hashlib.md5(x).hexdigest()
