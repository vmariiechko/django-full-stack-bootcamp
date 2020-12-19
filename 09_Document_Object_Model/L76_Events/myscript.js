// Get all three elements by id
var doubleclick = document.querySelector("#dblclick")
var singleclick = document.querySelector("#click")
var hover = document.querySelector("#hover")

// Add event for double click
doubleclick.addEventListener("dblclick", function(){
	doubleclick.textContent = "DOUBLE CLICKED!"
	doubleclick.style.color = "cyan"
})

// Add event for click
singleclick.addEventListener("click", function(){
	singleclick.textContent = "CLICKED!"
	singleclick.style.color = "green"
})

// Add hover events
hover.addEventListener("mouseover", function(){
	hover.textContent = "HOVERED!"
	hover.style.color = "blue"
})

hover.addEventListener("mouseout", function(){
	hover.textContent = "HOVER ME!"
	hover.style.color = "black"
})
