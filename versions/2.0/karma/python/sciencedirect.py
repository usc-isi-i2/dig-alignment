from datetime import datetime, date
from time import mktime, gmtime


def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri(name):
    first_word = name.split()[0].replace('.','')
    second_word = name.split()[1].replace('.','')
    if len(second_word) < 3:
        return "author/" + second_word[0].lower() + '.' + first_word.lower()
    return  "author/" + first_word[0].lower() + '.' + second_word.lower()


def sd_article_uri(doi):
	"""Construct the URI for an article using the DOI"""
	return 'article/sciencedirect/'+doi
