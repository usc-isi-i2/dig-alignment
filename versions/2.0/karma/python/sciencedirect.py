from datetime import datetime, date
from time import mktime, gmtime


def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    return  "author/" + first_name[0] + '.' + last_name
    