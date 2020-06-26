// Timer App
function Countdown() {
    var seconds = document.getElementById("seconds").value;
    var stop;
    function tick() {
        seconds = seconds - 1;
        timer.innerHTML = seconds;
        stop = setTimeout(tick, 1000);
        
        if (seconds == -1) {
            alert("Time's Up!");
            clearTimeout(stop);
            document.getElementById("timer").innerHTML = "Time's Up!";
            }
    }
    tick();
}

// Slideshow
var slideIndex = 1;
showSlides(slideIndex);

// Next/Previous Controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail Image Controls
function currentSlides(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}