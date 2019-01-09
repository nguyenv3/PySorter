
function filterAndSend() {
    var x = document.getElementById('raw_elements').value;
    var client = new XMLHttpRequest;
    client.open('POST', '/numbers', true);
    client.setRequestHeader('Content-Type', 'application/json')
    result = client.send(x);
    console.log(result);
    

}