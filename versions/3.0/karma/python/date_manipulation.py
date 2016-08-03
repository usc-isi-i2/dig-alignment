__author__ = 'amandeep'

import calendar
import re
from datetime import datetime
from datetime import date
from datetime import timedelta
from time import mktime, gmtime


class DM(object):
    def __init__(self):
        self.name = "Date Manipulation"

    days_long = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    days_long_regex = r"|".join(days_long)

    months_dict = {
        "01": 1,
        "1": 1,
        "02": 2,
        "2": 2,
        "03": 3,
        "3": 3,
        "04": 4,
        "4": 4,
        "05": 5,
        "5": 5,
        "06": 6,
        "6": 6,
        "07": 7,
        "7": 7,
        "08": 8,
        "8": 8,
        "09": 9,
        "9": 9,
        "10": 10,
        "11": 11,
        "12": 12,
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "de": 12,
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
        "janvier": 1,
        "fevrier": 2,
        "fvrier": 2,
        "mars": 3,
        "avril": 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "aout": 8,
        "aot": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "decempre": 12,
        "janeiro": 1,
        "fevereiro": 2,
        "marco": 3,
        # "abril": 4,
        "maio": 5,
        "junho": 6,
        "julho": 7,
        # "agosto": 8,
        "setembro": 9,
        "setiembre": 9,
        "outubro": 10,
        "novembro": 11,
        "dezembro": 12,
        "gennaio": 1,
        "febbraio": 2,
        # "marzo": 3,
        "aprile": 4,
        "maggio": 5,
        "giugno": 6,
        "luglio": 7,
        # "agosto": 8,
        "settembre": 9,
        "ottobre": 10,
        # "novembre": 11,
        "dicembre": 12,
        "januar": 1,
        # "februar": 2,
        "marz": 3,
        # "april": 4,
        # "mai": 5,
        "juni": 6,
        "juli": 7,
        # "august": 8,
        # "september": 9,
        "oktober": 10,
        # "november": 11,
        "dezember": 12,
        # "januar": 1,
        # "februar": 2,
        "marts": 3,
        # "april": 4,
        "maj": 5,
        # "juni": 6,
        # "juli": 7,
        # "august": 8,
        # "september": 9,
        # "oktober": 10,
        # "november": 11,
        # "december": 12
    }


    months_long_regex = r"|".join(months_dict.keys())
    # Adult service regex
    # Thursday, September 4, 2014, 4:57 PM PST
    adultservice_regex_day = r"(" + months_long_regex + r")\s+(\d\d?),\s+(\d\d\d\d)"

    # Citiguide regex
    # September 9, 2012  10:29 AM
    citiguide_regex_day = r"(" + months_long_regex +r")\s+(\d\d?),\s+(\d\d\d\d)"

    # anunico regex
    # Domingo, 20
    # Diciembre, 2009 & nbsp;
    # 04:11
    anunico_regex_day = r"(\d\d?)\s(" + months_long_regex + r"),\s+(\d\d\d\d)"

    # craigslist regex
    # 2013-12-04,  7:44PM CST
    craigslist_regex_day = r"(\d\d\d\d)-(\d\d)-(\d\d)"

    # backpage regex
    # saturday, 1 february 2014, 12:03 am
    # friday, december 6, 2013 3:16 pm
    backpage1_regex_day = r"(\d\d?)\s+(" + months_long_regex + r")\s+(\d\d\d\d)"
    backpage2_regex_day = r"(" + months_long_regex + r")\s+(\d\d?),\s+(\d\d\d\d)"

    # myproviderguide regex
    # wednesday, april 16th, 2014
    myproviderguide_regex_day = r"(" + months_long_regex + r")\s+(\d\d?)\w+,\s+(\d\d\d\d)"

    # sipsap regex
    # wednesday, april 16th, 2014
    sipsap_regex_day = r"(" + months_long_regex + r")\s+(\d\d?)\w+\s+(\d\d\d\d)"

    # 9 days ago
    days_relative_regex = r'(\b\d\d?)\s+days?\s+ago\b'

    # 22 hours ago
    hours_relative_regex = r'(\b\d\d?)\s+hours?\s+ago\b'

    # spanish backpage regex
    # sábado, 9 de julio de 2016, 13:39
    #  lunes, 27 de junio de 2016, 14:07
    # lunes, 4 de julio de 2016, 9:01
    backpage3_regex_day = r"(\d\d?)\s+de\s+(" + months_long_regex + r")\s+de\s+(\d\d\d\d)"

    # european backpahe dates
    # torsdag, 7. juli 2016, 12:01
    backpage4_regex_day = r"(\d\d?)\.\s+(" + months_long_regex + r")\s+(\d\d\d\d)"

    @staticmethod
    def make_iso(yyyy, mm, dd, format='time'):
        """Make an iso date.
        :param yyyy: the year as 4 digits
        :param mm: the month as a name or digits, looked up in
        :return:
        """
        try:
            month = int(DM.months_dict[mm])
            day = int(dd)
            year = int(yyyy)
            if year < 2008 or year > 2016:
                return ''
            if format == 'time':
                return datetime(year, month, day).isoformat()
            else:
                return date(year, month, day).isoformat()
        except Exception:
            return ''

    @staticmethod
    def datetime_to_iso(time, format='time'):
        """"""
        if format == 'time':
            return time.isoformat()
        else:
            return time.date().isoformat()

    # 1 Jul
    date_month_relative_regex = r"(\d\d?)\s+(" + months_long_regex + r")\b"

    # 3. jul
    date_month_relative_regex_2 = r"(\d\d?)\.\s+(" + months_long_regex + r")\b"

    # Jul-01
    date_month_relative_regex_3 = r"(" + months_long_regex + r")-(\d\d?)\b"

    # Jun 25
    date_month_relative_regex_4 = r"(" + months_long_regex + r")\s+(\d\d?)\b"

    @staticmethod
    def extract_relative_date(str, base_time, format='time'):
        """"""
        str = str.lower().strip()
        try:
            tuples = re.findall(DM.days_relative_regex, str)
            if (len(tuples) > 0):
                (days) = tuples[0]
                base_time -= timedelta(days=int(days))
                return DM.datetime_to_iso(base_time, format=format)
            else:
                tuples = re.findall(DM.hours_relative_regex, str)
                if (len(tuples) > 0):
                    (hours) = tuples[0]
                    base_time -= timedelta(hours=int(hours))
                    return DM.datetime_to_iso(base_time, format=format)
        except:
            return ''

        base_year = "2016"
        try:
            if base_time:
                base_year = str(base_time.year)
        except:
            pass

        tuples = re.findall(DM.date_month_relative_regex, str)
        if (len(tuples) > 0):
            (d, m) = tuples[0]
            return DM.make_iso(base_year, m, d, format)

        tuples = re.findall(DM.date_month_relative_regex_2, str)
        if (len(tuples) > 0):
            (d, m) = tuples[0]
            return DM.make_iso(base_year, m, d, format)

        tuples = re.findall(DM.date_month_relative_regex_3, str)
        if (len(tuples) > 0):
            (m, d) = tuples[0]
            return DM.make_iso(base_year, m, d, format)

        tuples = re.findall(DM.date_month_relative_regex_4, str)
        if (len(tuples) > 0):
            (m, d) = tuples[0]
            return DM.make_iso(base_year, m, d, format)

        return ''


    @staticmethod
    def posttime_date(str, default_time, format='time'):
        """
        default_time can be None
        """
        # print "default_time ",
        # print default_time
        str = str.lower().strip()
        tuples = re.findall(DM.adultservice_regex_day, str)
        if (len(tuples) > 0):
            (m, d, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.citiguide_regex_day, str)
        if (len(tuples) > 0):
            (m, d, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.anunico_regex_day, str)
        if (len(tuples) > 0):
            (d, m, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.craigslist_regex_day, str)
        if (len(tuples) > 0):
            (y, m, d) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.backpage1_regex_day, str)
        if (len(tuples) > 0):
            (d, m, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.backpage2_regex_day, str)
        if (len(tuples) > 0):
            (m, d, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.backpage3_regex_day, str)
        if len(tuples) > 0:
            (d, m, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.backpage4_regex_day, str)
        if len(tuples) > 0:
            (d, m, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.myproviderguide_regex_day, str)
        if (len(tuples) > 0):
            (m, d, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        tuples = re.findall(DM.sipsap_regex_day, str)
        if (len(tuples) > 0):
            (m, d, y) = tuples[0]
            return DM.make_iso(y, m, d, format)

        last_ditch_parse = DM.iso8601date(str, format)
        if last_ditch_parse:
            if format=='time':
                return last_ditch_parse
            else:
                reparse_datetime = datetime.datetime.strptime(last_ditch_parse, "%Y-%m-%dT%H:%M:%S")
                # reparse_datetime = dateutil.parser.parse(last_ditch_parse)
                return reparse_datetime.date().isoformat()

        if default_time and default_time != '':
            if default_time > datetime(2000,1,1):
                if format == 'time':
                    return default_time.isoformat()
                else:
                    return default_time.date().isoformat()
            else:
                return ''
        else:
            return ''

    @staticmethod
    def date_created(posttime, crawl_time, format='time'):
        """
        return DM.date_created(getValue("posttime_extraction"), getValue("timestamp"))
        Construct iso time from posttime and crawl_time.
        :param posttime: extracted string of posted data, in arbitrary format.
        :type posttime: string
        :param crawl_time: epoch of time when the page was crawled, known to be inaccurate.
        :type crawl_time: string
        :return: if posttime can be parsed, then return it, otherwise return the crawl_time
        """
        default_time = None
        try:
            default_time = datetime.strptime(crawl_time, "%Y-%m-%dT%H:%M:%S")
        except:
            pass
        parsed_date = DM.posttime_date(posttime, None, format)
        if parsed_date == '':
            parsed_date = DM.extract_relative_date(posttime, default_time, format)
        return parsed_date
    
    @staticmethod
    def iso8601date(date, date_format=None):
        """Convert a date to ISO8601 date format
        input format: YYYY-MM-DD HH:MM:SS GMT (works less reliably for other TZs)
        or            YYYY-MM-DD HH:MM:SS.0
        or            YYYY-MM-DD
        or            epoch (13 digit, indicating ms)
        or            epoch (10 digit, indicating sec)
        output format: iso8601"""
        date = date.strip()

        if date_format:
            try:
                return datetime.strptime(date, date_format).isoformat()
            except Exception:
                pass

        try:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").isoformat()
        except:
            pass

        try:
            # Friday, October 2, 2015 1:35 AM
            return datetime.strptime(date, "%A, %B %d, %Y %I:%M %p").isoformat()
        except:
            pass

        try:
            # Friday, 2 October 2015, 18:23
            return datetime.strptime(date, "%A, %d %B %Y, %H:%M").isoformat()
        except:
            pass

        try:
            # Thu October 01st, 2015
            return datetime.strptime(date, "%a %B %dst, %Y").isoformat()
        except:
            pass

        try:
            # Thu October 02nd, 2015
            return datetime.strptime(date, "%a %B %dnd, %Y").isoformat()
        except:
            pass

        try:
            # Thu October 03rd, 2015
            return datetime.strptime(date, "%a %B %drd, %Y").isoformat()
        except:
            pass

        try:
            # Thu October 04th, 2015
            return datetime.strptime(date, "%a %B %dth, %Y").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S %Z").isoformat()
        except Exception:
            pass

        try:
            return datetime.strptime(date, "%A, %b %d, %Y").isoformat()
        except Exception:
            pass

        try:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.0").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%Y-%m-%d").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%b %d, %Y").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%B %d, %Y").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%B %d, %Y %I:%M %p").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%b %d, %Y at %I:%M %p").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%m-%d-%Y").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").isoformat()
        except:
            pass

        try:
            return datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").isoformat()
        except:
            pass

        try:
            date = int(date)
            if 1000000000000 < date < 9999999999999:
                # 13 digit epoch
                return datetime.fromtimestamp(mktime(gmtime(date / 1000))).isoformat()
        except:
            pass

        try:
            date = int(date)
            if 1000000000 < date < 9999999999:
                # 10 digit epoch
                return datetime.fromtimestamp(mktime(gmtime(date))).isoformat()
        except:
            pass
        # If all else fails, return empty
        return ''


    @staticmethod
    def translate_date(string, in_format, out_format):
        """Convert a date to ISO8601 date format without time"""
        try:
            return datetime.strptime(string.strip(), in_format).date().strftime(out_format)
        except Exception:
            pass
        return ''


    @staticmethod
    def conver_time_to_epoch(date, format=None):
        date = date.strip()

        if format:
            try:
                calendar.timegm(datetime.strptime(date, format).timetuple())
            except:
                pass
        try:
            return calendar.timegm(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").timetuple())
        except:
            pass
        return ''


    @staticmethod
    def epoch_to_datetime(timestamp):
        try:
            ts = float(timestamp)
            if len(timestamp) == 13:
                ts = ts / 1000
            elif len(timestamp) == 16:
                ts = ts / 1000000
            return datetime.fromtimestamp(ts)
        except:
            return None

    @staticmethod
    def epoch_to_iso8601(timestamp):
        return DM.epoch_to_datetime(timestamp).isoformat()

    @staticmethod
    def get_year_from_iso_date(iso_date):
        if iso_date:
            return iso_date[0:4]
        return ''


    @staticmethod
    def get_current_time():
        return datetime.today().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    filename = "../../test/posttime/adultsearch-dates.txt"
    filename = "../../test/posttime/cityxguide-dates.txt"
    filename = "../../test/posttime/escortsincollege-dates.txt"
    filename = "../../test/posttime/rubads-dates.txt" # 26 October # no year!
    filename = "../../test/posttime/anunico-dates.txt"
    filename = "../../test/posttime/craigslist-dates.txt"
    filename = "../../test/posttime/massagetroll-dates.txt"
    filename = "../../test/posttime/backpage-dates.txt"
    filename = "../../test/posttime/eroticmugshots-dates.txt"
    filename = "../../test/posttime/myproviderguide-dates.txt"
    filename = "../../test/posttime/cityvibe-dates.txt" # tuesday, march 25th at 10:49 am # no year!
    filename = "../../test/posttime/escortphonelist-dates.txt"
    filename = "../../test/posttime/naughtyreviews-dates.txt"
    filename = "../../test/posttime/sipsap-dates.txt"
    filename = "../../test/posttime/classivox-dates.txt"
    filename = "../../test/posttime/liveescortreviews-dates.txt"

    # with open(filename, "r") as dates_file:
    #     for d in dates_file.readlines():
    #         print "l=%s" % d.strip().lower()
    #         d = d.strip().lower()
    #         date = DM.iso8601date(d)
    #         print ">>>%s" % date

    #print DM.date_created("Posted:Thursday, June 2, 2016 10:35 PM", "1399273701000", 'date')

    # print DM.date_created(""""HYDERABAD (07768032817 - 21\n\n    \n  \n\n\n  \n    Posted: \n    Monday, 11 January 2016, 21:36\n  \n\n  \n    \n\n  \n  \n""", "2016-06-27T19:58:11", 'time')
    # print DM.date_created("Posted:Thursday, June 2, 2016 10:35 PM", "2016-06-27T19:58:11", 'date')
    # print DM.date_created("2016xc sd-01-11T0sf0:00:00", "2016-06-27T19:58:15", 'date')
    # print DM.extract_relative_date("Posted 9:99 days ago, etc posted 29 hours ago", datetime.now(), format='date')
    # print DM.date_created("Posted:\r\n    Thursday, June 2, 2016 10:35 PM\r\n   \n \n \n \n \r\n      \r\n\r\n      \r\n\r\n      \r\n        \r\n        \r\n          Hey Guy's come ", "2016-06-27T19:58:11", 'date')
    # print DM.date_created("online: Jul 07, 00:44 \n  Posted: Fri. 1 Jul., 21:19 \n \n \n", "2016-06-27T19:58:11", 'date')
    print DM.date_created("online: Jul 07, 00:44 \n  ", "2016-06-27T19:58:11",
                          'date')
    # 07 / 07 / 2016    136781205
    # Last Updated:   2016-07-07 20:52:53
