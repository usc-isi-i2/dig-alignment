
from datetime import datetime, date
from time import mktime, gmtime

def jp_author_uri(forename, surname):
 """Construct the URI of an author so that it will reduce correctly most of the time."""
 first_word = forename.replace('.','')
 second_word = surname.replace('.','')
 if len(second_word) < 3:
    base = second_word[0].lower() + '.' + first_word.lower()
 else:
 	base = first_word[0].lower() + '.' + second_word.lower()
 return  "author/" + asciiChars(base,'')


def jp_author_name_normalized(name):
 """Construct the author name as P. Szekely."""

 clean = name.replace('.',' ').replace(',',' ').replace(';', ' ')

 names = re.sub(r'\s+', ' ', clean.strip()).split(' ');
 last_word = names[-1]

 if len(last_word) == 1:
 	# The last word is an initial, so we accumulate all words before it that are not initials
 	# that will be our last name
 	i = 0;
 	index = -1   # index of last word that is not an initial
 	for n in names:
 		if len(n)>1:
 			index = i
 		else:
 			names[i] = n + '.'
 		i = i + 1;

 	if index == -1 or index == len(names) - 1:
 		return ' '.join(names).title();

 	last = names[index]
 	first = ' '.join(names[0:index]) + ' '.join(names[index + 1:])
 	return (first + ' ' + last).title()

 else:
 	i = 0
 	for n in names:
 		if len(n) == 1:
 			names[i] = n + '.'
 		elif i < len(names) - 1:
 			names[i] = n[0] + '.'
 		i = i + 1
 	return ' '.join(names).title();



def jp_author_name_normalized_old(name):
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
	just_name = alphaNumeric(filename[:i],'_')
	return 'article/jpl/'+just_name


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
