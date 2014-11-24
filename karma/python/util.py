import re
from datetime import datetime
from time import mktime, gmtime


def documentUrl(x):
    "Return the original document URL from the URL in the document version"
    i = x.find('churl')
    return 'http://' + x[x.find('/', i + 6) + 1:]


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


def phoneExchange(phonenumber):
    "Return the first six digits of a phone if it is a 10-digit USA phone, ie, starts with 1-."
    result = ''
    if phonenumber.startswith("+1-"):
        tenDigitPhone = phonenumber[3:]
        if tenDigitPhone.isdigit() and len(tenDigitPhone.decode("utf-8")) == 10:
            result = tenDigitPhone[0:6]
    else:
        if phonenumber.isdigit() and len(phonenumber.decode("utf-8")) == 10:
            if isUSAreaCode(phonenumber):
                result = phonenumber[0:6]
    return result


def phoneExchangeUri(phonenumber):
    "Return the URI of a phone exchange so that we can join with the phone exchange data"
    x = phoneExchange(phonenumber)
    if len(x) > 0:
        return "phone/exchange/" + x
    else:
        return ''


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

    return re.sub(r'[^\x00-\x7F]+', ' ', x)


def alphaNumeric(x):
    "Replace consecutive non-alphanumeric bya single space"
    return re.sub('[^A-Za-z0-9]+', ' ', x)


def numericOnly(x):
    "Remove non-numeric chars from the string x"
    return re.sub('[^0-9]+', '', x)


def alphaOnly(x):
    "Remove non-alphabetic chars from the string x"
    return re.sub('[^A-Za-z]+', '', x)


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


def inOutCallUriOld(x):
    "Return a URI for a In/Out Call Preference"
    import re

    x = re.sub('[^A-Za-z0-9]+', '', x)
    x = x.lower()
    return 'inOutCallPreference/' + x


def inOutCallUri(x):
    "Return a URI for a In/Out Call Preference based on the category column"
    return 'inoutcallpreference/' + x


def md5Hash(x):
    "Return md5 hash of x"
    import hashlib

    return hashlib.md5(x).hexdigest()


def tenDigitPhoneNumber(x):
    """Return the 10-digit phone number of a phone, as 10 consecutive digits"""
    return re.sub('[^0-9]+', '', x)


def iso8601date(date, format="%Y-%m-%d %H:%M:%S %Z"):
    """Convert a date to ISO8601 date format

input format: YYYY-MM-DD HH:MM:SS GMT (works less reliably for other TZs)
or            YYYY-MM-DD HH:MM:SS.0
or            YYYY-MM-DD
or            epoch (13 digit, indicating ms)
or            epoch (10 digit, indicating sec)
output format: iso8601

"""

    try:
        return datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z").isoformat()
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
    return date

