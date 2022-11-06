function today() {
    document.getElementById("date").valueAsDate = new Date();
};

function validate() {
    let title = document.getElementById("title");
    let password = document.getElementById("password");
    let body = document.getElementById("body");

    let clearButton = document.getElementById("clearButton");
    let saveButton = document.getElementById("saveButton");

    if (body.value.trim() != "") {
        clearButton.removeAttribute("disabled");
    } else {
        clearButton.setAttribute("disabled", "");
    };

    if (title.value.trim() != "" && password.value.trim() != "" && body.value.trim() != "") {
        saveButton.removeAttribute("disabled");
    } else {
        saveButton.setAttribute("disabled", "");
    };

    let count = document.getElementById("count");
    count.innerHTML = body.value.length + "/1000000";

    if (body.value.length === 1000000) {
        count.style.color = "red";
    } else if (body.value.length >= 750000) {
        count.style.color = "orange";
    } else if (body.value.length < 750000) {
        count.style.color = "rgb(200, 200, 200)";
    };
};

function cancel() {
    document.getElementById("body").value = "";
    document.getElementById("clearButton").value = "Cleared";
};