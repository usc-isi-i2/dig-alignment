
from datetime import datetime, date
from time import mktime, gmtime

def jp_author_uri(forename, surname):
 """Construct the URI of an author so that it will reduce correctly most of the time."""
 first_word = forename.replace('.','')
 second_word = surname.replace('.','')
 if len(second_word) < 3:
    return "author/" + second_word[0].lower() + '.' + first_word.lower()
 return  "author/" + first_word[0].lower() + '.' + second_word.lower()


def jp_author_name_normalized(name):
 """Construct the author name as P. Szekely."""
 names = name.replace('.','').split(' ');
 first_word = names[0];
 last_word = names[-1]
 if len(last_word) == 1:
 	first = last_word;
 	last = first_word;
 else:
 	first = first_word;
 	last = last_word;
 # make the first name be the initial only.
 if len(first) > 1:
 	first = first[0];
 if len(first) == 1:
 	first = first + '.';
 names[0] = first;
 names[-1] = last;
 return ' '.join(names).title();


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
	return getYearFromISODate(iso8601date(dateString,"%B %Y"))


def jp_clean_year(string, format):
	"""Parse the date and return the year."""
	return getYearFromISODate(iso8601date(string,format))


def jp_clean_year_best_effort(string):
	"""Try to parse the string as a date and return the year"""
	d = jp_clean_year(string, "%Y")
	if d:
		return d;

	d = jp_clean_year(string, "%Y-%m")
	if d:
		return d;
	
	return ''
