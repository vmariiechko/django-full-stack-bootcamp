// Create a simple object with method inside of it
var simple = {
	sayHi: "Hello", 
	method: function(){
		console.log("The method was called")}
	}

console.log(["sayHi"])
console.log(simple.method)
simple.method()

// Create an object greeting with method that use a value of object
var myObj = {
	name: "Vadym",
	greet: function(){
		console.log("Hello " + this.name)
	}
}

console.log(myObj["name"])
console.log(myObj.greet)
myObj.greet()