#!/usr/bin/env bash

echo -e '{"time":"1471613579", "host":"test_host", "event":{"test_key":"test_line1"}}\n{"time":"1471613580", "host":"test_host", "event":{"test_key":"test_line2"}}' > temp_data

curl -k https://127.0.0.1:8088/services/collector -H 'Authorization: Zbrunk 8DEE8A67-7700-4BA7-8CBF-4B917CE2352B' -d @temp_data
{"text":"Success","code":0}

