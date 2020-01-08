import zbrunk_functions

### Global
server = "https://127.0.0.1:8088"

##### Tables

def delete_all_events_by_type(event_type):
    ### Deleting Table Settings Events
    auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512"
    delete_request = {"search":
        {
            "event_type": event_type,
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

delete_all_events_by_type("agent_installation_table_settings")
delete_all_events_by_type("agent_installation_table_content")
delete_all_events_by_type("agent_installed_informer_table_settings")
delete_all_events_by_type("agent_installed_informer_table_content")
delete_all_events_by_type("agent_not_installed_informer_table_settings")
delete_all_events_by_type("agent_not_installed_informer_table_content")
delete_all_events_by_type("agent_installation_coverage_informer_table_settings")
delete_all_events_by_type("agent_installation_coverage_informer_table_content")
delete_all_events_by_type("agent_installation_coverage_dynamics_table_settings")
delete_all_events_by_type("agent_installation_coverage_dynamics_table_content")

### Sending Table Events
events = list()
# Agent Installation
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_settings", "host": "test_host", "event": {"title":"Agent Installation", "col_order":["Host","Agent is installed"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host1", "Agent is installed":"+"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host2", "Agent is installed":"+"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host3", "Agent is installed":"-"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host4", "Agent is installed":"+"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host5", "Agent is installed":"-"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_table_content", "host": "test_host", "event": {"content":{"Host":"host5", "Agent is installed":"+"}}})
# Agent is Installed informer
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installed_informer_table_settings", "host": "test_host", "event": {"title":"Agent is installed", "col_order":["Agent is installed"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installed_informer_table_content", "host": "test_host", "event": {"content":{"Agent is installed":"4"}}})
# Agent is NOT Installed informer
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_not_installed_informer_table_settings", "host": "test_host", "event": {"title":"Agent is NOT installed", "col_order":["Agent is NOT installed"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_not_installed_informer_table_content", "host": "test_host", "event": {"content":{"Agent is NOT installed":"2"}}})
# Agent Installation coverage informer
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_informer_table_settings", "host": "test_host", "event": {"title":"Agent Installation coverage", "col_order":["Agent Installation coverage"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_informer_table_content", "host": "test_host", "event": {"content":{"Agent Installation coverage":"67"}}})
# Agent Installation coverage dynamics
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_settings", "host": "test_host", "event": {"title":"Agent Installation coverage dynamics", "col_order":["Date", "Agent Installation coverage"]}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_content", "host": "test_host", "event": {"content":{"Date":"2020.01.03", "Agent Installation coverage":"35"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_content", "host": "test_host", "event": {"content":{"Date":"2020.01.04", "Agent Installation coverage":"45"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_content", "host": "test_host", "event": {"content":{"Date":"2020.01.05", "Agent Installation coverage":"60"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_content", "host": "test_host", "event": {"content":{"Date":"2020.01.06", "Agent Installation coverage":"65"}}})
events.append({"time": zbrunk_functions.get_ts("Current"), "event_type": "agent_installation_coverage_dynamics_table_content", "host": "test_host", "event": {"content":{"Date":"2020.01.07", "Agent Installation coverage":"67"}}})

collector_token = '8DEE8A67-7700-4BA7-8CBF-4B917CE23441'
print("Sending Table Events")
print("Results: " + str(zbrunk_functions.send_to_collector(server=server, events=events, collector_token=collector_token)))

