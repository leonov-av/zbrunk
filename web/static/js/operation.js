function httpPost(theUrl, theValue)
{
    var xhr = new XMLHttpRequest();
    var url = theUrl;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var json = JSON.parse(xhr.responseText);
            console.log(json.email + ", " + json.password);
        }
    };
    var data = theValue;
    xhr.send(data);
}

var message = document.getElementById("operation_text");
var el = document.getElementById("executeButton");
if(el){
    el.addEventListener("click", function() {
        operation = message.value;
        alert(operation);
//        theUrl = window.location.href + "services/searcher";
//        httpPost(theUrl, operation);
    });
}