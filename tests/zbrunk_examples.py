import zbrunk_functions

### Global
server = "https://127.0.0.1:8088"

# Time function examples:
time_line = "Today 13:00:00"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "Today 00:00:00"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "Today 23:59:59"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "Yesterday 13:00:00"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "1 days ago 13:00:00"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "10 days ago 13:00:00"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "Beginning of Time"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "End of Time"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))
time_line = "Current"
print(time_line + " - " + zbrunk_functions.get_ts(time_line))

## Send events
events = list()
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_event", "host": "test_host", "event": {"test_key": "test_line1"}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_event", "host": "test_host", "event": {"test_key": "test_line2"}})
collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE23441'
print("Sending Events")
print("Results: " + str(zbrunk_functions.send_to_collector(server=server, events=events, collector_token=collector_token)))
# Sending Events
# Results: {'text': 'Success', 'code': 0}

## Search events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=search_request)))
# Searching for Events
# Results: {'results': [{'_id': '5df67245463fe9e64045d2b0', 'time': 1471613579, 'host': 'test_host', 'event': {'test_key': 'test_line1'}, 'event_type': 'test_event'}, {'_id': '5df67245463fe9e64045d2b1', 'time': 1471613580, 'host': 'test_host', 'event': {'test_key': 'test_line2'}, 'event_type': 'test_event'}], 'results_count': 2, 'all_results_count': 2, 'text': 'Success', 'code': 0}

## Search types of events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
get_types_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "get_types": "True"
}
print("Searching types of Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=get_types_request)))
# Searching types of Events
# Results: {'results': ['test_event'], 'results_count': 1, 'all_results_count': 0, 'text': 'Types found', 'code': 0}

### Delete events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_event",
        "time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=delete_request)))
# Deleting Events
# Results: {'results': [], 'results_count': 0, 'all_results_count': 0, 'text': 'Events deleted', 'code': 0}

##### Tables

### Sending Table Events
events = list()
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_table_settings", "host": "test_host", "event": {"title":"Important Table", "col_order":["col1","col2"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value1", "col2":"valuе2"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value3", "col2":"valuе4"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "test_table_content", "host": "test_host", "event": {"content":{"col1":"value5", "col2":"valuе6"}}})
collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE23441'
print("Sending Table Events")
print("Results: " + str(zbrunk_functions.send_to_collector(server=server, events=events, collector_token=collector_token)))

## Searching for Table Settings Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_table_settings",
        "time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "1",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Table Settings Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=search_request)))
# Searching for Table Content Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {"search":
    {
        "event_type": "test_table_content",
        "time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
    },
    "output_mode": "json",
    "max_count": "2",
    "skip": "0",
    "auth_token": auth_token,
}
print("Searching for Table Content Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=search_request)))

### Deleting Table Settings Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_table_settings",
        #"time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
        "time": {"from": zbrunk_functions.get_ts("Beginning of Time"), "to": zbrunk_functions.get_ts("End of Time")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Table Settings Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=delete_request)))

# Deleting Table Content Events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {"search":
    {
        "event_type": "test_table_content",
        #"time": {"from": zbrunk_functions.get_ts("Today 00:00:00"), "to": zbrunk_functions.get_ts("Today 23:59:59")}
        "time": {"from": zbrunk_functions.get_ts("Beginning of Time"), "to": zbrunk_functions.get_ts("End of Time")}
    },
    "output_mode": "json",
    "max_count": "10000000",
    "skip": "0",
    "auth_token": auth_token,
    "delete": "True"
}
print("Deleting Table Content Events")
print("Results: " + str(zbrunk_functions.send_to_searcher(server=server, search_request=delete_request)))