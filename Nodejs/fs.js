var fs = require("fs");

var data = {"name":"Jonathan", "age":25};

// write file sync
// var state = fs.writeFileSync("./datafiles/test.txt", JSON.stringify(data), 'utf8');
// if (state == undefined) {
// 	console.log("Success");
// } else {
// 	console.log("Error");
// }

// write file async
// fs.writeFile("./datafiles/test.txt", JSON.stringify(data), 'utf8', (err) => {
// 	console.log(err);
// })

// // write file sync "add"
// // if not exists, it will create a new file
// var data = new Date() + "\n";
// var state = fs.appendFileSync("./datafiles/logs.txt", data, 'utf8');
// if (state == undefined) {
// 	console.log("Success");
// } else {
// 	console.log("Error");
// }

// write file async "add"
// if not exists, it will create a new file
// var data = new Date() + "\n";
// fs.appendFile("./datafiles/logs.txt", data, 'utf8', (err) => {
// 	if (err) {
// 		console.log("Error");
// 		throw err;
// 	}
// 	console.log("Success");
// });

// read file sync
// var d = fs.readFileSync("./datafiles/test.txt", 'utf8');
// console.log(JSON.parse(d));

// read file async
// fs.readFile("./datafiles/test.txt", 'utf8', (err, d) => {
// 	if (err) {
// 		console.log(err);
// 		throw err;
// 	}
// 	console.log(JSON.parse(d));
// });

// file exists? sync
// if (fs.existsSync("./datafiles/test.txt")) {
// 	console.log("exists");
// } else {
// 	console.log("not exists");
// }

// file exists? async
// fs.exists("./datafiles/test.txt", (state) => {
// 	if (state) {
// 		console.log("exists");
// 	} else {
// 		console.log("not exists");
// 	}
// })

// listen file changes
// fs.watchFile("./datafiles/logs.txt", (a, b) => {
// 	console.log("log file changed");
// 	console.log("origin:", a);
// 	console.log("current:", b);
// })