// Whenever someone clicks (click event) any button, a callback function should be executed.
// we have to attach events to our buttons
// method 1--> Either get the button elements and then use the addEventListener(event, callback_func)
// method 2--> Use the onclick attribute of the HTML function

// method 1-->

/*
let add_button = document.getElementById('add_btn');
add_button.addEventListener('click', add_task);
*/

// method 2--> lets define all the functions
// defining add_task button

function add_task() {

    // step 1 --> update local storage
    update_localstorage();
}

// defining clear_list function
function clear_list() {

    // clearing the local storage and updating the table
    clear_localstorage();
    update_table();
}

// defining delete_task function
function delete_task(element_number) {
    // console.log('Deleting', element_number);

    // let's get the data from localStorage
    let current_data = get_data('items');

    // let's remove the element at the given index/element_number
    // splice arguments --> index of element to remove, number of elements to be removed
    current_data.splice(element_number, 1);

    // updating the localstorage and table
    set_data('items', current_data);
    update_table();

}

// function to update localStorage
function update_localstorage() {

    // getting elements to fetch text (val attribute is used to set/get text of input element)
    let t_element = document.getElementById('title');
    let d_element = document.getElementById('description');
    let title = t_element.value;
    let description = d_element.value;

    // clearing them
    t_element.value = '';
    d_element.value = '';

    // creating an object(key-value pairs) to store the data
    let obj = {title: title, description: description};

    // adding it to localstorage: first check if items key exists or not
    // empty array to hold data
    let data = [];
    if (get_data('items') == null) {

        // adding object to array
        data.push(obj);
    }
    else {

        // if items key is already there, we have to update the data. For that let's first fetch it and parse it so that we can process it as well
        data = get_data('items');

        // pushing in the new data
        data.push(obj);
    }

    // adding the array to localstorage in the form of JSON string (for easy processing when we parse it)
    set_data('items', data);

    // let's update the table now
    update_table();
}

// function to add the data from localstorage to the table
function update_table(){

    // getting the table body element
    let table_body = document.getElementById('table_body');

    // getting data from localstorage
    let current_data = get_data('items');
    
    // let's create an HTML string for all the elements of the current_data array: for each loop can give us both the JS object (key-value pair) and the index of that JS object in the current_data array.
    let html_str = '';

    // if clear button is pressed, it clears the localstorage first, then updates the table.
    if (current_data == null){
        html_str = '';
    }
    else{
        current_data.forEach((element, index) => {
            html_str += `
            <tr>
                <td>${index + 1}</td>
                <td>${element['title']}</td>
                <td>${element['description']}</td>
                <td><button class="btn btn-primary" onclick="delete_task(${index})">Delete</button></td>
            </tr>
            `;
        });
    
        // console.log(html_str);
    }

     // changing the html of the table_body
    table_body.innerHTML = html_str;
}

// function to get data from localstorage
function get_data(key){
    return JSON.parse(localStorage.getItem(key));
}

// function to set data in local storage
function set_data(key, data){
    localStorage.setItem(key, JSON.stringify(data))
}

// function to clear localstorage
function clear_localstorage(){
    localStorage.clear();
}

// let's update the table anyways in the start
update_table();