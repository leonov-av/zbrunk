import requests
import urllib3
import time
import datetime
import re

urllib3.disable_warnings()

# Function to generate timestamps.
def get_ts(time_line):
    # It's necessary to set time and date in comfortable human readable format
    # Eg: 2019.12.10 13:00:00

    # Instead of date you can set synonyms:
    # - Today
    # - Yesterday
    # - N days ago
    # - Beginning of Time
    # - End of Time
    #
    # API will work only with timestamps

    ts = "Error"

    def full_human_readable_to_ts(date_string):
        # from 2019.12.10 13:00:00
        return int(time.mktime(datetime.datetime.strptime(date_string, '%Y.%m.%d %H:%M:%S').timetuple()))

    def get_current_date_from_ts(ts):
        return (
            datetime.datetime.fromtimestamp(
                int(ts)
            ).strftime('%Y.%m.%d')
        )

    def get_current_ts():
        return (int(time.time()))

    if re.findall("[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time_line):
        ts = full_human_readable_to_ts(time_line)

    if re.findall("Today [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time_line):
        time_line = re.sub("^Today", get_current_date_from_ts(get_current_ts()),time_line)
        ts = full_human_readable_to_ts(time_line)

    if re.findall("Yesterday [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time_line):
        time_line = re.sub("^Yesterday", get_current_date_from_ts(get_current_ts() - 86400),time_line)
        ts = full_human_readable_to_ts(time_line)

    if re.findall("[0-9]* days ago [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}", time_line):
        n_days = re.findall("([0-9]*) days ago", time_line)[0]
        time_line = re.sub("^[0-9]* days ago", get_current_date_from_ts(get_current_ts() - 86400 * int(n_days)), time_line)
        ts = full_human_readable_to_ts(time_line)

    if re.findall("Beginning of Time", time_line):
        time_line = re.sub("Beginning of Time", "1970.01.01 00:00:00", time_line)
        ts = full_human_readable_to_ts(time_line)

    if re.findall("End of Time", time_line):
        time_line = re.sub("End of Time", "2100.01.01 12:00:00", time_line)
        ts = full_human_readable_to_ts(time_line)

    if re.findall("Current", time_line):
        ts = get_current_ts()

    return str(ts)


# Adding the table
def send_to_collector(server, events, collector_token):
    headers = {
        'Authorization': 'Zbrunk ' + collector_token,
    }
    r = requests.post(url=server + '/services/collector', headers=headers, json={"events": events}, verify=False)
    return r.json()


def send_to_searcher(server, search_request):
    r = requests.post(url=server + '/services/searcher', json=search_request, verify=False)
    return r.json()
