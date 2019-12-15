import requests
import urllib3
urllib3.disable_warnings()

def send_to_collector(server, events, collector_token):
    headers = {
        'Authorization': 'Zbrunk ' + collector_token,
    }
    r = requests.post(url=server + '/services/collector', headers=headers, json={"events":events}, verify=False)
    return(r.json())

def send_to_searcher(server,search_request):
    r = requests.post(url=server + '/services/searcher', json=search_request, verify=False)
    return(r.json())

### Global
server = "https://127.0.0.1:8088"

## Send events
events = list()
events.append({"time": "1471613579", "host": "test_host", "event": {"test_key": "test_line1"}})
events.append({"time": "1471613580", "host": "test_host", "event": {"test_key": "test_line2"}})
collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE2352B'
print("Sending Events")
print("Results: " + str(send_to_collector(server = server, events = events, collector_token = collector_token)))
# Sending Events
# Results: {'text': 'Success', 'code': 0}

## Search events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
search_request = {  "search":
                    {
                        "event_type": "test_event",
                        "time":{"from":"1471613579","to":"1471613580"}
                    },
                    "output_mode": "json",
                    "max_count":"10000000",
                    "skip":"0",
                    "auth_token":auth_token,
                 }
print("Searching for Events")
print("Results: " + str(send_to_searcher(server = server, search_request = search_request)))
# Searching for Events
# Results: {'results': [{'_id': '5df67245463fe9e64045d2b0', 'time': 1471613579, 'host': 'test_host', 'event': {'test_key': 'test_line1'}, 'event_type': 'test_event'}, {'_id': '5df67245463fe9e64045d2b1', 'time': 1471613580, 'host': 'test_host', 'event': {'test_key': 'test_line2'}, 'event_type': 'test_event'}], 'results_count': 2, 'all_results_count': 2, 'text': 'Success', 'code': 0}

## Search types of events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
get_types_request = {   "search":
                        {
                            "event_type": "test_event",
                            "time":{"from":"1471613579","to":"1471613580"}
                        },
                        "output_mode": "json",
                        "max_count":"10000000",
                        "skip":"0",
                        "auth_token":auth_token,
                        "get_types":"True"
                 }
print("Searching types of Events")
print("Results: " + str(send_to_searcher(server = server, search_request = get_types_request)))
# Searching types of Events
# Results: {'results': ['test_event'], 'results_count': 1, 'all_results_count': 0, 'text': 'Types found', 'code': 0}

### Delete events
auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
delete_request = {  "search":
                    {
                        "event_type": "test_event",
                        "time":{"from":"1471613579","to":"1471613580"}
                    },
                    "output_mode": "json",
                    "max_count":"10000000",
                    "skip":"0",
                    "auth_token":auth_token,
                    "delete":"True"
                  }
print("Deleting Events")
print("Results: " + str(send_to_searcher(server = server, search_request = delete_request)))
# Deleting Events
# Results: {'results': [], 'results_count': 0, 'all_results_count': 0, 'text': 'Events deleted', 'code': 0}