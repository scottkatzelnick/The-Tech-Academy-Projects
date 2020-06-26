function conceptCar(model) {
  let conceptModel = model.getAttribute('data-concept-car');
  if (conceptModel === 'The 2021 Mustang Mach-E') {
    alert(
      `${conceptModel} is the newest concept car from Ford Motors! Visit https://www.ford.com/suvs/mach-e/2021/ to see it for yourself!`
    );
  } else if (conceptModel === 'The Bugatti Hypercar Concept') {
    alert(
      `${conceptModel} is the newest concept car from Bugatti! Visit https://www.motor1.com/news/177936/bugatti-futuristic-hypercar-rendering/ to see it for yourself!`
    );
  } else if (conceptModel === 'The Ferrari 612 GTO') {
    alert(
      `${conceptModel} is the newest concept car from Ferrari! Visit https://2018releasedateprice.com/2017-ferrari-612-gto-release-date-and-price/ to see it for yourself!`
    );
  } else if (conceptModel === 'The Terzo Millennio') {
    alert(
      `${conceptModel} is the newest concept car from Lamboghini! Visit https://www.lamborghini.com/en-en/models/concept/terzo-millennio to see it for yourself!`
    );
  } else {
    alert('Please click on a manufacturer from the list.');
  }
}
