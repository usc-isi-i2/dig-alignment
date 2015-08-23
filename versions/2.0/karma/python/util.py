import re
from datetime import datetime, date
from time import mktime, gmtime
from urlparse import urlparse
import hashlib
import uuid

def documentUrl(x):
    "Return the original document URL from the URL in the document version"
    i = x.find('churl')
    return 'http://' + x[x.find('/', i + 6) + 1:]


def getCurrentTime():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")


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

def nonWhitespace(x):
    "Return the string removing all spaces."
    import re

    y = re.sub(r'\s+', '', x.strip())
    return y

def toTitleCaseCleaned(x):
    "Return the string in title case cleaning spaces."
    import re

    y = re.sub(r'\s+', ' ', x.strip())
    return y.title()

def nonAsciiChars(x):
    "Return a set of the non-ascii chars in x"
    import re

    return set(re.sub('[\x00-\x7f]', '', x))


def nonAsciiCharsAsString(x):
    "Return a string containing a comma-separated list of non-ascii chars in x"
    y = list(nonAsciiChars(x))
    y.sort()
    return ', '.join(y)


def asciiChars(x, replacement_string=' '):
    "Remove non-ascii chars in x replacing consecutive ones with a single space"
    import re

    return re.sub(r'[^\x00-\x7F]+', replacement_string, x)


def alphaNumeric(x, replacement_string=' '):
    "Replace consecutive non-alphanumeric bya replacement_string"
    return re.sub('[^A-Za-z0-9]+', replacement_string, x)


def numericOnly(x):
    "Remove non-numeric chars from the string x"
    return re.sub('[^0-9]+', '', x)


def alphaOnly(x):
    "Remove non-alphabetic chars from the string x"
    return re.sub('[^A-Za-z]+', '', x)

def removeAlpha(x):
    "Remove alphabetic chars from the string x"
    return re.sub('[A-Za-z]+', '', x)


def alphaOnlyPreserveSpace(x):
    x = re.sub('[^A-Za-z\s]+', '', x)
    y = re.sub(r'\s+', ' ', x.strip())
    return y

def isSymbol(char1):
    if char1.isalnum():
        return False
    return True

def fingerprintString(x):
    "Make a fingerprint liek the one google refine makes"
    x = alphaNumeric(asciiChars(x)).lower()
    y = list(set(x.split()))
    y.sort()
    return '_'.join(y)

def uri_from_string(str, prefix):
    """Create a valid uri for a string."""
    x = asciiChars(str, '');
    x = alphaNumeric(x, "_");
    return x;

def selectInOutCall(x):
    res = True
    if (x == "incall" or x == "notincall" or x == "outcall" or x == "notoutcall" or x == "incalloutcall"):
        res = False
    return res


def inOutCallUriOld(x):
    "Return a URI for a In/Out Call Preference"
    import re

    x = re.sub('[^A-Za-z0-9]+', '', x)
    x = x.lower()
    return 'inOutCallPreference/' + x


def inOutCallUri(x):
    "Return a URI for a In/Out Call Preference based on the category column"
    return 'inoutcallpreference/' + x

def organization_uri(id):
    return "organization/" + str(id)

def md5Hash(x):
    "Return md5 hash of x"

    return hashlib.md5(x).hexdigest()


def tenDigitPhoneNumber(x):
    """Return the 10-digit phone number of a phone, as 10 consecutive digits"""
    return re.sub('[^0-9]+', '', x)


def translate_date(str, in_format, out_format):
    """Convert a date to ISO8601 date format without time"""
    try:
        return datetime.strptime(str.strip(), in_format).date().strftime(out_format)
    except Exception:
        pass
    return ''


def iso8601date(date, format=None):
    """Convert a date to ISO8601 date format

input format: YYYY-MM-DD HH:MM:SS GMT (works less reliably for other TZs)
or            YYYY-MM-DD HH:MM:SS.0
or            YYYY-MM-DD
or            epoch (13 digit, indicating ms)
or            epoch (10 digit, indicating sec)
output format: iso8601

"""
    date = date.strip()
    
    if format:
        try:
            return datetime.strptime(date, format).isoformat()
        except Exception:
            pass

    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z").isoformat()
    except Exception:
        pass

    try:
        return datetime.strptime(date, "%A, %b %d, %Y").isoformat()
    except Exception:
        pass

    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.0").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%Y-%m-%d").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%b %d, %Y").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%B %d, %Y").isoformat()
    except:
        pass

    try:
        return datetime.strptime(date, "%B %d, %Y %I:%M %p").isoformat()
    except:
        pass
        
    try:
        date = int(date)
        if 1000000000000 < date and date < 9999999999999:
            # 13 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date / 1000))).isoformat()
    except:
        pass

    try:
        date = int(date)
        if 1000000000 < date and date < 9999999999:
            # 10 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date))).isoformat()
    except:
        pass
    # If all else fails, return input
    return ''


def getYearFromISODate(isoDate):
    if isoDate:
        return isoDate[0:4]
    return ''

def getWebsiteDomain(url):
    parsed_uri = urlparse(url)
    if parsed_uri:
        domain = parsed_uri.netloc
        if domain:
            if domain.startswith("www."):
                domain = domain[4:]
            return domain
    return ''

def getTextHash(text):
    if text:
        return hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
    return ''

def first_non_null(*args):
    """return the first non null value in the arguments supplied"""
    for x in args:
        if x != '':
            return x
    return ''

def uri_from_fields(prefix, *fields):
    """Construct a URI out of the fields, concatenating them after removing offensive characters.
    When all the fields are empty, return empty"""

    str = '_'.join(alphaNumeric(f.strip().lower(),'') for f in fields)

    if len(str) == len(fields)-1:
        return ''

    return prefix + str


def uri_from_url_timestamp(url,timestamp):
    """Construct a URI from the URL and timestamp"""
    return hashlib.sha1(url.encode('utf-8')).hexdigest()+'_'+numericOnly(timestamp)


def uri_from_url(url):
    """Construct a URI from the URL"""
    return hashlib.sha1(url.encode('utf-8')).hexdigest()


def uuid_uri(prefix):
    """Construct a URI using a UUID"""
    return prefix + str(uuid.uuid1())


def get_weapons(*texts):
    atf_weapons = get_atf_weapons(*texts)
    keywords = get_keywords(*texts)
    return ("%s|%s" % (atf_weapons, keywords)).strip("|")


def uri_for_userid(prefix, userid):
  """Construct a URI for a user id"""
  return prefix + alphaNumeric(userid.strip().lower())

def select_if_empty(value):
  """Return true if the value is empty"""
  try:
    is_empty = (value.strip()=='')
    return is_empty
    pass
  except Exception:
    return false


def price_quantity_us_number(price):
    """Extract the numeric quantity of the price, 
    assuming the number uses dot for decimal and comma for thousands, etc."""
    p = re.sub('[^0-9.]', '', price.strip())
    return p


def price_currency(price, default_currency="USD"):
    """Return the currency of a price specification.
    Should be enhanced to deal with other currencies and bitcoin"""

    if price_quantity_us_number(price) == '':
        return ''

    p = price.strip()
    if "$" in price:
        return 'USD'

    #add sophistication
    return default_currency
