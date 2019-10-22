var app = new Vue({
  el: '#example-3',
  data: {
    operation_text: ""
  },
  methods: {
    say: function (message) {
      alert(this.operation_text)
    }
  }
})