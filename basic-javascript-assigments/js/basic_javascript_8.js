function FullSentence() {
    var sent1 = "This function ";
    var sent2 = "is an example of ";
    var sent3 = "how the concat() ";
    var sent4 = "function works."
    var sentence = sent1.concat(sent2, sent3, sent4);
    document.getElementById("sentence").innerHTML = sentence;
}

function Separate() {
    var str = "To be, or not to be, that is the question?";
    var short = str.slice(33, 41);
    document.getElementById("slice").innerHTML = short;
}

function NumberText() {
    var x = 10;
    var numStr = x.toString();
    document.getElementById("string").innerHTML = numStr;
}

function Precise() {
    var num = 123456789.123456789;
    document.getElementById("precise").innerHTML = num.toPrecision(11);
}

function Fixed() {
    var num1 = 123456789.123456789;
    document.getElementById("fixed").innerHTML = num1.toFixed();
}

function Value() {
    var num = 123456789.123456789;
    document.getElementById("value").innerHTML = num.valueOf();
}