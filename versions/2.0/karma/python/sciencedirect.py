from datetime import datetime, date
from time import mktime, gmtime



def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri(name):
    first_name = name.split()[0]
    last_name = name.split()[1]
    return  "author/" + first_name[0].lower() + '.' + last_name.lower()


def sd_article_uri(abstract, title, doi):
	"""Construct the URI for an article using the Abstract, Title, DOI"""
	#return 'article/sciencedirect/'+doi

	text = ''
	if abstract and abstract != '':
		text = text + abstract

	if title and title != '':
		text = text + title

	if doi and doi != '':
		text = text + doi

	return 'article/sciencedirect/'+ getTextHash(text)

def getTextHash(text):
    if text:
        return hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
    return ''
