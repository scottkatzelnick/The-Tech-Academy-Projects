function Test(Number) {
    this.testNumber = Number;
}

var true = new Test(1);
function myFunction() {
    document.getElementById("here").innerHTML = true.testNumber;
    console.log(myFunction);
}

// This constructor function is being called by an invalid variable.
// The keyword "true" like other keywords and lables
// are already "spoken for" by the javascript language itself. It will
// return nothing in the document and an error in the console.