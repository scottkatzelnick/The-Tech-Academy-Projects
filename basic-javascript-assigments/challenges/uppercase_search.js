function Uppercase() {
    var str1 = "This sentence needs to be Uppercase.";
    var upString = str1.toUpperCase();
    document.getElementById("new-case").innerHTML = upString;
}

function Lowercase() {
    var str2 = "This sentence needs to be Lowercase.";
    var lowString = str2.toLowerCase();
    document.getElementById("new-case").innerHTML = lowString;
}

function Find() {
    var str3 = "Please locate where \"School\" starts.";
    var locate = str3.search("School");
    document.getElementById("search").innerHTML = locate;
}