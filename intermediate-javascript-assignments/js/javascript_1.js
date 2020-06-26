function favAnimal() {
  let animalOut;
  let animal = document.getElementById('fav-animal').value;
  switch (animal) {
    case 'Dog':
      animalOut = `A ${animal.toLowerCase()} is a man's best friend!`;
      break;
    case 'Cat':
      animalOut = `A ${animal.toLowerCase()} chooses us- we don't pick them.`;
      break;
    case 'Fish':
      animalOut = `Give a man a ${animal.toLowerCase()} and you feed him for a day; teach a man to ${animal.toLowerCase()} and you feed him for a lifetime.`;
      break;
    case 'Reptile':
      animalOut = `The man who never alters his opinions is like standing water , and breeds ${animal.toLowerCase()}s of the mind.`;
      break;
    case 'Pig':
      animalOut = `I am fond of ${animal.toLowerCase()}s. Dogs look up to us. Cats look down on us. ${animal}s treat us as equals.`;
      break;
    default:
      animalOut = 'Please write in an animal exactly as written from the list.';
  }
  document.getElementById('picked-animal').innerHTML = animalOut;
}

function testFunction() {
  let x = document.getElementsByClassName('test');
  x[1].innerHTML = 'To a much better sentence if I say so myself!';
}

let canvas = document.getElementById('myCanvas');
let ctx = canvas.getContext('2d');
ctx.beginPath();
ctx.arc(90, 50, 45, 0, 2 * Math.PI);
ctx.stroke();

let canvas2 = document.getElementById('myCanvas2');
let ctx2 = canvas2.getContext('2d');
let backgroundGradient = ctx2.createLinearGradient(0, 0, 0, 90);
backgroundGradient.addColorStop(0, 'white');
backgroundGradient.addColorStop(1, 'black');
ctx2.fillStyle = backgroundGradient;
ctx2.fillRect(0, 0, 180, 100);
