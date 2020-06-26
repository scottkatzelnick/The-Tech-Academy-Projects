function Vehicle(Make, Model, Year, Color) {
    this.vehicleMake = Make;
    this.vehicleModel = Model;
    this.vehicleYear = Year;
    this.vehicleColor = Color;
}

var scott = new Vehicle("Nissan", "Altima", 2017, "darkblue");
var amber = new Vehicle("Ford", "Escape", 2019, "white");

function myFunction1() {
    document.getElementById("scott-car").innerHTML = "Scott drives a " + scott.vehicleColor + "-colored, " + scott.vehicleMake + " " + scott.vehicleModel + " manufactured in " + scott.vehicleYear + "."; 
}

function myFunction2() {
    document.getElementById("amber-car").innerHTML = "Amber drives a " + amber.vehicleColor + "-colored, " + amber.vehicleMake + " " + amber.vehicleModel + " manufactured in " + amber.vehicleYear + ".";
}