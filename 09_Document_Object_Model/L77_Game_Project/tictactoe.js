// Grab the cells
var cells = document.querySelectorAll("td")
console.log(cells)

// Restart Button
var restart = document.querySelector("#btn")

// Restart the Game
restart.addEventListener("click", function(){
	cells.forEach(td => td.textContent = "")
})

// Add event to all the cells:
function changeMarker(){
	if (this.textContent === ''){
		this.textContent = 'X';
	} else if (this.textContent === 'X'){
		this.textContent = 'O';
	} else {
		this.textContent = '';
	}
}

cells.forEach(th => th.addEventListener("click", changeMarker))