// Form Validation Function
function validateForm() {
  let noFName = document.forms['myForm']['fname'].value;
  let noLName = document.forms['myForm']['lname'].value;
  let noEmail = document.forms['myForm']['email'].value;
  let noPhone = document.forms['myForm']['phone'].value;
  if (noFName == '') {
    alert('You must enter your first name to proceed.');
    return false;
  } else if (noLName == '') {
    alert('You must enter your last name to proceed.');
    return false;
  } else if (noEmail == '') {
    alert('You must enter a valid email to proceed.');
    return false;
  } else if (noPhone == '') {
    alert('You must enter your phone number to proceed.');
    return false;
  } else {
    return true;
  }
}
