"""
Read in a file
Extract either:
    - emails
    - urls
    - domains
    - mobile (simplified for singapore mobile only)
    - all
Write to a file
"""

import re
import urlparse


# Email regex for extraction
# A simple version
email_regex1 = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', re.IGNORECASE)
email_regex2 = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
email_regex3 = re.compile(r'[\w\.-]+@[\w\.-]+')
email_regex4 = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                     "{|}~-]+)*(@)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))

# URL regex
url_regex = re.compile('(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&@#/%=~_|$?!:,.]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)


# A convenient enum for the type of data that can be extracted
class EXTRACT_TYPE:
    EMAIL, URL, DOMAIN, MOBILE = 'email', 'url', 'domain', 'mobile'

def clean_email(x):
    """Remove all non alphabetic characters from the end of the string after the last dot"""
    try:
        clean_regex = re.compile('^.*@.+\.com')
        x = re.sub('^[^A-Za-z]+', '', x)
        x = re.sub('[^A-Za-z]+$', '', x)
        x1 = re.findall(clean_regex, x)
        if len(x1) > 0:
            x = x1[0]
        return x
    except:
        return x

def extract_emails(data):
    """
    Extract all emails from data. This includes email obfuscation techniques.
    It is impossible to cover all cases, but this method will try as many of the common cases.

    >>> extract_emails(" I love the nature especially the sand and boating. My fantasy is to have a man fu c k me on a boat only contract my gmail......rosejulia559@gmail.com")
    set(['samwize@gmail.com'])

    >>> extract_emails("Looking for a well reviewed mature sexy lady? I'm your girl. I'm new in town and looking for some fun. I provide a very discreet and unrushed experience. Very well reviewed. Ask me about my Half hour and hourly specials available. Outcall only.References preferred. If you want to have some fun contact me at 6one2nine86seventeen97 or missleilaj.2015@gmail.. Me and my friends are on Easy Sex soooo you can find us all on there if you want... skittlegirl :)")
    set(['bluebirdof.happiness@yahoo.com'])

    >>> extract_emails("JUST a little Patience is all you need! Tits ass lips and hips PatienceHunny@gmail.com.415-574-7724.")
    set(['rajr@uol.com.br'])

    >>> extract_emails('hinfai/at/gmail/dot/com')
    set(['hinfai@gmail.com'])

    >>> extract_emails('eehassell   -   at  -  hushmail.com')
    set(['eehassell@hushmail.com'])

    >>> extract_emails('kellydc[.]wanderer[@]gmail<.>com')
    set(['kellydc.wanderer@gmail.com'])

    """
    email_set = set()

    # Clean up the data for email first
    # data = cleanup_for_emails(data)

    # Extract each email
    for email in email_regex1.findall(data.lower()):
        email_set.add(clean_email(email))
    for email in email_regex2.findall(data.lower()):
        email_set.add(clean_email(email))
    for email in email_regex3.findall(data.lower()):
        email_set.add(clean_email(email))
    for email in email_regex4.findall(data.lower()):
        email_set.add(clean_email(email[0]))

    return ",".join(email_set)

#
# def extract_urls(data):
#     """
#     Extract URLs from data.
#
#     >>> extract_urls('yoyoyo http://www.regexguru.com/2008/11/detecting-urls-in-a-block-of-text/ yoyoyo')
#     set(['http://www.regexguru.com/2008/11/detecting-urls-in-a-block-of-text/'])
#
#     >>> extract_urls('ohoho\nhttp://www.google.com.sg/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CHQQFjAB&url=http%3A%2F%2Fwww.junda.com%2F&ei=faoXUMKNEsWGrAfhm4DwCg&usg=AFQjCNFXDbUHvVhdvVkPuSgDVU-Pb01EiA&sig2=EkLM-_6En7Jg4_XVAzQYAQ me too\nme too')
#     set(['http://www.google.com.sg/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0CHQQFjAB&url=http%3A%2F%2Fwww.junda.com%2F&ei=faoXUMKNEsWGrAfhm4DwCg&usg=AFQjCNFXDbUHvVhdvVkPuSgDVU-Pb01EiA&sig2=EkLM-_6En7Jg4_XVAzQYAQ'])
#
#     >>> extract_urls('https://a.b.com http://a.b.org')
#     set(['https://a.b.com', 'http://a.b.org'])
#
#     """
#     _set = set()
#     for x in url_regex.findall(data):
#         _set.add(x)
#     return _set

