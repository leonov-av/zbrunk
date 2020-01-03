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


### Global
server = "https://127.0.0.1:8088"

# Time function examples:
time_line = "Today 13:00:00"
print(time_line + " - " + get_ts(time_line))
time_line = "Today 00:00:00"
print(time_line + " - " + get_ts(time_line))
time_line = "Today 23:59:59"
print(time_line + " - " + get_ts(time_line))
time_line = "Yesterday 13:00:00"
print(time_line + " - " + get_ts(time_line))
time_line = "1 days ago 13:00:00"
print(time_line + " - " + get_ts(time_line))
time_line = "10 days ago 13:00:00"
print(time_line + " - " + get_ts(time_line))
time_line = "Beginning of Time"
print(time_line + " - " + get_ts(time_line))
time_line = "End of Time"
print(time_line + " - " + get_ts(time_line))
time_line = "Current"
print(time_line + " - " + get_ts(time_line))

## Send events
events = list()
events.append({"time": get_ts("Current"), "event_type": "test_event", "host": "test_host", "event": {"test_key": "test_line1"}})
events.append({"time": get_ts("Current"), "event_type": "test_event", "host": "test_host", "event": {"test_key": "test_line2"}})
collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE23441'
print("Sending Events")
print("Results: " + str(send_to_collector(server=server, events=events, collector_token=collector_token)))
# Sending Events
# Results: {'text': 'Success', 'code': 0}

## Search events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Events")
print("Results: " + str(send_to_searcher(server=server, search_request=search_request)))
# Searching for Events
# Results: {'results': [{'_id': '5df67245463fe9e64045d2b0', 'time': 1471613579, 'host': 'test_host', 'event': {'test_key': 'test_line1'}, 'event_type': 'test_event'}, {'_id': '5df67245463fe9e64045d2b1', 'time': 1471613580, 'host': 'test_host', 'event': {'test_key': 'test_line2'}, 'event_type': 'test_event'}], 'results_count': 2, 'all_results_count': 2, 'text': 'Success', 'code': 0}

## Search types of events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
get_types_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "get_types": "True"
}
print("Searching types of Events")
print("Results: " + str(send_to_searcher(server=server, search_request=get_types_request)))
# Searching types of Events
# Results: {'results': ['test_event'], 'results_count': 1, 'all_results_count': 0, 'text': 'Types found', 'code': 0}

### Delete events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Events")
print("Results: " + str(send_to_searcher(server=server, search_request=delete_request)))
# Deleting Events
# Results: {'results': [], 'results_count': 0, 'all_results_count': 0, 'text': 'Events deleted', 'code': 0}

##### Tables

### Sending Table Events
events = list()
events.append({"time": get_ts("Current"), "event_type": "test_table_settings", "host": "test_host", "event": {"title":"Important Table", "col_order":["col1","col2"]}})
events.append({"time": get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value1", "col2":"valuе2"}}})
events.append({"time": get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value3", "col2":"valuе4"}}})
events.append({"time": get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value5", "col2":"valuе6"}}})
collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE23441'
print("Sending Table Events")
print("Results: " + str(send_to_collector(server=server, events=events, collector_token=collector_token)))

## Searching for Table Settings Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_table_settings",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "1",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Table Settings Events")
print("Results: " + str(send_to_searcher(server=server, search_request=search_request)))
# Searching for Table Content Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_table_content",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "2",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Table Content Events")
print("Results: " + str(send_to_searcher(server=server, search_request=search_request)))

### Deleting Table Settings Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_table_settings",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Table Settings Events")
print("Results: " + str(send_to_searcher(server=server, search_request=delete_request)))

# Deleting Table Content Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_table_content",
        "time": {"from": get_ts("Today 00:00:00"), "to": get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Table Content Events")
print("Results: " + str(send_to_searcher(server=server, search_request=delete_request)))