var x = 1;

function Add1() {
    document.write(1 + x + '<br>');
}
function Add2() {
    document.write(2 + x + '<br>');
}
function Add3() {
    var y = 2;
    document.write(3 + y + '<br>');
}
function Add4() {
    console.log(4 + y + '<br>');
}

Add1();
Add2();
Add3();
Add4();

function myDate() {
    if (new Date().getHours() >= 0) {
        document.getElementById("condition").innerHTML = "It is after 12pm, midnight.";
    }
}

function myStatement() {
    var x = 100;
    if (Math.random(150) < x) {
        document.getElementById("if-statement").innerHTML = "The number is less than 100"
    }
}

function Eligibility() {
    threshold = Math.round(document.getElementById("income").value);
    if (threshold < 99000) {
        qualify = "You are pre-qualified! The Economic Relief Payment will be sent to your bank's direct deposit information you provided within the next 1 million years. Congratulations!"
    } else {
        qualify = "Unfortunatley, you do not qualify."
    }
    document.getElementById("result").innerHTML = qualify;
}