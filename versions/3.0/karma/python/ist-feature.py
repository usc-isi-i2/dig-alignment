
import re
from urllib import quote



def phone_uri(x):
    """Return the uri for a phone
    as countrycode-phone
    Use 'x-' as country code if not present in the number
    """
    x = clean_phone(x)
    if len(x) > 0:
        dashIdx = x.find('-');
        if(dashIdx != -1):
            return "phonenumber/" + x[1:]
        return "phonenumber/x-" + x
    return ''



# age   15647
def clean_age(x):
    """Return the clean age
    """
    stripped = x.strip().lower()
    # take only first value of any range
    stripped = stripped.split('-')[0].strip()
    try:
        age = int(stripped)
        if age<1 or age>99:
            return None
    except:
        return None
    return age



# email 7105
def clean_email(x):
    """Return a clean email address
    """
    if (len(x)>0 and x.find("@") != -1):
        em = x.strip().lower()
        em = nonWhitespace(em)
        return em
    return ''



def emailaddress_uri(email):
    c = clean_email(email)
    if len(c) > 0:
        qc = quote(c, safe='')
        return "emailaddress/" + qc
    return ''


