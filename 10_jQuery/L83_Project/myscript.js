// Define first player
var playerOne = prompt("Player One: Enter Your Name, you will be Blue")
var playerOneColor = 'rgb(0, 0, 255)'

// Define second player
var playerTwo = prompt("Player Two: Enter Your Name, you will be Red")
var playerTwoColor = 'rgb(255, 0, 0)'

// Initialize a game
var gameOn = true
var table = $('table tr')

function reportWin(rowNum,colNum) {
  console.log("You won starting at this row,col");
  console.log(rowNum);
  console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
	return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function reportColor(rowIndex, colIndex) {
	return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex) {
	var colorReturn = reportColor(5,colIndex);
	for(var row = 5; row > -1; row--) {
		colorReturn = reportColor(row,colIndex);
		if (colorReturn === 'rgb(128, 128, 128)'){
			return row
		}
	}
}

function colorMatchCheck(one, two, three, four) {
	return (one === two & one === three & one === four & one !== 'rgb(128, 128, 128)' & one !== undefined)
}

// Check for Horizontal Wins
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {
      if (colorMatchCheck(reportColor(row,col), reportColor(row,col+1) ,reportColor(row,col+2), reportColor(row,col+3))) {
        console.log('horiz');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Vertical Wins
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(reportColor(row,col), reportColor(row+1,col) ,reportColor(row+2,col), reportColor(row+3,col))) {
        console.log('vertical');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(reportColor(row,col), reportColor(row+1,col+1) ,reportColor(row+2,col+2), reportColor(row+3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else if (colorMatchCheck(reportColor(row,col), reportColor(row-1,col+1) ,reportColor(row-2,col+2), reportColor(row-3,col+3))) {
        console.log('diag');
        reportWin(row,col);
        return true;
      }else {
        continue;
      }
    }
  }
}

// Start with player One
var currentPlayer = 1;
var currentName = playerOne;
var currentColor = playerOneColor;

$('p').text(playerOne + " it is your turn, please pick a column to drop your blue chip.")

$('.board button').on('click', function(){
	// Pick a column
  	var column = $(this).closest("td").index();

	// Pick a row
	var bottomAvailable = checkBottom(column);

	changeColor(bottomAvailable, column, currentColor);

	// Check win or tie
	if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
		$('h1').text(currentName + " You have won!")
		$('h2').fadeOut('fast');
		$('p').fadeOut('fast');
	}

	// Switch the player
	currentPlayer = currentPlayer * -1

	if (currentPlayer === 1) {
		currentName = playerOne;
		$('p').text(currentName + " it is your turn, please pick a column to drop your blue chip.")
		currentColor = playerOneColor;
	} else {
		currentName = playerTwo;
		$('p').text(currentName + " it is your turn, please pick a column to drop your red chip.")
		currentColor = playerTwoColor;
	}
})










