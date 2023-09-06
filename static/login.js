$(document).ready(function() {
  // Validate the login form before submitting it
  $("#login").submit(function(event) {
    var email = $("#email").val();
    var password = $("#password").val();

    // Check if email and password are empty
    if (email == "" || password == "") {
      alert("Please enter both email and password.");
      event.preventDefault(); // Prevent form submission
    }
  });
});

