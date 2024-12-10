// displaying date
let current_date = new Date()
let d = current_date.toLocaleDateString()
let t = current_date.toLocaleTimeString()
console.log('Date: ', d)
console.log('Time: ', t)

// lets get the button with id click and change its CSS
// document.gebi + enter --> Abbreviation
let button = document.getElementById('click')
// console.log(button)
button.style.border = '5px solid red'

// lets target the class container. It will return a collection of all html elements with class container
// lets add another class to the first element as 'h1_container'
let collection = document.getElementsByClassName('container')
// console.log(collection)
collection[0].classList.add('h1_container')
collection[0].classList.add('white_text')

// getting the innerHTML of the element
console.log(collection[0].innerHTML)

// getting the inner Text(paragraph + heading content + Text on button)
console.log(collection[0].innerText)

// creating a new html element  using JS: A paragraph element
let new_element_1 = document.createElement('p')
let break_tag = document.createElement('br')
new_element_1.innerText = 'This is a newly created paragraph'

// let's add it to the second div container
// adding a break element first
collection[1].appendChild(break_tag)
collection[1].appendChild(new_element_1)

// let's create another element: A bold tag with text
let new_element_2 = document.createElement('b')
new_element_2.innerText = 'This is a new bold tag'

// let's replace this element from the previous element
// replaceChild(Element to be replaced by, Element to be replaced)
collection[1].replaceChild(new_element_2, new_element_1)

// using querySelector method: Helps to target elements using CSS selector.
elem = document.querySelector("div[class='container']")
console.log(elem)

// selecting all elements in DOM
// we will see only one element as in the other div, we added another class as h1_container, white_text
elem_all = document.querySelectorAll("div[class='container']")
console.log(elem_all)

// defining the clicked call back
// We can pass a parameter if needed.
function clicked(a){
    console.log(a)
}

// adding event listener to the div containers.
collection[0].addEventListener('click', function(){

    // let's change the button text to clicked
    document.getElementById('click').innerText = 'Click Me'
})

// adding event listener to the div containers.
collection[1].addEventListener('click', function(){

    // let's change the button text to clicked
    document.getElementById('click').innerText = 'Touch Me Not'
})

// arrow function-->
sum = (a, b) => {
    console.log(a+b)
}
console.log(sum(5,6)) // calling the function

// scheduling this function once
// id = setTimeout(() => {
//     console.log('Arrow function scheduled once')
// }, 5000);

// scheduing the function repeatedly
// id = setInterval( ()=>{
//     console.log('Hello')
// }   ,2000)

// Creating JS object: key-value pair
let js_obj = {name: 'Gautam', age: '24'}
console.log(js_obj, typeof js_obj)

// converting it to json string
let js_string = JSON.stringify(js_obj)
console.log(js_string, typeof js_string)

// converting the JS string, back to object
// parameter -> JSON string
let parsed = JSON.parse('{"name":"Gautam","age":"24"}')
console.log(parsed, typeof parsed)

// template literals
let age = 25
console.log(`The age: ${age}`)

