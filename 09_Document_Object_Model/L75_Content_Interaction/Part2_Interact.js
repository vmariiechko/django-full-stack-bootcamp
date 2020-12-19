// Get paragraph and change its content:
var p = document.querySelector('p')

console.log(p.textContent)

p.textContent = "Content was changed"

// Change its html

console.log(p.innerHTML)

p.innerHTML = "Second changing of the <strong>content</strong>"

// Get special element:
var special = document.querySelector("#special")

var specialA = special. querySelector("a")

// Get attribute of <a> tag:
console.log(specialA.getAttribute("href"))

// Change link attribute:
console.log(specialA.setAttribute("href", "https://www.google.com"))
