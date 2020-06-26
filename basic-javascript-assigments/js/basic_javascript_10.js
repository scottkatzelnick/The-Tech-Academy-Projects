function whileLoop() {
  var x = 1;
  var digit = '';
  while (x < 11) {
    digit += '<br>' + x;
    x++;
  }
  document.getElementById('loop').innerHTML = digit;
}

function arrayFunction() {
  let goodDog = [];
  goodDog[0] = 'sleepy';
  goodDog[1] = 'playful';
  goodDog[2] = 'hungry';
  goodDog[3] = 'cuddley';
  document.getElementById('array').innerHTML = `In this picture, the dog is ${goodDog[1]}.`;
}

function constFunction() {
  const student = {
    gpa    : 3.5,
    major  : 'Software Developer Course',
    school : 'The Tech Academy',
  };
  student.major = 'Rocking Software Development';
  student.computer = 'Macbook Pro 13"';
  document.getElementById(
    'constant'
  ).innerHTML = ` This object holds pertinent information for a student, like their GPA, which is ${student.gpa}. Their major is ${student.major} and the computer they're using to develop is the ${student.computer}.`;
}

function identifier() {
  let x = 42;
  document.getElementById('let').innerHTML = x;
}

function returnFunction() {
  function valueFunction() {
    return document.getElementById('name').value;
  }
  document.getElementById('return').innerHTML = `Hello ${valueFunction()}!`;
}

function loop() {
  let num = '';
  for (let i = 1; i <= 20; i++) {
    num += '<br>' + i * i;
  }
  document.getElementById('perfect-square').innerHTML = `${num}`;
}

let myDog = {
  name     : 'Toby',
  breed    : 'Golden Retriever',
  age      : 2,
  weight   : 99,
  activity : function() {
    return `My dog's name is ${this.name} and he is a ${this.breed}. He is ${this.age} years old and weighs ${this
      .weight} lbs.`;
  },
};
document.getElementById('dog').innerHTML = myDog.activity();

function myBreak() {
  let str = '';
  let i;
  for (i = 0; i <= 5; i++) {
    if (i === 4) {
      break;
    }
    str += `My number is ${i} <br>`;
  }
  document.getElementById('break').innerHTML = str;
}

function myContinue() {
  let str = '';
  let i;
  for (i = 0; i <= 10; i++) {
    if (i === 4) {
      continue;
    }
    str += `My number is ${i} <br>`;
  }
  document.getElementById('continue').innerHTML = str;
}
