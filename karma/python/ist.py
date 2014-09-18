from collections import defaultdict
import re

# phone
# phone2	810

def clean_phone(x):
	"""Return the phone as a 10 digit number,
	 or as close to that as we can make it
	"""
	ph = numericOnly(x.strip().lower())
	# If there are 11 numbers 
	if (len(ph)==11 and ph[0]=="1"):
		ph = ph[1:]
	return ph;

def feature_phone(x):
	cleaned = clean_phone(x)
	if cleaned:
		return "feature/phonenumber/%s" % cleaned

# age	15647
def clean_age(x):
	"""Return the a clean age
	"""
	return x.strip().lower();

def feature_age(x):
	cleaned = clean_age(x)
	if cleaned:
		return "feature/age/%s" % cleaned

# email	7105
def clean_email(x):
	"""Return a clean email address
	"""
	if (x.find("@") != -1):
		em = x.strip().lower().lower();
		return em;

def feature_email(x):
	cleaned = clean_email(x)
	if cleaned:
		return "feature/email/%s" % cleaned

# gender
def clean_gender(x):
	g = x.strip().lower().lower();
	if g in ["female", "f"]:
		return "f"
	elif g in ["male", "m"]:
		return "m"
	else:
		return None

def feature_gender(x):
	cleaned = clean_gender(x)
	if cleaned:
		return "feature/gender/%s" % cleaned

# rate
# rate60	12706
# rate30	10640
# rate15	1215
def clean_rate(x):
	r = strip();
	return int(x)

def feature_rate(x):
	cleaned = clean_rate(x)
	if cleaned:
		return "feature/rate/%s" % cleaned


# ethnicity	38587
def clean_ethnicity(x):
	stripped = x.strip().lower()
	return x

def feature_ethnicity(x):
	cleaned = clean_ethnicity(x)
	if cleaned:
		return "feature/ethnicity/%s" % cleaned

# height	29135
# 168
# 5'6"
# 6'
# 5'7" - 5'9"
# test=["168", "5'6\"", "6'", "5'7\" - 5'9\""]

def nearest5(x):
	return 5*(int(2.5 + x)/5)

def clean_height(x):
	stripped = x.strip().lower()
	# take only first measurement of any range
	stripped = stripped.split('-')[0].strip()
	try:
		# First, 5'6" or 6' or 6'7
		dimensions = stripped.split("'")
		if len(dimensions) >= 2:
			feet = int(dimensions[0])
			try:
				inches = int(dimensions[1].strip('"'))
			except:
				# empty inches
				inches = 0
			return nearest5(int(2.54 * (12 * feet) + inches))
		else:
			# no inches, so try centimeters
			# Second, 137
			return nearest5(int(stripped))
	except:
		return None
	return None

def feature_height(x):
	cleaned = clean_height(x)
	if cleaned:
		return "feature/height/%s" % cleaned

# hair	22078
def clean_hair(x):
	stripped = x.strip().lower()
	return x

def feature_hair(x):
	cleaned = clean_hair(x)
	if cleaned:
		return "feature/hair/%s" % cleaned

# build	21842
def clean_build(x):
	stripped = x.strip().lower()
	return x

def feature_build(x):
	cleaned = clean_build(x)
	if cleaned:
		return "feature/build/%s" % cleaned

# cup	19179
def clean_cup(x):
	stripped = x.strip().lower().lower()
	return x

def feature_cup(x):
	cleaned = clean_cup(x)
	if cleaned:
		return "feature/cup/%s" % cleaned

# bust	18394
def clean_bust(x):
	stripped = x.strip().lower()
	return x

def feature_bust(x):
	cleaned = clean_bust(x)
	if cleaned:
		return "feature/bust/%s" % cleaned

# piercings	18294
def clean_piercings(x):
	stripped = x.strip().lower()
	return x

def feature_piercings(x):
	cleaned = clean_piercings(x)
	if cleaned:
		return "feature/piercings/%s" % cleaned

# creditcards	18272
def clean_creditcards(x):
	stripped = x.strip().lower()
	return x

def feature_creditcards(x):
	cleaned = clean_creditcards(x)
	if cleaned:
		return "feature/creditcards/%s" % cleaned

# hairlength	18030
def clean_hairlength(x):
	stripped = x.strip().lower()
	return x

def feature_hairlength(x):
	cleaned = clean_hairlength(x)
	if cleaned:
		return "feature/hairlength/%s" % cleaned

# hairtype	17945
def clean_hairtype(x):
	stripped = x.strip().lower()
	return x

def feature_hairtype(x):
	cleaned = clean_hairtype(x)
	if cleaned:
		return "feature/hairtype/%s" % cleaned

# eyes	16723
def clean_eyes(x):
	stripped = x.strip().lower()
	return x

def feature_eyes(x):
	cleaned = clean_eyes(x)
	if cleaned:
		return "feature/eyes/%s" % cleaned

# weight	13316
def clean_weight(x):
	stripped = x.strip().lower()
	return x

def feature_weight(x):
	cleaned = clean_weight(x)
	if cleaned:
		return "feature/weight/%s" % cleaned

# name	10042
def clean_name(x):
	stripped = x.strip().lower()
	return x

def feature_name(x):
	cleaned = clean_name(x)
	if cleaned:
		return "feature/name/%s" % cleaned

# tattoos	8614
def clean_tattoos(x):
	stripped = x.strip().lower()
	return x

def feature_tattoos(x):
	cleaned = clean_tattoos(x)
	if cleaned:
		return "feature/tattoos/%s" % cleaned

# grooming	5709
def clean_grooming(x):
	stripped = x.strip().lower()
	return x

def feature_grooming(x):
	cleaned = clean_grooming(x)
	if cleaned:
		return "feature/grooming/%s" % cleaned

# implants	5469
def clean_implants(x):
	stripped = x.strip().lower()
	return x

def feature_implants(x):
	cleaned = clean_implants(x)
	if cleaned:
		return "feature/implants/%s" % cleaned

# username	5209
def clean_username(x):
	stripped = x.strip().lower()
	return x

def feature_username(x):
	cleaned = clean_username(x)
	if cleaned:
		return "feature/username/%s" % cleaned

# travel	4727
def clean_travel(x):
	stripped = x.strip().lower()
	return x

def feature_travel(x):
	cleaned = clean_travel(x)
	if cleaned:
		return "feature/travel/%s" % cleaned

# zip	2734
def clean_zip(x):
	stripped = x.strip().lower()
	return x

def feature_zip(x):
	cleaned = clean_zip(x)
	if cleaned:
		return "feature/zip/%s" % cleaned

# waist	2468
def clean_waist(x):
	stripped = x.strip().lower()
	return x

def feature_waist(x):
	cleaned = clean_waist(x)
	if cleaned:
		return "feature/waist/%s" % cleaned

# hips	2400
def clean_hips(x):
	stripped = x.strip().lower()
	return x

def feature_hips(x):
	cleaned = clean_hips(x)
	if cleaned:
		return "feature/hips/%s" % cleaned

# alias	2049
def clean_alias(x):
	stripped = x.strip().lower()
	return x

def feature_alias(x):
	cleaned = clean_alias(x)
	if cleaned:
		return "feature/alias/%s" % cleaned




mapFunctions = defaultdict(lambda x: None)

mapFunctions['phone'] = feature_phone
mapFunctions['age'] = feature_age
mapFunctions['email'] = feature_email
mapFunctions['gender'] = feature_gender
mapFunctions['rate'] = feature_rate
mapFunctions['ethnicity'] = feature_ethnicity
mapFunctions['height'] = feature_height
mapFunctions['hair'] = feature_hair
mapFunctions['build'] = feature_build
mapFunctions['cup'] = feature_cup
mapFunctions['bust'] = feature_bust
mapFunctions['piercings'] = feature_piercings
mapFunctions['creditcards'] = feature_creditcards
mapFunctions['hairlength'] = feature_hairlength
mapFunctions['hairtype'] = feature_hairtype
mapFunctions['eyes'] = feature_eyes
mapFunctions['weight'] = feature_weight
mapFunctions['name'] = feature_name
mapFunctions['tattoos'] = feature_tattoos
mapFunctions['grooming'] = feature_grooming
mapFunctions['implants'] = feature_implants
mapFunctions['username'] = feature_username
mapFunctions['travel'] = feature_travel
mapFunctions['zip'] = feature_zip
mapFunctions['waist'] = feature_waist
mapFunctions['hips'] = feature_hips
mapFunctions['alias'] = feature_alias

def feature_value(attributeName, value):
	return mapFunctions[attributeName](value)
