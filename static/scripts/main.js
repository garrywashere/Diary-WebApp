function greeting(fname) {
    const date = new Date();
    let hour = date.getUTCHours();
    let state;
    if (hour >= 0 && hour <= 11){
        state = "Morning";
    } else if (hour >= 12 && hour <= 17){
        state = "Afternoon";
    } else if (hour >= 18 && hour <= 21){
        state = "Evening";
    } else if (hour >= 22 && hour <= 24){
        state = "Night";
    };
    document.getElementById("greetingText").innerHTML = `Good ${state}, ${fname}!`
}

function dnt(){
    const date = new Date();
    let timeString = date.toLocaleTimeString()
    let dateString = date.toLocaleDateString()
    document.getElementById("dntText").innerHTML = `${timeString} ${dateString}`
}

function chainStart(fname){
    window.setInterval(dnt, 1000);
    greeting(fname)
}