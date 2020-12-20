// Add event for h1 when clicked
$('h1').click(function(){
	console.log("h1 clicked!")
})

// Add event for li when clicked
$('li').click(function(){
	console.log("one of li was clicked!")
})

// Change h1 whenever its clicked
$('h1').click(function(){
	$(this).text("New text")
})

// Change class for h3 when key was pressed in text box 
$('input').eq(0).keypress(function(){
	$('h3').toggleClass('turnBlue')
})

// Same as previous for h2 but only when key Enter is pressed
$('input').eq(0).keypress(function(event){
	if (event.which === 13){
		$('h2').toggleClass('turnRed')
	}
})

// Add event for h1 when double clicked in another way
$('h1').on('dblclick', function(){
	$(this).toggleClass('turnBlue')
})

// Animation for container when submit button pressed
$('input').eq(-1).on('click', function(){
	$('.container').slideUp()
})