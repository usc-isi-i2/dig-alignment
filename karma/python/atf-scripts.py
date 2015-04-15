# Scripts for modeling ATF data.

def atf_article_uri(url, post_id):
    return get_url_hash(url)+"/"+post_id


test_date = "Wed Feb 11, 2015 10:31 am"

def atf_date_created(date):
    """Put the date in ISO format"""
    return iso8601date(date, "%a %b %d, %Y %I:%M %p")

def atf_joined_date(date):
    """Put the date in ISO format"""
    return iso8601date(date, "%a %b %d, %Y %I:%M %p")

from HTMLParser import HTMLParser

class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def handle_starttag(self, tag, attrs):
        self.fed.append(" ")
    def handle_endtag(self, tag):
        self.fed.append(" ")
    def handle_startendtag(self, tag, attrs):
        self.fed.append(" ")
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()

test_signature = "<span style=\"font-style: italic\">Precision Combat Arms<br />1710 E Trent, Unit 1<br />Spokane, WA 99202<br />509-535-0655<br />M-F 9-5</span></div>"

def signature_clean(text):
    """Strip HTML"""
    return strip_tags(text).strip()


def atf_fc_uri(article_uri):
    """URI of feature collection"""
    return article_uri+"/featurecollection"


def atf_parse_city_state(city_state):
    if "," in city_state:
        return [x.strip() for x in city_state.split(",")]
    else:
        return [city_state, ""]
