
import re
from urllib import quote


USPhonePattern = re.compile(r"^\([0-9]{3}\) [0-9]{3}\-[0-9]{4}$")
def clean_phone(x):
    """Return the phone as a 10 digit number,
     or as close to that as we can make it.
     Prefix with country code '+1' at the end.
    """
    if (len(x)>0):
        x = x.strip().lower()
        cc = ''
        if x.find("+") == 0:
            end1 = x.find(" ")
            end2 = x.find("-")
            if end1 == -1: end1 = 10000
            if end2 == -1: end2 = 10000
            if end1 != 10000 or end2 != 10000:
                end = min(end1, end2)
                cc = x[1:end]
                ph = numericOnly(x[end+1:])
            else:
                testCC = detectCountryCode(x)
                if testCC:
                    cc = testCC
                    ccLen = len(cc)
                    ph = x[ccLen+1:]
                    ph = numericOnly(ph)
                else:
                    ph = numericOnly(x)
        else:
            valid = USPhonePattern.match(x)
            if valid:
                ph = valid.group()
                cc = "1"
                ph = numericOnly(ph)
            else:
               ph = numericOnly(x)

    	# If there are 11 numbers
    	if (len(ph)==11 and ph[0]=="1"):
            ph = ph[1:]
            cc = "1"

        if len(cc) > 0:
            ph = "+" + cc + "-" + ph
    	return ph;
    return ''

def clean_phone_hack(x):
    """Return the phone as a 10 digit number,
     or as close to that as we can make it.
     Prefix with country code '+1' at the end.REMOVE THIS AFTER THE NUMBER SEMANTIC BUG IS FIXED
    """
    if (len(x)>0):
        x = x.strip().lower()
        cc = ''
        if x.find("+") == 0:
            end1 = x.find(" ")
            end2 = x.find("-")
            if end1 == -1: end1 = 10000
            if end2 == -1: end2 = 10000
            if end1 != 10000 or end2 != 10000:
                end = min(end1, end2)
                cc = x[1:end]
                ph = numericOnly(x[end+1:])
            else:
                testCC = detectCountryCode(x)
                if testCC:
                    cc = testCC
                    ccLen = len(cc)
                    ph = x[ccLen+1:]
                    ph = numericOnly(ph)
                else:
                    ph = numericOnly(x)
        else:
            valid = USPhonePattern.match(x)
            if valid:
                ph = valid.group()
                cc = "1"
                ph = numericOnly(ph)
            else:
               ph = numericOnly(x)

        # If there are 11 numbers
        if (len(ph)==11 and ph[0]=="1"):
            ph = ph[1:]
            cc = "1"

        if len(cc) > 0:
            ph = "+" + cc + ":" + ph
        return ph;
    return ''

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


