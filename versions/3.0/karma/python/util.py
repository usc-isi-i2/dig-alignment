import re
from datetime import datetime
from time import mktime, gmtime
import calendar
from urlparse import urlparse
import hashlib
import uuid


def document_url(x):
    """Return the original document URL from the URL in the document version"""
    i = x.find('churl')
    return 'http://' + x[x.find('/', i + 6) + 1:]


def get_current_time():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")


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


def non_whitespace(x):
    """Return the string removing all spaces."""
    y = re.sub(r'\s+', '', x.strip())
    return y


def to_title_case_cleaned(x):
    """Return the string in title case cleaning spaces."""
    y = re.sub(r'\s+', ' ', x.strip())
    return y.title()


def non_ascii_chars(x):
    """Return a set of the non-ascii chars in x"""
    return set(re.sub('[\x00-\x7f]', '', x))


def non_ascii_chars_as_string(x):
    """Return a string containing a comma-separated list of non-ascii chars in x"""
    y = list(non_ascii_chars(x))
    y.sort()
    return ', '.join(y)


def ascii_chars(x, replacement_string=' '):
    """Remove non-ascii chars in x replacing consecutive ones with a single space"""
    return re.sub(r'[^\x00-\x7F]+', replacement_string, x)


def alpha_numeric(x, replacement_string=' '):
    """Replace consecutive non-alphanumeric bya replacement_string"""
    return re.sub('[^A-Za-z0-9]+', replacement_string, x)


def numeric_only(x):
    """Remove non-numeric chars from the string x"""
    return re.sub('[^0-9]+', '', x)


def alpha_only(x):
    """Remove non-alphabetic chars from the string x"""
    return re.sub('[^A-Za-z]+', '', x)


def remove_alpha(x):
    """Remove alphabetic chars from the string x"""
    return re.sub('[A-Za-z]+', '', x)


def alpha_only_preserve_space(x):
    x = re.sub('[^A-Za-z\s]+', '', x)
    y = re.sub(r'\s+', ' ', x.strip())
    return y


def is_symbol(char1):
    if char1.isalnum():
        return False
    return True


def fingerprint_string(x):
    """Make a fingerprint like the one google refine makes"""
    x = alpha_numeric(ascii_chars(x)).lower()
    y = list(set(x.split()))
    y.sort()
    return '_'.join(y)


def uri_from_string(string):
    """Create a valid uri for a string."""
    x = ascii_chars(string, '')
    x = alpha_numeric(x, "_")
    return x


def select_in_out_call(x):
    res = True
    if x == "incall" or x == "notincall" or x == "outcall" or x == "notoutcall" or x == "incalloutcall":
        res = False
    return res


def in_out_call_uri_old(x):
    """Return a URI for a In/Out Call Preference"""
    x = re.sub('[^A-Za-z0-9]+', '', x)
    x = x.lower()
    return 'inOutCallPreference/' + x


def in_out_call_uri(x):
    """Return a URI for a In/Out Call Preference based on the category column"""
    return 'inoutcallpreference/' + x


def organization_uri(id1):
    return "organization/" + str(id1)


def md5_hash(x):
    """Return md5 hash of x"""
    return hashlib.md5(x).hexdigest()


def ten_digit_phone_number(x):
    """Return the 10-digit phone number of a phone, as 10 consecutive digits"""
    return re.sub('[^0-9]+', '', x)


def translate_date(string, in_format, out_format):
    """Convert a date to ISO8601 date format without time"""
    try:
        return datetime.strptime(string.strip(), in_format).date().strftime(out_format)
    except Exception:
        pass
    return ''


def iso8601date(date, date_format=None):
    """Convert a date to ISO8601 date format

input format: YYYY-MM-DD HH:MM:SS GMT (works less reliably for other TZs)
or            YYYY-MM-DD HH:MM:SS.0
or            YYYY-MM-DD
or            epoch (13 digit, indicating ms)
or            epoch (10 digit, indicating sec)
output format: iso8601

"""
    date = date.strip()
    
    if date_format:
        try:
            return datetime.strptime(date, date_format).isoformat()
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
        if 1000000000000 < date < 9999999999999:
            # 13 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date / 1000))).isoformat()
    except:
        pass

    try:
        date = int(date)
        if 1000000000 < date < 9999999999:
            # 10 digit epoch
            return datetime.fromtimestamp(mktime(gmtime(date))).isoformat()
    except:
        pass
    # If all else fails, return input
    return ''


def conver_time_to_epoch(date,format=None):
    date = date.strip()

    if format:
        try:
            calendar.timegm(datetime.strptime(date, format).timetuple())
        except:
            pass
    try:
        return calendar.timegm(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").timetuple())
    except:
        pass
    return ''


def get_year_from_iso_date(iso_date):
    if iso_date:
        return iso_date[0:4]
    return ''


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


def get_text_hash(text):
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


def uuid_uri(prefix):
    """Construct a URI using a UUID"""
    return prefix + str(uuid.uuid1())


def uri_for_userid(prefix, userid):
    """Construct a URI for a user id"""
    return prefix + alpha_numeric(userid.strip().lower())


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


def get_string(string, start, end):
    if len(string) < start:
        return ''
    if end > len(string):
        return string[start:]
    return string[start:end+1]


def get_decimal_coodinate(lat):
    result = 0
    x = get_string(lat, 0, 1)
    if x:
        result += int(x)
    x = get_string(lat, 2, 3)
    if x:
        result += int(x)/float("60")
    x = get_string(lat, 4, 5)
    if x:
        result += int(x)/float("3600")
    return str(result)


def parse_latitude_longitude(latlon):
    # Examples: LATMIN:2310N04350W
    # LATDEC:351025.3N0790125.7W
    idx = latlon.find(":")
    if idx != -1:
        type = latlon[0:idx]
        latlon = latlon[idx+1:]
        idx = latlon.find("-")
        if idx != -1:
            lat = latlon[0:idx-1]
            lon = latlon[idx+2:]
        else:
            latlon = re.sub('[^0-9\.]+', ',', latlon)
            latlons = latlon.split(",")
            lat = latlons[0]
            lon = latlons[1]
        if type == "LATMIN" or type == "LATDEC":
            return [get_decimal_coodinate(lat), get_decimal_coodinate(lon)]
        else:
            return [lat, lon]

    return [-1, -1]
