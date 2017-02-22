from HTMLParser import HTMLParser

test_signature = "<span style=\"font-style: italic\">Precision Combat Arms<br />1710 E Trent, Unit 1<br />Spokane, " \
                 "WA 99202<br />509-535-0655<br />M-F 9-5</span></div>"


class HM(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
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

    @staticmethod
    def strip_tags(html):
        s = HM()
        s.feed(html)
        return s.get_data()

    @staticmethod
    def clean_html_tags(text):
        """Strip HTML"""
        try:
            clean_text = HM.strip_tags(text).strip()
            return clean_text
        except Exception, e:
            return text

    @staticmethod
    def remove_junk(x):
        result=""
        junk = ["A", "DIV", "ESCORTS", "B", "WINDOW", "DOCTYPE", "HTML", "PUBLIC", "INITIAL", "SCALE", "1", "END", "HEADER"]
        values = x.split(" ")
        if len(values) > 1:
            for value in values:
                if value.upper() not in junk:
                    result += value + " "
            return result.strip()
        else:
            return x.strip()
        
