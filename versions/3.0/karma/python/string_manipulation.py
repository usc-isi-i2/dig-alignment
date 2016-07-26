__author__ = 'amandeep'

import re
import hashlib
from urlparse import urlparse, urlsplit

DOLLAR_PRICE_REGEXPS = [re.compile(r'''\$\s*(?:\d{1,3},\s?)*\d{1,3}(?:(?:\.\d+)|[KkMm])?''', re.IGNORECASE),
                        re.compile(r'''USD\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                        re.compile(r'''\d{1,7}(?:\.\d+)?\s*USD''', re.IGNORECASE)
                        ]

BITCOIN_PRICE_REGEXPS = [re.compile(r'''(?:BTC|XBT|XBC)\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                         re.compile(r'''\d{1,7}(?:\.\d+)?\s*(?:BTC|XBT|XBC)''', re.IGNORECASE)
                         ]


class SM(object):

    def __init__(self):
        self.name = "String Manipulation"

    @staticmethod
    def non_whitespace(x):
        """Return the string removing all spaces."""
        y = re.sub(r'\s+', '', x.strip())
        return y

    @staticmethod
    def non_ascii_chars(x):
        """Return a set of the non-ascii chars in x"""
        return set(re.sub('[\x00-\x7f]', '', x))

    @staticmethod
    def non_ascii_chars_as_string(x):
        """Return a string containing a comma-separated list of non-ascii chars in x"""
        y = list(SM.non_ascii_chars(x))
        y.sort()
        return ', '.join(y)

    @staticmethod
    def ascii_chars(x, replacement_string=' '):
        """Remove non-ascii chars in x replacing consecutive ones with a single space"""
        return re.sub(r'[^\x00-\x7F]+', replacement_string, x)

    @staticmethod
    def alpha_numeric(x, replacement_string=' '):
        """Replace consecutive non-alphanumeric bya replacement_string"""
        return re.sub('[^A-Za-z0-9]+', replacement_string, x)

    @staticmethod
    def numeric_only(x):
        """Remove non-numeric chars from the string x"""
        return re.sub('[^0-9]+', '', x)

    @staticmethod
    def alpha_only(x):
        """Remove non-alphabetic chars from the string x"""
        return re.sub('[^A-Za-z]+', '', x)

    @staticmethod
    def remove_alpha(x):
        """Remove alphabetic chars from the string x"""
        return re.sub('[A-Za-z]+', '', x)

    @staticmethod
    def alpha_only_preserve_space(x):
        x = re.sub('[^A-Za-z\s]+', '', x)
        y = re.sub(r'\s+', ' ', x.strip())
        return y

    @staticmethod
    def is_symbol(char1):
        if char1.isalnum():
            return False
        return True

    @staticmethod
    def fingerprint_string(x):
        """Make a fingerprint like the one google refine makes"""
        x = SM.alpha_numeric(SM.ascii_chars(x)).lower()
        y = list(set(x.split()))
        y.sort()
        return '_'.join(y)

    @staticmethod
    def md5_hash(x):
        """Return md5 hash of x"""
        return hashlib.md5(x).hexdigest()

    @staticmethod
    def sha1_hash(text):
        """return upper cased sha1 hash of the string"""
        if text:
            return hashlib.sha1(text.encode('utf-8')).hexdigest().upper()
        return ''

    @staticmethod
    def get_string(string, start, end):
        if len(string) < start:
            return ''
        if end > len(string):
            return string[start:]
        return string[start:end+1]

    @staticmethod
    def clean_age(x, lower_bound=18, upper_bound=60):
        """Return the clean age"""
        stripped = x.strip().lower()
        """take only first value of any range"""
        stripped = stripped.split('-')[0].strip()
        try:
            age = int(stripped)
            if age <= lower_bound or age >= upper_bound:
                return None
        except:
            return None
        return age

    @staticmethod
    def clean_email(x):
        """Return a clean email address"""
        if len(x) > 0 and x.find("@") != -1:
            em = x.strip().lower()
            em = SM.non_whitespace(em)
            return em
        return ''

    @staticmethod
    def convert_to_float_string(number):
        """return the number as a float string, eg: scientific notation numbers"""
        try:
            return '{0:.15f}'.format(float(number))
        except:
            return ''

    @staticmethod
    def to_title_case_if_upper(x):
        """Return the string in title case if it is all upper, otherwise leave capitalization alone."""
        x = x.strip()
        if x.isupper():
            return x.title()
        else:
            return x

    @staticmethod
    def to_title_case_cleaned(x):
        """Return the string in title case cleaning spaces."""
        y = re.sub(r'\s+', ' ', x.strip())
        return y.title()

    @staticmethod
    def get_website_domain(url):
        """input www.google.com, output google.com"""
        parsed_uri = urlsplit(url)
        # parsed_uri = urlparse(url)
        if parsed_uri:
            domain = parsed_uri.netloc
            if domain:
                if domain.startswith("www."):
                    domain = domain[4:]
                return domain
        return ''

    @staticmethod
    def get_website_domain_only(url):
        """input www.google.com, output google"""
        netloc = SM.get_website_domain(url)
        pieces = netloc.split('.')
        if len(pieces) > 0:
            if len(pieces) == 2:
                return netloc
            if len(pieces) == 3 and len(pieces[2]) == 2:
                if len(pieces[1]) <= 3:
                    return netloc
                else:
                    return '.'.join(pieces[1:])
            else:
                return '.'.join(pieces[1:])

        return netloc


    @staticmethod
    def get_dollar_prices(*texts):
        matches = []
        for t in texts:
            for r in DOLLAR_PRICE_REGEXPS:
                for m in r.findall(t):
                    matches.append(m.replace('$ ', '$').replace(',', '').replace('$', '').replace('K', "000")
                                   .replace('k', "000").replace("M", "000").replace('m', "000"))
        return "|".join(matches)

    @staticmethod
    def get_bitcoin_prices(*texts):
        matches = []
        for t in texts:
            for r in BITCOIN_PRICE_REGEXPS:
                for m in r.findall(t):
                    matches.append(m.replace('BTC', '').replace('XBT', '').replace('XBC', '').replace(' ', ''))
        return "|".join(matches)

    @staticmethod
    def clean_name(x):
        x = SM.toTitleCaseCleaned(x)
        if SM.isSymbol(x[0:1]):
            return ''
        return x

    @staticmethod
    def toTitleCaseCleaned(x):
        """Return the string in title case cleaning spaces."""
    
        y = re.sub(r'\s+', ' ', x.strip())
        return y.title()

    @staticmethod
    def isSymbol(char1):
        if char1.isalnum():
            return False
        return True

    @staticmethod
    def clean_ethnicity(x):
        stripped = x.strip().lower().replace(" ","")
        return stripped

    @staticmethod
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
                # return nearest5(int(2.54 * (12 * feet) + inches))
                # no binning
                return int(2.54 * (12 * feet) + inches)
            else:
                # no inches, so try centimeters
                # Second, 137
                # return nearest5(int(stripped))
                # no binning
                return int(stripped)
        except:
            return None
        return None


    @staticmethod
    def clean_price_name(x):
        try:
            minutes = str(SM.calculate_minutes(x))
            return SM.get_price(x) + '-per-' + minutes + 'min'
        except:
            return x


    @staticmethod
    def get_price(x):
        try:
            v = x.split('-')
            return v[0]
        except:
            return x


    @staticmethod
    def calculate_minutes(x):
        try:
            v = x.split('-')
            time = v[1]
            if ":" in time:
                v = time.split(':')
                hour = v[0]
                minute = v[1]
                return int(hour)*60 + int(minute)
            else:
                return x
        except:
            return x


    @staticmethod
    def base_clean_rate(x):
        clean = x.strip().lower()
        if clean[0] == "0":
            return None

        rate = int(float(clean))
        if rate < 20 or rate > 1000:
            return None
        return rate

    @staticmethod
    def clean_rate60(x):
        rate = SM.base_clean_rate(x)
        if rate != None:
            return "%s-per-60min" % rate
        return ''

    @staticmethod
    def clean_rate15(x):
        rate = SM.base_clean_rate(x)
        if rate != None:
            return "%s-per-15min" % rate
        return ''

    @staticmethod
    def clean_rate30(x):
        rate = SM.base_clean_rate(x)
        if rate != None:
            return "%s-per-30min" % rate
        return ''

    @staticmethod
    def rate_price(cleaned):
        if cleaned:
            idx = cleaned.find("-")
            if idx != -1:
                return int(cleaned[0:idx])
        return ''

    @staticmethod
    def rate_duration(cleaned):
        if cleaned:
            idx = cleaned.find("per-")
            if idx != -1:
                str = cleaned[idx+4:]
                dur = str[0: len(str)-3]
                return dur
        return ''

    @staticmethod
    def rate_unit(cleaned):
        if cleaned:
            idx = cleaned.find("min")
            if idx != -1:
                return "MIN"
            idx = cleaned.find("sec")
            if idx != -1:
                return "SEC"
            idx = cleaned.find("hr")
            if idx != -1:
                return "HUR"
        return ''

    @staticmethod
    def clean_weight(x):
        """In kg.unmarked weight < 90 is interpreted as kg, >=90 as lb"""
        x = str(x).strip().lower()

        def lb_to_kg(lb):
            return int(float(lb)/2.2)
        def sanityCheck(kg):
            if kg >= 40 and kg <= 200:
                return kg
            else:
                return None

        try:
            cleaned = x

            # # first try for st/stone
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
                # return sanityCheck(nearest2(lb_to_kg(int(stone*14+lb))))
                # no binning
                return sanityCheck(lb_to_kg(int(stone*14+lb)))
            lb = cleaned.strip('s')
            # now try for just pounds
            if lb.endswith("lb"):
                # return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('lb'))))))
                # no binning
                return sanityCheck(lb_to_kg(int(float(lb.strip('lb')))))
            if lb.endswith('pound'):
                # return sanityCheck(nearest2(lb_to_kg(int(float(lb.strip('pound'))))))
                # no binning
                return sanityCheck(lb_to_kg(int(float(lb.strip('pound')))))
            # now kg
            kg = cleaned.strip('s')
            if kg.endswith("kg"):
                # return sanityCheck(nearest2(int(float(kg.strip('kg')))))
                # no binning
                return sanityCheck(int(float(kg.strip('kg'))))
            if kg.endswith("kilo"):
                # return sanityCheck(nearest2(int(float(kg.strip('kilo')))))
                # no binning
                return sanityCheck(int(float(kg.strip('kilo'))))
            if kg.endswith('kilogram'):
                # return sanityCheck(nearest2(int(float(kg.strip('kilogram')))))
                # no binning
                return sanityCheck(int(float(kg.strip('kilogram'))))
            # now assume number sans unit
            num = int(float(cleaned))
            if num < 90:
                # assume kg
                # return sanityCheck(nearest2(num))
                # no binning
                return sanityCheck(num)
            else:
                # assume lb
                # return sanityCheck(nearest2(lb_to_kg(num)))
                # no binning
                return sanityCheck(lb_to_kg(num))

        except Exception, e:
            return None

# if __name__ == "__main__":
#     import codecs
#     lines = codecs.open('urls', 'r', 'utf-8').readlines()
#     unique_publishers = set()
#     for line in lines:
#         # print line
#         idx = line.rfind(':')
#         line = line[:idx]
#         p = SM.get_website_domain_only(line).replace('\n', '')
#         if not p or p == '':
#             print line
#         unique_publishers.add(p)
#
#     print unique_publishers

