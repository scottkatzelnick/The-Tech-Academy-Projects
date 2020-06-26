function myDictionary() {
  var customer = {
    FirstName: "Scott",
    LastName: "Katzelnick",
    Phone: "(732)900-1932",
    Email: "scottkatzelnick@mac.com",
    Id: "09231986"
  };
  delete customer.Phone;
  document.getElementById("dictionary").innerHTML = customer.Phone;
}