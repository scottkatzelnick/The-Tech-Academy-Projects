// Smooth scrolling to all links
$(document).ready(function() {
  $('a').on('click', function(event) {
    if (this.link !== '') {
      event.preventDefault();
      var link = this.link;
      $('html, body').animate(
        {
          scrollTop : $(link).offset().top,
        },
        2000,
        function() {
          window.location.link = link;
        }
      );
    }
  });
});

function openForm() {
  document.getElementById('myForm').style.display = 'block';
}

function closeForm() {
  document.getElementById('myForm').style.display = 'none';
  this.Close();
}
