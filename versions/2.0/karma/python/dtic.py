from datetime import datetime, date
from time import mktime, gmtime


def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri_dtic (name):
    """ dtic lists last name, first name, middle name as author name """
    last_name = name.split()[0]
    first_name = name.split()[1]
    return  "author/" + first_name[0].lower() + '.' + last_name.lower()
