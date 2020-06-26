function displayTime() {
  let militaryTime = new Date().getHours();
  let time = (new Date().getHours() + 24) % 12;
  let minutes = new Date().getMinutes();
  let reply;

  if (militaryTime < 12 == militaryTime >= 0) {
    reply = ' in the morning!';
  } else if (militaryTime >= 12 == militaryTime < 16) {
    reply = ' in the afternoon !';
  } else if (militaryTime >= 16 == militaryTime < 20) {
    reply = ' in the evening!';
  } else {
    reply = ' at night!';
  }

  if (militaryTime < 12) {
    var timeOfDay = 'am';
  } else {
    var timeOfDay = 'pm';
  }

  document.getElementById(
    'time'
  ).innerHTML = `It's ${time}:${minutes} ${timeOfDay}${reply}!`;
}
