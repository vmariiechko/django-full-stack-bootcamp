var x = 0;

while (x < 5) {
	console.log("x is currently: " + x);

	if (x===3) {
		console.log("X IS EQUEAL TO THREE!");
		break;
	}

	console.log("x is still less than 5, adding 1 to x");

	x = x+1
}


// Exercise solution:

var x = 1;

while (x < 11) {
	if (x%2 === 0){
		console.log("x = " + x)
	}
	x += 1;
}