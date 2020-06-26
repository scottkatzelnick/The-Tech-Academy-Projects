function getReceipt() {
  let text1 = '<h3>You Ordered:</h3>';
  let runningTotal = 0;
  let sizeTotal = 0;
  let sizeArray = document.getElementsByClassName('size');
  for (var i = 0; i < sizeArray.length; i++) {
    if (sizeArray[i].checked) {
      var selectedSize = sizeArray[i].value;
      text1 = text1 + selectedSize + '<br>';
    }
  }
  if (selectedSize === 'Personal Pizza') {
    sizeTotal = 6;
  } else if (selectedSize === 'Medium Pizza') {
    sizeTotal = 8;
  } else if (selectedSize === 'Large Pizza') {
    sizeTotal = 10;
  } else if (selectedSize === 'Extra Large Pizza') {
    sizeTotal = 14;
  } else if (selectedSize == 'Sicilian Pizza') {
    sizeTotal = 16;
  }
  runningTotal = sizeTotal;
  console.log(selectedSize + ' = $' + sizeTotal + '.00');
  console.log('size text1: ' + text1);
  console.log('subtotal: $' + runningTotal + '.00');
  getToppings(runningTotal, text1);
}

function getToppings(runningTotal, text1) {
  var meatTotal = 0;
  var selectedMeat = [];
  var meatArray = document.getElementsByClassName('toppings');
  for (var j = 0; j < meatArray.length; j++) {
    if (meatArray[j].checked) {
      selectedMeat.push(meatArray[j].value);
      console.log('selected meat item: (' + meatArray[j].value + ')');
      text1 = text1 + meatArray[j].value + '<br>';
    }
  }
  var meatCount = selectedMeat.length;
  if (meatCount > 1) {
    meatTotal = meatCount - 1;
  } else {
    meatTotal = 0;
  }
  var vegTotal = 0;
  var selectedVeg = [];
  let vegArray = document.getElementsByClassName('veg');
  for (var h = 0; h < vegArray.length; h++) {
    if (vegArray[h].checked) {
      selectedVeg.push(vegArray[h].value);
      console.log('selected veg item: (' + vegArray[h].value + ')');
      text1 = text1 + vegArray[h].value + '<br>';
    }
  }
  var vegCount = selectedVeg.length;
  if (vegCount > 0) {
    vegTotal = vegCount;
  } else {
    vegTotal = 0;
  }
  runningTotal = runningTotal + vegTotal + meatTotal;
  console.log('total selected items: ' + (vegCount + meatCount));
  console.log(meatCount + ' meat - 1 free meat = ' + '$' + meatTotal + '.00');
  console.log('toppings text1: ' + text1);
  console.log('Purchase Total: ' + '$' + runningTotal + '.00');
  document.getElementById('showText').innerHTML = text1;
  document.getElementById('totalPrice').innerHTML =
    '<p>Total: <strong>$' + runningTotal + '.00' + '</strong></p>';
}
