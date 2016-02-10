__author__ = 'amandeep'

from datetime import datetime
from time import mktime, gmtime
import calendar

class DM(object):

    def __init__(self):
        self.name = "Date Manipulation"

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
        # If all else fails, return input
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
    def epoch_to_iso8601(timestamp):
        ts=float(timestamp)
        if len(timestamp) == 13:
            ts = ts/1000
        return datetime.fromtimestamp(ts).isoformat()

    @staticmethod
    def get_year_from_iso_date(iso_date):
        if iso_date:
            return iso_date[0:4]
        return ''

    @staticmethod
    def get_current_time():
        return datetime.today().strftime("%Y-%m-%d %H:%M:%S")
