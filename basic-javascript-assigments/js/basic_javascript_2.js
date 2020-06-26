function myFunction() {
  var str = "My favorite color is green.";
  var result = str.fontcolor("green");
  document.getElementById("greenText").innerHTML = result;
}

function concatenate() {
  var sentence = "Learning to us Javascript ";
  sentence += "is easy with The Tech Academy";
  document.getElementById("element").innerHTML = sentence;
}