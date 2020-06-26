function myTest() {
  document.getElementById("testNaN").innerHTML = 0 / 0;
}

function trueNaN() {
  document.getElementById("trueNaN").innerHTML = isNaN("Hello World");
}

function falseNaN() {
  document.getElementById("falseNaN").innerHTML = isNaN(1);
}

document.getElementById("positive").innerHTML = 1E400;

document.getElementById("negative").innerHTML = -1E400;

function trueNot() {
  document.getElementById("true").innerHTML = !(5 > 10);
}

function falseNot() {
  document.getElementById("false").innerHTML = !(5 < 10);
}

document.write(typeof 1 + "<br>" + "<br>");

document.write((1 < 2) + "<br>" + "<br>");

document.write((1 > 2) + "<br>" + "<br>");

document.write(("Dog" + 2E1) + "<br>" + "<br>");

document.write((1 + 2 == 3) + "<br>" + "<br>");

document.write((1 + 2 == 0) + "<br>" + "<br>");

x = 1
y = 1
document.write((x === y) + "<br>" + "<br>");

x1 = 1
y1 = "2"
document.write((x1 === y1) + "<br>" + "<br>");

x2 = 1
y2 = "1"
document.write((x2 === y2) + "<br>" + "<br>");

x3 = "Hello"
y3 = "World"
document.write((x3 === y3) + "<br>" + "<br>");

document.write((1 < 2 && 2 < 3) + "<br>" + "<br>");

document.write((1 > 3 && 2 < 3) + "<br>" + "<br>");

document.write((1 > 3 || 2 < 3) + "<br>" + "<br>");

document.write((1 > 3 || 2 > 3) + "<br>" + "<br>");

console.log(10 * 2);

console.log(1 > 2);