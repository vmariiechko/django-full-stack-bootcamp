console.log($)

// Grab all h1 and li tags
console.log($('h1'))
console.log($('li'))

// Change css properties for h1:
var h1tag = $('h1')
h1tag.css('color', 'cyan')
h1tag.css('background', 'black')

// Change css properties for h1 using object
var h2tag = $('h2')
var styleCSS = {
	'color': 'blue',
	'background': 'green',
	'border': '5px solid orange'
}
h2tag.css(styleCSS)

// Grab li tags and change their css properties differently
var listItems = $('li')
listItems.css('color', 'green')
listItems.eq(0).css('color', 'pink')
listItems.eq(-1).css('color', 'purple')

// Change text for h1
console.log(h1tag.text())
h1tag.text("Text was changed")

// Change html for h1
console.log(h1tag.html())
h1tag.html('<em><strong>Another change of text</strong></em>')

// Change attribute for submit button
$('input').eq(-1).attr('type', 'radio')

// Change value for text input
$('input').eq(0).val("New text") 

// Add and remove class for h3
$('h3').addClass('turnBlue')
$('h3').removeClass('turnBlue')

// Toggle class twice for first paragraph
$('p').eq(0).toggleClass('turnRed')
$('p').eq(0).toggleClass('turnRed')