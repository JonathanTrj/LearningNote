var http = require("http");
var fs = require("fs");

var myServer = http.createServer((req, res) => {
	var url = req.url;
	console.log("request to: ", url);
	switch(url) {
		case "/": {
			var data = fs.readFileSync("./datafiles/index.html", 'utf8');
			res.write(data);
			break;
		}
		case "/page1": {
			res.write("<div align='center'><h2>Page1</h2></div>");
			break;
		}
		default: {
			res.write("<div align='center'><h2>Path Not Found!</h2></div>");
			break;
		}
	}
	res.end();
});

myServer.listen("8888", (err) => {
	if (err) {
		console.log(err);
		throw err;
	}
	console.log("Listening on port 8888");
})