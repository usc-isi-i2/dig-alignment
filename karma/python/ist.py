from collections import defaultdict
import re
from util import numericOnly, alphaOnly

def nearest5(x):
	return 5*(int(2.5 + x)/5)

def nearest2(x):
	return 2*(int(1 + x)/2)

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
	r = x.strip().lower()
	if r[0] == "0":
		return None
	rate = int(float(r))
	if rate < 20 or rate > 1000:
		return None
	return nearest5(rate)

def feature_rate(x):
	cleaned = clean_rate(x)
	if cleaned:
		return "feature/rate/%s" % cleaned
def test_ethnicity():
	for b in ethnicity_samples:
		f = feature_ethnicity(b)
		print "%r => %r" % (b, f)

# ethnicity	38587
def clean_ethnicity(x):
	stripped = x.strip().lower().replace(" ","")
	return stripped

def feature_ethnicity(x):
	cleaned = clean_ethnicity(x)
	if cleaned:
		return "feature/ethnicity/%s" % cleaned

# height	29135

height_samples = ["168", "5'6\"", "6'", "5'7\" - 5'9\""]
def test_height():
	for b in height_samples:
		f = feature_height(b)
		print "%r => %r" % (b, f)


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
	return alphaOnly(stripped)

def feature_hair(x):
	cleaned = clean_hair(x)
	if cleaned:
		return "feature/hair/%s" % cleaned

# build	21842
def clean_build(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_build(x):
	cleaned = clean_build(x)
	if cleaned:
		return "feature/build/%s" % cleaned

# cup	19179
def clean_cup(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_cup(x):
	cleaned = clean_cup(x)
	if cleaned:
		return "feature/cup/%s" % cleaned

# bust	18394
# bust  34-35
# bust  D
# bust  34&quot;
# bust  over
# bust  Perrrfct

bust_samples = ["34-35", "D", "34&quot;", '34"', "over", "Perrrfct", "34.5"]
def test_bust():
	for b in bust_samples:
		f = feature_bust(b)
		print "%r => %r" % (b, f)

def clean_bust(x):
	stripped = x.strip().lower()
	stripped = stripped.replace(" ","")
	first = re.split("-", stripped)[0]
	try:
		return int(float(first))
	except:
		pass
	try:
		return int(numericOnly(first))
	except:
		pass
	return None

def feature_bust(x):
	"this one is in inches"
	def sanityCheck(bust):
		if bust >= 20 and bust <= 50:
			return bust
		else:
			return None

	cleaned = clean_bust(x)
	if cleaned:
		return "feature/bust/%s" % cleaned

# piercings	18294 
# None Belly Button Face
# xxxxx Other (where xxxx is a legal value)
# Tongue Breasts Belly Button Other
#
# Maybe use "belly button" "bellow the belt" as tokens, and then
# we should generate a comma-separated list of values and then
# use split values to generate a multi-valued cell so that we
# can generate multiple features per attribute.
def clean_piercings(x):
	stripped = x.strip().lower()
	stripped = re.sub("belly button", "bellybutton", stripped)
	stripped = re.sub("below the belt", "belowthebelt", stripped)
	return stripped.split(' ')

def feature_piercings(x):
	cleaned = clean_piercings(x)
	if cleaned:
		return ",".join(["feature/piercings/%s" % c for c in cleaned])

# creditcards	18272
def clean_creditcards(x):
	stripped = x.strip().lower()
	return stripped

def feature_creditcards(x):
	cleaned = clean_creditcards(x)
	if cleaned:
		return "feature/creditcards/%s" % cleaned

# hairlength	18030
def clean_hairlength(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_hairlength(x):
	cleaned = clean_hairlength(x)
	if cleaned:
		return "feature/hairlength/%s" % cleaned

# hairtype	17945
def clean_hairtype(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_hairtype(x):
	cleaned = clean_hairtype(x)
	if cleaned:
		return "feature/hairtype/%s" % cleaned

# eyes	16723
def clean_eyes(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_eyes(x):
	cleaned = clean_eyes(x)
	if cleaned:
		return "feature/eyes/%s" % cleaned

# weight	13316
def clean_weight(x):
	stripped = x.strip().lower()
	return stripped

def feature_weight(x):
	"unmarked weight < 90 is interpreted as kg, >=90 as lb"
	def lb_to_kg(lb):
		return int(float(lb)/2.2)
	def sanityCheck(kg):
		if kg >= 40 and kg <= 200:
			return "feature/weight/" + str(kg)
		else:
			return None

	try:
		cleaned = clean_weight(x)
		# first try for st/stone
		l = re.split("stone", cleaned)
		if len(l) == 1:
			l = re.split("st", cleaned)
		if len(l) > 1:
			stone = float(l[0])
			lb = l[1]
			lb = lb.strip('s')
			lb = lb.strip('lb')
			lb = lb.strip('pound')
			try:
				lb = float(lb)
			except ValueError, e:
				lb = 0
			return sanityCheck(nearest2(lb_to_kg(int(stone*14+lb))))
		lb = cleaned.strip('s')
		# now try for just pounds
		if lb.endswith("lb"):
			return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('lb'))))))
		if lb.endswith('pound'):
			return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('pound'))))))
		# now kg
		kg = cleaned.strip('s')
		if kg.endswith("kg"):
			return sanityCheck(nearest2(int(float(kg.strip('kg')))))
		if kg.endswith('kilo'):
			return sanityCheck(nearest2(int(float(kg.strip('kilo')))))
		if kg.endswith('kilogram'):
			return sanityCheck(nearest2(int(float(kg.strip('kilogram')))))
		# now assume number sans unit
		num = int(float(cleaned))
		if num < 90:
			# assume kg
			return sanityCheck(nearest2(num))
		else:
			# assume lb
			return sanityCheck(nearest2(lb_to_kg(num)))
	
	except Exception, e:
		return None


# name	10042
def clean_name(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_name(x):
	cleaned = clean_name(x)
	if cleaned:
		return "feature/name/%s" % cleaned

# tattoos	8614
def clean_tattoos(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_tattoos(x):
	cleaned = clean_tattoos(x)
	if cleaned:
		return "feature/tattoos/%s" % cleaned

# grooming	5709
def clean_grooming(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_grooming(x):
	cleaned = clean_grooming(x)
	if cleaned:
		return "feature/grooming/%s" % cleaned

# implants	5469
def clean_implants(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_implants(x):
	cleaned = clean_implants(x)
	if cleaned:
		return "feature/implants/%s" % cleaned

# username	5209
def clean_username(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_username(x):
	cleaned = clean_username(x)
	if cleaned:
		return "feature/username/%s" % cleaned

# travel	4727
def clean_travel(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_travel(x):
	cleaned = clean_travel(x)
	if cleaned:
		return "feature/travel/%s" % cleaned

# zip	2734
def clean_zip(x):
	stripped = x.strip().lower()
	return numericOnly(stripped)

def feature_zip(x):
	cleaned = clean_zip(x)
	if cleaned:
		return "feature/zip/%s" % cleaned

# waist	2468
waist_samples = ["24 inches", "28\"", "70cm", "70 cm", "26.5", "svelte", "24-25"]
def test_waist():
	for b in waist_samples:
		f = feature_waist(b)
		print "%r => %r" % (b, f)


def clean_waist(x):
	"copied from bust"
	try:
		stripped = x.strip().lower()
		stripped = stripped.replace(" ","")
		first = re.split("-", stripped)[0]
		first = first.strip()
		return first 
	except:
		pass
	return None

def feature_waist(x):
	"unmarked waist < 60 is interpreted as in, >=60 as cm"
	def inch_to_cm(inch):
		return int(inch*2.54)
	def sanityCheck(cm):
		if cm >= 40 and cm <= 200:
			return "feature/waist/" + str(cm)
		else:
			return None

	try:
		cleaned = clean_waist(x)
		inch = cleaned.strip('es')
		inch = inch.strip('s')
		# now try for just inches
		if inch.endswith("inch"):
			return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('inch'))))))
		if inch.endswith('in'):
			return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('in'))))))
		if inch.endswith('"'):
			return sanityCheck(nearest2(inch_to_cm(int(float(inch.strip('"'))))))
		# now cm
		cm = cleaned.strip('s')
		if cm.endswith("cm"):
			return sanityCheck(nearest2(int(float(cm.strip('cm')))))
		if cm.endswith('centimeter'):
			return sanityCheck(nearest2(int(float(cm.strip('centimeter')))))
		# now assume number sans unit
		num = int(float(cleaned))
		if num >= 60:
			# assume cm
			return sanityCheck(nearest2(num))
		else:
			# assume inch
			return sanityCheck(nearest2(inch_to_cm(num)))
	
	except Exception, e:
		return None

# hips	2400
def clean_hips(x):
	stripped = x.strip().lower()
	return numericOnly(stripped)

def feature_hips(x):
	cleaned = clean_hips(x)
	if cleaned:
		return "feature/hips/%s" % cleaned

# alias	2049
def clean_alias(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_alias(x):
	cleaned = clean_alias(x)
	if cleaned:
		return "feature/alias/%s" % cleaned

# availability	2049
availability_samples = ["Incall", "Outcall", "Incall Outcall"] 
def test_availability():
	for b in availability_samples:
		f = feature_availability(b)
		print "%r => %r" % (b, f)
def clean_availability(x):
	stripped = x.strip().lower()
	return alphaOnly(stripped)

def feature_availability(x):
	cleaned = clean_availability(x)
	if cleaned:
		return "feature/availability/%s" % cleaned

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
mapFunctions['availability'] = feature_availability

def feature_value(attributeName, value):
	return mapFunctions[attributeName](value)
