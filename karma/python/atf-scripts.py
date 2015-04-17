# Scripts for modeling ATF data.

def atf_article_uri(url, post_id):
    return get_url_hash(url)+"/"+post_id


test_date = "Wed Feb 11, 2015 10:31 am"

def atf_date_created(date, format="%a %b %d, %Y %I:%M %p"):
    """Put the date in ISO format"""
    return iso8601date(date, format)

def atf_joined_date(date, format="%a %b %d, %Y %I:%M %p"):
    """Put the date in ISO format"""
    return iso8601date(date, format)

test_date2 = "Wednesday, March 18, 2015 10:33 AM"
test_format2 = "%A, %B %d, %Y %I:%M %p"

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

def atf_get_city(city_state):
    if "," in city_state:
        return city_state.split(",")[0]
    else:
        return city_state

def atf_get_state(city_state):
    if "," in city_state:
        return city_state.split(",")[1]
    else:
        return ""

def atf_address_uri(city, state, country):
    return address_uri(city, state, country)

def atf_clean_post_count(post_count):
    return numericOnly(post_count)

import re

WEAPONS_PHRASES = ['gun',
                   'rifle',
                   'missile',
                   'mark',
                   'tank',
                   'mk',
                   'torpedo',
                   'naval',
                   'vehicle',
                   'remington',
                   'smith',
                   'pistol',
                   'wesson',
                   'grenade',
                   'howitzer',
                   'mine',
                   'mortar',
                   'colt',
                   'submachine',
                   'canon',
                   'cannon',
                   'mod\xe8le',
                   'ruger',
                   'koch',
                   'heckler',
                   'weapon',
                   'bomb',
                   'armoured',
                   'carbine',
                   'beretta',
                   'missile',
                   'armored',
                   'winchester',
                   'springfield',
                   'revolver',
                   'launcher',
                   'caliber',
                   'assault',
                   'sig',
                   '45',
                   'ordnance',
                   'zastava',
                   'rocket',
                   'anti-tank',
                   'walther',
                   'combat',
                   'benelli',
                   'sniper',
                   'series',
                   'mle',
                   'browning',
                   'schneider',
                   'm1',
                   'carrier',
                   'kanone',
                   'defense',
                   'artillery',
                   'tank',
                   'steyr',
                   'rml',
                   'mowag',
                   'wz.',
                   'mauser',
                   'm3',
                   'vehicle',
                   'vickers',
                   'taurus',
                   'tactical',
                   'sword',
                   'infantry',
                   'panzer',
                   'marlin',
                   'hotchkiss',
                   'fk',
                   'barrett',
                   'weapon',
                   'sauer',
                   'modello',
                   'explosive',
                   'aircraft',
                   'tractor',
                   'skoda',
                   'self-propelled',
                   'rheinmetall',
                   'reconnaissance',
                   'minenwerfer',
                   'm4',
                   'kel-tec',
                   'fighting',
                   'daewoo',
                   'bofors',
                   'rocket',
                   'sd.kfz.',
                   'scout',
                   'pindad',
                   'knife',
                   'carriage',
                   'bliss-leavitt',
                   'arms',
                   'advanced',
                   'storm',
                   'sdkfz',
                   'savage',
                   'saurer',
                   'renault',
                   'nuclear',
                   'missile',
                   'bayonet',
                   'arsenal',
                   'sword',
                   'armoured',
                   'weapons',
                   'weapon-stub',
                   'war',
                   'strike',
                   'spartan',
                   'oerlikon',
                   'obusier',
                   'nebelwerfer',
                   'm\xF6rser',
                   'munition',
                   'military',
                   'marksman',
                   'krupp',
                   'flamethrower',
                   'feldhaubitze',
                   'eagle',
                   'crosman',
                   'cobra',
                   'carrier',
                   'bushmaster',
                   'breda',
                   'army',
                   'amphibious',
                   'afv',
                   'wolf',
                   'vektor',
                   'vehicle',
                   'turret',
                   'tanks',
                   'stridsvagn',
                   'soltam',
                   'siege',
                   'shotgun',
                   'sg',
                   'schwerer',
                   'schwere',
                   'pdw',
                   'panhard',
                   'nambu',
                   'mortier',
                   'magnum',
                   'm8',
                   'm60',
                   'm1918',
                   'm1895',
                   'luftminenwerfer',
                   'leopard',
                   'kbk',
                   'kanon',
                   'imbel',
                   'humber',
                   'hi-point',
                   'guns',
                   'gryazev-shipunov',
                   'explosives',
                   'denel',
                   'battle',
                   'axe',
                   'automag',
                   'attack',
                   'armory',
                   'armalite',
                   'alfa',
                   'pistol',
                   'bomb',
                   'artillery']

def isInt(s):
    try:
        int(s)
        return True
    except:
        pass
    return False

WEAPONS_PHRASES = [w for w in WEAPONS_PHRASES if not isInt(w)]
# restore a few numbers
WEAPONS_PHRASES = WEAPONS_PHRASES + ["45", ".45", "38", "50", "3006", ".22", "22", "357"]
# add a few missing popular items
WEAPONS_PHRASES = WEAPONS_PHRASES + ['uzi', 'ammo', 'ammunition', 'stoner', 'scar17', 'taser', 'tazer', 
                                     'Tokarev', 'glock', 'AK-47', 'AK 47', 'luger', 'P38', 'spdmstr', 
                                     'AR15', 'AR-15', 'AMT', 'Trejo', 'Armatix', 'Astra', 'Bechowiec',
                                     'Bauer', 'Benelli', 'Versa', 'Browning', 'BUL', 'Caracal', 'Zamorana',
                                     'Wesson', 'Danuvia', 'Musgrave', 'Vektor', 'Enfield',
                                     'FEG', 'FN', 'Herstal', 'Gabilondo', 'Urresti', 'Makarov', 'Izhevsk',
                                     'Sauer', 'KBP', 'Kimber', 'MAB', 'Mauser', 'MAC-10', 'MAC-11',
                                     'MAC10', 'MAC11', 'Pindad',
                                     'RPC', 'Bonifacio', 'Steyr',
                                     'Tanfoglio', 'Tula', "CZ",
                                     "\x010CZ", 'RSAF', 'Webley',
                                     'Norinco', 'Akdal', 'Famars',
                                     'Marlin']

WEAPONS_PATTERNS = [re.compile(r"""\b%s\b""" % ph, re.IGNORECASE) for ph in WEAPONS_PHRASES]

test_text = """New In Box Walther UZI .22LR RIFLE 20+1 $349.99"""

def weapons_words(text, patterns=WEAPONS_PATTERNS, phrases=WEAPONS_PHRASES):
    matches = set()
    for (pattern, phrase) in zip(patterns, phrases):
        for match in re.finditer(pattern, text):
            matches.add(phrase)
    matches = list(matches)
    matches.sort()
    return matches

# print weapons_words(test_text)

def get_weapons(*texts):
    all_text = " ".join([strip_tags(t) for t in texts])
    return "|".join(weapons_words(all_text))

test_prices = ["I like to spend $50 for a sword, $75.00 for ammo, $ 100.00 for rifle, $ 1,000 for lunch, and BTC 2.468 to donate to Edward Snowden.", 
               "I make $60K a year on Herbalife.  Ask me how!",
               "JPY 500000 is more than CHF 200.5",
               "2.5 BTC or BTC 4.5"]

DOLLAR_PRICE_REGEXPS = [re.compile(r'''\$\s*(?:\d{1,3},\s?)*\d{1,3}(?:(?:\.\d+)|[KkMm])?''', re.IGNORECASE),
                        re.compile(r'''USD\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                        re.compile(r'''\d{1,7}(?:\.\d+)?\s*USD''', re.IGNORECASE)
                        ]

BITCOIN_PRICE_REGEXPS = [re.compile(r'''(?:BTC|XBT|XBC)\s*\d{1,7}(?:\.\d+)?''', re.IGNORECASE),
                         re.compile(r'''\d{1,7}(?:\.\d+)?\s*(?:BTC|XBT|XBC)''', re.IGNORECASE)
                         ]

def get_dollar_prices(*texts):
    matches = []
    for t in texts:
        for r in DOLLAR_PRICE_REGEXPS:
            for m in r.findall(t):
                matches.append(m.replace('$ ','$').replace(',','').replace('$','').replace('K',"000").replace('k',"000").replace("M","000").replace('m',"000"))
    return "|".join(matches)

def get_prices(*texts):
    return get_dollar_prices(*texts)

def get_bitcoin_prices(*texts):
    matches = []
    for t in texts:
        for r in BITCOIN_PRICE_REGEXPS:
            for m in r.findall(t):
                matches.append(m.replace('BTC','').replace('XBT','').replace('XBC','').replace(' ',''))
    return "|".join(matches)


# print get_prices(*test_prices)

def atf_body_clean(text):
    """Strip HTML"""
    return strip_tags(text).strip()

def onion_name_to_provider_name(onion):
    if onion   in ["k5zq47j6wd3wdvjq.onion"]:
        return "evolution"
    elif onion in ["i25c62nvu4cgeqyz.onion"]:
        return "evolution-forums"
    else:
        return onion

def atf_provider_name(uri):
    domain = getWebsiteDomain(uri)
    if domain.endswith('backpage.com'):
        return "backpage.com"
    elif domain.endswith('.onion'):
        return onion_name_to_provider_name(domain)
    else:
        return domain

# print test_prices, get_dollar_prices(*test_prices)
# print test_prices, get_bitcoin_prices(*test_prices)
