# Zbrunk
Universal data analysis system.

Zbrunk project began almost like a joke. And in a way it is. 😜 In short, my friends and I (@leonov-av) decided to make an open-source (MIT license) tool, which will be a kind of alternative to Splunk for some specific tasks. So, it will be possible to:

* Put structured JSON events in Zbrunk using http collector API 
* Get the events from Zbrunk using http search API
* Make information panels based on these search requests and place them on dashboards

Why is it necessary? Well, I've worked a lot with Splunk in recent years. I like the main concepts, and I think working with the events is a very effective and natural way of processing and presenting data. But for my tasks (Asset Management, Compliance Management, Vulnerability Management) with several hundred megabytes of raw data per day to process and dashboards that need to be updated once or several times a day Splunk felt like an overkill. You really don't need such performance for these tasks. And, considering the price, it only makes sense if your organization already uses Splunk for other tasks. After Splunk decision to leave Russian market, this became even more obvious, so many people began to look for alternatives for possible and, as far as possible, painless migration. 

We are realistic, the performance and search capabilities of Zbrunk will be MUCH worse. It's impossible to make such universal and effective solution as a pet project without any resources. So, don't expect something that will process terabytes of logs in near real time, the goal is completely different. But if you want same basic tool to make dashboards, it worth a try. 🙂

Now, after first weekend of coding and planning it's possible to:

1) Send events to Zbrunk just like you do it using the Splunk HTTP Event Collector. Thus, it will be very easy to use your existing custom connectors if you already have some.
2) Search for events by type and time range.
3) Delete events by type and time range.

See the examples in "MANUAL -> Test cases"

The next step is to prepare dashboard data using the search requests and somehow show these dashboards, for example, in Grafana.

Stay tuned and welcome to participate. 😉
