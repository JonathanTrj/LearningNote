var http = require("http");
var url = require("url");
var util = require("util");

function start() {
	function onRequest(request, response) {
		var pathname = url.parse(request.url).pathname;
		var query = url.parse(request.url, true).query;
		var id = query.id;
		console.log("Request for " + pathname + " received.");
    	response.writeHead(200, {"Content-Type": "text/plain"});
    	response.write(util.inspect(url.parse(request.url, true)));
    	response.write(id);
    	response.end();
	}

	http.createServer(onRequest).listen(8888);
  	console.log("runing at http://127.0.0.1:8888");
}

exports.start = start;