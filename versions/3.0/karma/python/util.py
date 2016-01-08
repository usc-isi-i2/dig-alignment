import re
from urlparse import urlparse
import hashlib


def convert_to_float_string(number):
    """return the number as a float string, eg: scientific notation numbers"""
    return '{0:.15f}'.format(float(number))


def document_url(x):
    """Return the original document URL from the URL in the document version"""
    i = x.find('churl')
    return 'http://' + x[x.find('/', i + 6) + 1:]





def country_uri(x):
    """Return a URI for a country given its name."""
    x = re.sub('[^A-Za-z0-9]+', '', x)
    return x.lower()


def person_name_uri(x):
    """Return a URI for a person name."""
    x = re.sub('[^A-Za-z0-9]+', '', x.strip())
    return x.lower()


def to_title_case_if_upper(x):
    """Return the string in title case if it is all upper, otherwise leave capitalization alone."""
    x = x.strip()
    if x.isupper():
        return x.title()
    else:
        return x



def to_title_case_cleaned(x):
    """Return the string in title case cleaning spaces."""
    y = re.sub(r'\s+', ' ', x.strip())
    return y.title()






















def get_website_domain(url):
    parsed_uri = urlparse(url)
    if parsed_uri:
        domain = parsed_uri.netloc
        if domain:
            if domain.startswith("www."):
                domain = domain[4:]
            return domain
    return ''


def get_website_domain_only(url):
    parsed_uri = urlparse(url)
    if parsed_uri:
        domain = parsed_uri.netloc
        if domain:
            if domain.startswith("www."):
                domain = domain[4:]

            idx = domain.find('.')
            if idx != -1:
                domain2 = domain[idx+1:]
                if domain2.find('.') != -1:
                    domain = domain2
                
            return domain
    return ''





def uri_from_fields(prefix, *fields):
    """Construct a URI out of the fields, concatenating them after removing offensive characters.
    When all the fields are empty, return empty"""

    string = '_'.join(alpha_numeric(f.strip().lower(), '') for f in fields)

    if len(string) == len(fields)-1:
        return ''

    return prefix + string


def uri_from_url_timestamp(url, timestamp):
    """Construct a URI from the URL and timestamp"""
    return hashlib.sha1(url.encode('utf-8')).hexdigest() + '_' + numeric_only(timestamp)


def uri_from_url(url):
    """Construct a URI from the URL"""
    return hashlib.sha1(url.encode('utf-8')).hexdigest()





def select_if_empty(value):
    """Return true if the value is empty"""
    try:
        is_empty = (value.strip() == '')
        return is_empty
        pass
    except Exception:
        return False


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
    if "$" in p:
        return 'USD'

    # add sophistication
    return default_currency


def add_state(location, state):
    """If the location has the state, then do nothing, otherwise add the given state"""

    loc = location.strip()

    if loc == '':
        return ''

    if state in loc.lower():
        return loc
    else:
        return loc + ", " + state


def get_eye_hair_feature_name(name, value):
    if value.strip() == "NONE":
        return ''
        
    if name.strip() == "person_haircolor" or value.strip() == "hairColor":
        return "hairColor"
    elif name.strip() == "person_eyecolor" or value.strip() == "eyeColor":
        return "eyeColor"
    return ''








