var first = prompt("What's your first name?")
var second = prompt("What's your second name?")
var age = prompt("How old are you?")
var tall = prompt("What's your height in centimeters?")
var pet = prompt("What's the name of your pet?")

if (first[0] === second[0] && age > 20 && age < 30 && tall > 170 && pet[pet.length-1] === "y") {
	console.log("Welcome Comrade! You've passed the Spy Test")
} else {
	console.log("Sorry, there's nothing for you")
}