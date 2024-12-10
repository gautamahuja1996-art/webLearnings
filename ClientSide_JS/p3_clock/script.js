// using setInterval to update date and time continuously
setInterval( () => {

    // Getting the local date and time
    let new_dt = new Date();
    let d = new_dt.toLocaleDateString();
    let t = new_dt.toLocaleTimeString();

    // getting the date and time html elements
    date_element = document.getElementById('date');
    time_element = document.getElementById('time');

    // changing the innerHTML
    date_element.innerHTML = `Today's Date: ${d}`;
    time_element.innerHTML = `Current Time: ${t}`;
}
, 1000)
