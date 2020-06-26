function add() {
  var addition = 10 + 8;
  document.getElementById("math").innerHTML = "10 + 8 = " + addition;
}

function sub() {
  var subtraction = 3 - 1;
  document.getElementById("math1").innerHTML = "3 - 1 = " + subtraction;
}

function mult() {
  var multiplication = 7 * 13;
  document.getElementById("math2").innerHTML = "7 * 13 = " + multiplication;
}

function div() {
  var divison = 48 / 16;
  document.getElementById("math3").innerHTML = "48 / 16 = " + divison;
}

function pemdas() {
  var orderOfOperations = 2 + (10 * 7 - 6) / (9 + 9 - 2);
  document.getElementById("math4").innerHTML = "2 + (10 * 7 - 6) / (9 + 9 - 2) = " + orderOfOperations + " (Can you break it down in your head?)";
}

function mod() {
  var modulus = 100 % 11;
  document.getElementById("math5").innerHTML = "The remainder when you divide 100 by 11 is " + modulus;
}

function neg() {
  var x = 1;
  document.getElementById("math6").innerHTML = "The opposite of " + x + " is " + -x;
}

function inc() {
  var y = 9;
  y++;
  document.getElementById("math7").innerHTML = "Using the increment operator 9 becomes " + y;
}

function dec() {
  var b = 10;
  b--;
  document.getElementById("math8").innerHTML = "Using the decrement operator 10 becomes " + b;
}

function ran() {
  window.alert("Your random number is " + Math.random() * 1000);
}

function mathObject() {
  window.alert("The base 10 representation of Pie is " + Math.PI)
}