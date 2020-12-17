var hot = false
var temp = 60

if (temp>80) {
	console.log("Temp is greated than 80");
} else if (temp <= 80 && temp >= 50) {
	console.log("Temp is between 50 and 80");
} else if (temp < 50 && temp >=  32) {
	console.log("Temp is between 32 and 50");
} else {
	console.log("Temp is lower than 32");
}

console.log(hot)


var ham = 10;
var cheese = 10;

var report = "blank";

if (ham >= 10 && cheese >= 10) {
	report = "Strong sales of both"
} else if (ham === 0 && cheese === 0) {
	report = "Nothing Sold!"
} else {
	report = "We had some sales"
}

console.log(report);