// Create an object car
var carInfo = {make:"Toyota", year: 1995, model: "Camry"}

// Get value by key
console.log(carInfo["make"])
console.log(carInfo["year"])
console.log(carInfo["model"])

// Mixed object
var mixed = {a:true, b:[1,2,3], c:{letters:['a','b','c']}}

// Get values of mixed object
console.log(mixed["a"])
console.log(mixed["b"][1])
console.log(mixed["c"]["letters"][2])

// Change value of car object
carInfo['year'] = 2006
console.log(carInfo)

// Another way do display an object in console:
console.dir(carInfo)

// Iterating through an object
for (k in carInfo) {
	console.log(k)
	console.log(carInfo[k])
}
