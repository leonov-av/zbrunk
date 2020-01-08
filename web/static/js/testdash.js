function get_table(settings_data, content_data){

    //alert(JSON.stringify(settings_data))
    //alert(JSON.stringify(content_data))

    var title = settings_data['results'][0]['event']['title']
    var col_order = settings_data['results'][0]['event']['col_order']
    var lines = content_data['results']

    var i;
    var header="";
    for (i = 0; i < col_order.length; i++) {
      header += "<th>" + col_order[i] + "</th>";
    }
    header = "<tr>" + header + "</tr>";

    var j;
    var content="";
    for (j = 0; j < lines.length; j++) {
      //alert(JSON.stringify(lines[j]['event']['content']))
      content += "<tr>"
      for (i = 0; i < col_order.length; i++) {
        if ( col_order[i] in lines[j]['event']['content']){
            content += "<td>" + lines[j]['event']['content'][ col_order[i]] + "</td>";
        }
        else {
            content += "<td>" + "</td>";
        }
      }
      content += "</tr>"
    }

    var all_results_count = content_data['all_results_count']

    text = "<i>" + title  + "</i>" + "<table>" + header + content + "</table>" + "All results: " + all_results_count;

    /*var i;
    var text;
    text = "<i>" + search_results['results_count'] + " of " + search_results['all_results_count'] + "</i>"
    text += "<ol>"
    for (i = 0; i < search_results['results'].length; i++) {
      text += "<li><code class='json'>" + JSON.stringify(search_results['results'][i]) + "</code></li>";
    }
    text += "</ol>"*/
    return(text)
}

function getTableSettings(from,to,table_id){
    var search_api_url = 'https://127.0.0.1:8088/services/searcher';
    auth_token = "8DEE8A67-7700-4BA7-8CBF-4B917CE23512";
        json_settings = {"search":
        {
            "event_type": table_id + "_settings",
            "time": {"from": from, "to": to}
        },
        "output_mode": "json",
        "max_count": "1",
        "skip": "0",
        "auth_token": auth_token,
    };

    return(axios.post(search_api_url, json_settings))
}

function getTableContent(from,to,table_id){
    var search_api_url = 'https://127.0.0.1:8088/services/searcher';
    json_content = {"search":
        {
            "event_type": table_id + "_content",
            "time": {"from": from, "to": to}
        },
        "output_mode": "json",
        "max_count": "10",
        "skip": "0",
        "auth_token": auth_token,
    };

    return(axios.post(search_api_url, json_content))
}

var table_id = "agent_installation_table"
var app = new Vue({
  el: '#' + table_id,
  methods: {
    search: function () {
        var start = new Date();
        start.setHours(0,0,0,0);
        var end = new Date();
        end.setHours(23,59,59,000);
        var from = (start.getTime()/1000).toString()
        var to = (end.getTime()/1000).toString()
        Promise.all([getTableSettings(from,to,table_id), getTableContent(from,to,table_id)])
          .then(function ([settings, content]) {
              document.getElementById(table_id).innerHTML = get_table(settings.data, content.data);
          });
    }
  },
  created: function(){
    this.search()
  }
});

var table_id2 = "agent_installed_informer_table"
var app = new Vue({
  el: '#' + table_id2,
  methods: {
    search: function () {
        var start = new Date();
        start.setHours(0,0,0,0);
        var end = new Date();
        end.setHours(23,59,59,000);
        var from = (start.getTime()/1000).toString()
        var to = (end.getTime()/1000).toString()
        Promise.all([getTableSettings(from,to,table_id2), getTableContent(from,to,table_id2)])
          .then(function ([settings, content]) {
              document.getElementById(table_id2).innerHTML = get_table(settings.data, content.data);
          });
    }
  },
  created: function(){
    this.search()
  }
});

var table_id3 = "agent_not_installed_informer_table"
var app = new Vue({
  el: '#' + table_id3,
  methods: {
    search: function () {
        var start = new Date();
        start.setHours(0,0,0,0);
        var end = new Date();
        end.setHours(23,59,59,000);
        var from = (start.getTime()/1000).toString()
        var to = (end.getTime()/1000).toString()
        Promise.all([getTableSettings(from,to,table_id3), getTableContent(from,to,table_id3)])
          .then(function ([settings, content]) {
              document.getElementById(table_id3).innerHTML = get_table(settings.data, content.data);
          });
    }
  },
  created: function(){
    this.search()
  }
});


var table_id4 = "agent_installation_coverage_informer_table"
var app = new Vue({
  el: '#' + table_id4,
  methods: {
    search: function () {
        var start = new Date();
        start.setHours(0,0,0,0);
        var end = new Date();
        end.setHours(23,59,59,000);
        var from = (start.getTime()/1000).toString()
        var to = (end.getTime()/1000).toString()
        Promise.all([getTableSettings(from,to,table_id4), getTableContent(from,to,table_id4)])
          .then(function ([settings, content]) {
              document.getElementById(table_id4).innerHTML = get_table(settings.data, content.data);
          });
    }
  },
  created: function(){
    this.search()
  }
});

var table_id5 = "agent_installation_coverage_dynamics_table"
var app = new Vue({
  el: '#' + table_id5,
  methods: {
    search: function () {
        var start = new Date();
        start.setHours(0,0,0,0);
        var end = new Date();
        end.setHours(23,59,59,000);
        var from = (start.getTime()/1000).toString()
        var to = (end.getTime()/1000).toString()
        Promise.all([getTableSettings(from,to,table_id5), getTableContent(from,to,table_id5)])
          .then(function ([settings, content]) {
              document.getElementById(table_id5).innerHTML = get_table(settings.data, content.data);
          });
    }
  },
  created: function(){
    this.search()
  }
});



