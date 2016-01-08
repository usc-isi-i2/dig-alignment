from urllib import quote
from string_manipulation import SM
from phone_manipulation import PM
import re


class UM(object):

    def __init__(self):
        self.name = "Uri Manipulation"

    @staticmethod
    def phone_uri(x):
        """Return the uri for a phone
        as countrycode-phone
        Use 'x-' as country code if not present in the number
        """
        x = PM.clean_phone(x)
        if len(x) > 0:
            dash_idx = x.find('-')
            if dash_idx != -1:
                return "phonenumber/" + x[1:]
            return "phonenumber/x-" + x
        return ''

    @staticmethod
    def email_uri(email):
        c = SM.clean_email(email)
        if len(c) > 0:
            qc = quote(c, safe='')
            return "email/" + qc
        return ''

    @staticmethod
    def uri_from_fields(prefix, *fields):
        """Construct a URI out of the fields, concatenating them after removing offensive characters.
        When all the fields are empty, return empty"""
        string = '_'.join(SM.alpha_numeric(f.strip().lower(), '') for f in fields)

        if len(string) == len(fields)-1:
            return ''

        return prefix + string

    @staticmethod
    def country_uri(x):
        """Return a URI for a country given its name."""
        x = re.sub('[^A-Za-z0-9]+', '', x)
        return x.lower()


    @staticmethod
    def person_name_uri(x):
        """Return a URI for a person name."""
        x = re.sub('[^A-Za-z0-9]+', '', x.strip())
        return x.lower()
