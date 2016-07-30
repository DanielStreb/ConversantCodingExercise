"""MakeReadable.py."""
from datetime import datetime
import matplotlib.dates as dt

from pytz import utc


def human_readable(epoch_time=0):
    """Function to convert epoch time to a human-readable format."""
    return dt.date2num(datetime.fromtimestamp(epoch_time, utc))

print(human_readable(1347517370))
# print(human_readable())
# print(time.asctime(time.gmtime(1347517370)))
