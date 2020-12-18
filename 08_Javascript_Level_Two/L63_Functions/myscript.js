// Hello world function
function hello() {
	console.log("Hello World!");
}

// Hello function with name as parameter
function helloName(name){
	console.log("Hello " + name);
}

// Sum function
function numAdd(num1, num2){
	console.log(num1+num2);
}

// Hello function with default parameter
function helloYou(name="John"){
	console.log("Hello " + name);
}

// Formal hello function with return statement
function formalHello(title="Sir", name="Jordan"){
	return title + " " + name
}

// Function which multiplies parameter by 5 and return it
function timesTen(num) {
	var result = num * 10;
	return result
}

// Scope (local and global). Create two global variables
var g = "Global G"
var thing = "Global THING"

// Create a function which prints one global and re-assigns variable with local scope with the same name as second global variable
function scope(thing){
	console.log(g);
	thing = "Local THING"
	console.log(thing)
}

scope()
console.log(thing)
