
from datetime import datetime, date
from time import mktime, gmtime


def jp_author_uri(forename, surname):
	"""Construct the URI of an author so that it will reduce correctly most of the time."""
	return 'person/'+forename[0].lower()+"_"+surname.lower()


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

