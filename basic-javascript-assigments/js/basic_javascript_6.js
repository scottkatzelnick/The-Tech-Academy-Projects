function ride() {
  var height, canRide;
  height = document.getElementById("height").value;
  canRide = (height < 52) ? "You are too short":"You are tall enough";
  document.getElementById("ride").innerHTML = canRide + " to ride.";
}

function Dog(Name, Breed, Age, Weight) {
  this.dogName = Name;
  this.dogBreed = Breed;
  this.dogAge = Age;
  this.dogWeight = Weight;
}

var toby = new Dog("Toby", "Golden Retriever", 2, 90);

function GetDog() {
  document.getElementById("new-this").innerHTML = toby.dogName + " is a " + toby.dogBreed + ", weighing " + toby.dogWeight + " lbs. " + " and is " + toby.dogAge + " years old."
}

function Calculate() {
  document.getElementById("nested-function").innerHTML = Minus();
  function Minus() {
    var start = 10;
    function TakeOne() {
      start -= 1;
    }
    TakeOne();
    return start;
  }
}