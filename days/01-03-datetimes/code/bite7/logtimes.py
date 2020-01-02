# copied from https://codechalleng.es/bites/7/ and modified with my solution.

from datetime import datetime
import os
# import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('bite7_messages.log')
# tmp = os.getenv("TMP", "/tmp")
# logfile = os.path.join(tmp, 'log')
# urllib.request.urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
#     logfile
# )

with open(logfile) as f:
    loglines = f.readlines()
    print("loglines is type ", type(loglines))



# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    # Pybites solution:
    timestamp = line.split()[1]
    date_str = '%Y-%m-%dT%H:%M:%S'
    return datetime.strptime(timestamp, date_str)

    #My SOLUTION:  IT WORKS:
    # m = re.search('^([A-Za-z]*) ([0-9:T-]*) ', line)
    # date_str = m.group(2)
    # dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
    # return dt



def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    # Pybites Solution:
    # shutdown_entries = [line for line in loglines if SHUTDOWN_EVENT in line]
    # shutdown_times = [convert_to_datetime(event) for event in shutdown_entries]
    # return max(shutdown_times) - min(shutdown_times)

    # MY SOLUTION:  IT WORKS BUT IS NOT NEARLY AS ELEGANT AS THE Pybites Solution.
    # TODO: STUDY THE Pybites Solution!!
    events = []
    for line in loglines:
        if line.find(SHUTDOWN_EVENT) != -1:
            events.append(line)

    first = events[0]
    last = events[-1]
    print("first line: ", first)
    print("last line: ", last)

    first_dt = convert_to_datetime(first)
    last_dt = convert_to_datetime(last)
    print("first datetime: ", str(first_dt))
    print("last datetime: ", str(last_dt))

    diff = last_dt - first_dt
    print("diff: ", str(diff))

    return diff
