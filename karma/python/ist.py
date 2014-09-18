

def clean_phone(x):
	"""Return the phone as a 10 digit number,
	 or as close to that as we can make it
	"""
	ph = numericOnly(x.strip())
	# If there are 11 numbers 
	if (len(ph)==11 and ph[0]=="1"):
		ph = ph[1:]
	return ph;


def clean_age(x):
	"""Return the a clean age
	"""
	return x.strip();


def clean_email(x):
	"""Return a clean email address
	"""
	if (x.find("@") != -1):
		em = x.strip().lower();
		return em;


def clean_gender(x):
	g = x.strip().lower();
	if g in ["female", "f"]:
		return "f"
	elif g in ["male", "m"]:
		return "m";

def clean_rate(x):
	r = strip();
	return int(x)