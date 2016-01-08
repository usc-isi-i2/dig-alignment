__author__ = 'amandeep'

import re
import hashlib


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
