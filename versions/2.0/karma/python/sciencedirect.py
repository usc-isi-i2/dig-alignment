from datetime import datetime, date
from time import mktime, gmtime


def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    return  "author/" + first_name[0].lower() + '.' + last_name.lower()


def sd_article_uri(doi):
	"""Construct the URI for an article using the DOI"""
	return 'article/sciencedirect/'+doi
