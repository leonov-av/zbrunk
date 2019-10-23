var app = new Vue({
  el: '#example-3',
  data: {
    operation_text: "",
    results: "n/a"
  },
  methods: {
    say: function (message) {
      var search_api_url = 'https://127.0.0.1:8088/services/searcher';
      //var json = '{"search": {"event_type": "test_event", "time":{"from":"1471613579","to":"1471613580"}}, "output_mode": "json", "max_count":"10000000", "auth_token":"8DEE8A67-7700-4BA7-8CBF-4B917CE23512"}';
      json = this.operation_text
      axios.post(search_api_url, json).then(function (response) {
        // handle success
        console.log(response);
        alert(JSON.stringify(response.data))
      });
    }
  }
})