function process_search_results(search_results){
    var i;
    var text;
    text = "<ol>"
    for (i = 0; i < search_results['results'].length; i++) {
      text += "<li><code class='json'>" + JSON.stringify(search_results['results'][i]) + "</code></li>";
    }
    text += "</ol>"
    return(text)
}

var app = new Vue({
  el: '#search',
  data: {
    operation_text: "",
    results: ''
  },
  methods: {
    search: function () {
      var search_api_url = 'https://127.0.0.1:8088/services/searcher';
      json = this.operation_text
      axios
        .post(search_api_url, json)
        .then(response => (this.results = process_search_results(response.data)));
      }
   }
});