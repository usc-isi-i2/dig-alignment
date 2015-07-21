from datetime import datetime, date
from time import mktime, gmtime


###Pedro: obsolete, should be removed, but not sure it is not used.
def clean_date(dateString):
    return iso8601date(dateString,"%B %Y") 

def author_uri(name):
    first_word = name.split()[0].replace('.','')
    second_word = name.split()[1].replace('.','')
    if len(second_word) < 3:
        return "author/" + second_word[0].lower() + '.' + first_word.lower()
    return  "author/" + first_word[0].lower() + '.' + second_word.lower()


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

