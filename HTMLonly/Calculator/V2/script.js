const display = document.getElementById("display");

function appendToDisplay(value) {

    display.value += value;

}

function clearDisplay() {

    display.value = "";

}

function deleteDigit() {

    display.value = display.value.slice(0, -1);

}

function calculate() {

    try {

        display.value = eval(display.value);

    } catch (error) {

        display.value = "Error";

    }

}

