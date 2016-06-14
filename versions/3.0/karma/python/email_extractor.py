import re
import json
from sets import Set

class EE(object):
    """Extractor of email addresses from text.
    The legal definition is in https://en.wikipedia.org/wiki/Email_address

    This class attempts to map purposefully obfuscated email addresses to legal addresses.

    Users of this class should call EE.extract_email(), see documentation.
    The main program is to test against the ground truth.
    """

    common_domains = [
        "gmail",
        "gee mail",
        "g mail",
        "gml",
        "yahoo",
        "hotmail"
    ]
    common_domains_regex = "(?:" + "|".join(common_domains) + ")"

    gmail_synonyms = [
        "gee mail",
        "g mail"
        "gml"
    ]
    gmail_synonyms_regex = "(?:" + "|".join(gmail_synonyms) + ")"

    com_synonyms = [
        r"com\b",
        r"co\s*\.\s*\w\w\w?",
        r"co\s+dot\s+\w\w\w?"
    ]
    com_synonyms_regex = r"(?:" + "|".join(com_synonyms) + ")"

    # The intent here is to match things like "yahoo com", "yahoo dot com"
    # We require matching the com synonyms to avoid interpreting text that contains "at yahoo" as part of a domain name.
    spelled_out_domain_regex = r"(?:" + common_domains_regex + "(?:(?:dot\s+|\.+|\,+|\s+)" + com_synonyms_regex + "))"
    # print "spelled_out_domain_regex:%s" % spelled_out_domain_regex

    at_regexes = [
        r"@",
        r"\(+@\)+",
        r"\[+@\]+",
        r"\(+(?:at|arroba)\)+",
        r"\[+(?:at|arroba)\]+",
        r"\{+(?:at|arroba)\}+",
        r"\s+(?:at|arroba)@",
        r"@at\s+",
        r"at\s+(?=" + spelled_out_domain_regex + ")",
        r"(?<=\w\w\w|\wat)\s+(?=" + spelled_out_domain_regex + ")",
        r"(?<=\w\w\w|\wat)\[\](?=" + spelled_out_domain_regex + "?" + ")"
    ]
    at_regex = "(?:" + r'|'.join(at_regexes) + ")"
    # print "at_regex:%s" % at_regex

    # People put junk between the "at" sign and the start of the domain
    at_postfix_regexes = [
        ",+\s*",
        "\.+\s*"
    ]
    at_postfix_regex = "(?:" + r'|'.join(at_postfix_regexes) + ")?"

    full_at_regex = at_regex + at_postfix_regex + "\s*"
    # print "full_at_regex:%s" % full_at_regex

    # Character set defined by the standard
    basic_dns_label_regex = r"[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9]"
    non_dns_regex = r"[^a-zA-Z0-9\-.]"

    # Sometimes people do things like maria at (yahoo) (dot) (com)
    wrapped_basic_dns_label_regexes = [
        basic_dns_label_regex,
        "\(+" + basic_dns_label_regex + "\)+",
        "\[+" + basic_dns_label_regex + "\]+"
    ]
    dns_label_regex = "(?:" + "|".join(wrapped_basic_dns_label_regexes) + ")"

    # People put all kinds of junk between the parts of a domain name
    dot_regex = "[(\[]*dot[)\]]*"
    dns_separator_regexes = [
        "\s*\.+\s*",
        "[\.\s]+" + dot_regex + "[\.\s]+",
        "\(+(?:\.|" + dot_regex + ")+\)+",
        "\[+\.+\]+",
        "\{+\.+\}+",
        "\s+(?=" + com_synonyms_regex + ")"
    ]
    dns_separator_regex = "(?:" + ",*" + "|".join(dns_separator_regexes) + ",*" + ")"

    dns_re = full_at_regex + r"(" + dns_label_regex + r"(?:" + dns_separator_regex + dns_label_regex + r")*)"

    #
    # Regex for the user name part of legal addresses.
    # Assuming all text has been lowercased before.
    #
    # Assuming that special characters are not used, this can be added later.
    # from wikipedia: space and "(),:;<>@[\] characters are allowed with restrictions
    # all allowed: !#$%&'*+-/=?^_`{|}~ and space
    # allowed without quoting: !#$%&'*+-/?^_`{|}~, dot can appear, but not at the beginning

    # The full set requires starting with alphanumeric, this is because of all the junk
    # that appears often. Also require at least 4 characters.
    # full_username_regex = r"[a-z0-9][a-z0-9.!#$%&'*+-/?^_`{|}~]{3,}"
    full_username_regex = r"[a-z0-9]+(?:[-.!#$%&'*+/?^_`{|}~][a-z0-9]+)*"

    # The basic regex is for cases when there is no @ sign, which means there was plenty
    # of obfuscation and the potential for all kinds of decoration which we don't want in
    # the email address. We don't allow consecutive punctuation to avoid grabbing emails
    # such as me.......LouiseHolland41@gmail
    basic_username_regex = r"(?:[a-z0-9]+(?:(?:[-+_.]|[(]?dot[)]?)[a-z0-9]+)*\s*)"

    # use lookahead to find the @ immediately following the user name, with possible spaces.
    strict_username_regex = r"(?:" + full_username_regex + r"(?=@))"

    username_regex = r"(" + basic_username_regex + r"|" + strict_username_regex + r")"

    email_regex = username_regex + dns_re
    print email_regex

    @staticmethod
    def clean_domain(regex_match):
        """Once we compute the domain, santity check it, being conservative and throwing out
        suspicious domains. Prefer precision to recall.

        :param regex_match: the output of our regex matching
        :type regex_match: string
        :return:
        :rtype:
        """
        # print "clean_domain:%s" % regex_match
        result = regex_match
        result = re.sub(EE.gmail_synonyms_regex, "gmail", result)
        result = re.sub("\s+", ".", result)
        result = re.sub(EE.dot_regex, ".", result)
        result = re.sub(EE.non_dns_regex, "", result)
        result = re.sub("\.+", ".", result)
        result = result.strip()

        # If the domain ends with one of the common domains, add .com at the end
        if re.match(EE.common_domains_regex + "$", result):
            result += ".com"
        # All domains have to contain a .
        if result.find('.') < 0:
            return ''
        # If the doman contains gmail, it has has to be gmail.com
        # This is drastic because of examples such as "at faithlynn1959@gmail. in call"
        if result.find('gmail') >= 0:
            if result != 'gmail.com':
                return ''
        return result

    @staticmethod
    def clean_username(string):
        """

        :param string:
        :type string:
        :return:
        :rtype:
        """
        username = string.strip()
        username = re.sub("[(]?dot[)]?", '.', username)
        return username

    @staticmethod
    def extract_domain(string):
        """Extract the domain part of an email address within a string.
        Separate method used for testing purposes only.
        :param string:
        :return:
        :rtype:
        """
        matches = re.findall(EE.dns_re, string, re.I)

        clean_results = []
        for m in matches:
            clean_results.append(EE.clean_domain(m))
            print("domains: "+', '.join(clean_results))
        print "\n"
        return clean_results

    @staticmethod
    def extract_email(string, return_as_string=False):
        """Extract email address from string.
        :param string: the text to extract from
        :param return_as_string: whether to return the result as a string of comma-separated values or
        as a set
        :type return_as_string: Boolean
        """
        string = string.lower().replace('\n', ' ').replace('\r', '')
        line = re.sub(r"[*?]+", " ", string)
        line = re.sub(r"\\n", " ", string)
        line = re.sub(r"\s+g\s+mail\s+", " gmail ", line)
        # print line
        #return EE.extract_domain(line)

        matches = re.findall(EE.email_regex, string)

        clean_results = Set()
        for (u, d) in matches:
            print "user: %s, domain: %s" % (u, d)
            domain = EE.clean_domain(d)
            username = EE.clean_username(u)
            if domain:
                email = username + "@" + domain
                clean_results.add(email)
                # print ">>> %s" % email
        if return_as_string:
            return ",".join(clean_results)
        else:
            return clean_results



if __name__ == '__main__':
    # file = open('/Users/pszekely/Downloads/ht-email/ht-email.txt', 'r')
    # file = open('/Users/pszekely/Downloads/ht-email/jakarta.txt', 'r')
    # file = open('/Users/pszekely/Downloads/ht-email/test.txt', 'r')
    # file = open('/Users/pszekely/Downloads/ht-email/emails.txt', 'r')

    # line = "oikqlthi @ gmail commy GmaiL.. nude.ass33"
    # line = "@ashleyspecialselect@gmail .com"
    # line = "My personal gmail....wowboobs7"
    # line = "My personal gmail....cum2mom"
    # line = "[atmashraffreelancer gmail com]"
    # line = "\nSweetAbby90 at gmail\n" # this should be a separate pattern as it is all in one line
    # EE.extract_email(line)

    with open('../../training/emails_ground_truth.json') as gt_file:
        ground_truth = json.load(gt_file)

        correct = 0
        incorrect = 0
        incorrectly_extracted = []
        for r in ground_truth:
            sentence = r["sentence"]
            # print "as string: %s" % EE.extract_email(sentence, True)
            emails = EE.extract_email(sentence)
            if len(emails) == 0:
                print "~~~ no extractions"
            for e in emails:
                if e in r["emails"]:
                    correct += 1
                    print "+++ %s" % e
                else:
                    if len(r["emails"]) > 0:
                        incorrect += 1
                        r["extracted"] = e
                        incorrectly_extracted.append(r)
                    print "--- got: %s, expected: %s" % (e, r["emails"])
                print "\n"

        print json.dumps(incorrectly_extracted, indent=4)
        print "\ncorrect %d, incorrect %d" % (correct, incorrect)
        print len(ground_truth)
