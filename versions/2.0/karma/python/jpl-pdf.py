
from datetime import datetime, date
from time import mktime, gmtime

def jp_author_uri(forename, surname):
 """Construct the URI of an author so that it will reduce correctly most of the time."""
 first_word = forename.replace('.','')
 second_word = surname.replace('.','')
 if len(second_word) < 3:
    return "author/" + second_word[0].lower() + '.' + first_word.lower()
 return  "author/" + first_word[0].lower() + '.' + second_word.lower()


def jp_author_name(forename, surname):
	"""Construct the name of a person as a single string."""
	if len(forename) == 1:
		forename = forename+'.'	
	return forename+" "+surname


def jp_article_uri(filename):
	"""Construct the URI for an article using the file name"""
	i = filename.rfind('.') 
	return 'article/jpl/'+filename[:i]


def jp_clean_date(dateString):
	return iso8601date(dateString,"%B %Y") 

