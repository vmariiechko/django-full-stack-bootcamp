// Create array with countries
var countries = ["USA", "Japan", "France"]

// Acsses to elements
console.log(countries[0])
console.log(countries[2])

// Re-assign element
console.log(countries[2] = "UK")

// Mutable array / Immutable string
var country1 = "India"

// console.log(country[2] = "s")

// Array with mixed datatypes
var mixed = [true, 10, "Arr"]

console.log(mixed[0])

// Array methods: 
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

// pop and push methods
var country2 = countries.pop()

countries.push("German")
console.log(countries)

// Create matrix (array inside of array)
var matrix = [[1,2,3],[4,5,6],[7,8,9]]

// Array iteration - two methods
for (var i = 0; i < matrix.length; i++){
	console.log(matrix[i])
}

for (i of matrix) {
	console.log(matrix[i])
}

// forEach method
matrix.forEach(console.log)