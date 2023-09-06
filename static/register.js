$(document).ready(function() {
  // Validate the registration form before submitting it
  $("#register").submit(function(event) {
    var username = $("#username").val();
    var email = $("#email").val();
    var password = $("#password").val();
    var confirm_password = $("#confirm_password").val();

    // Check if any required field is empty
    if (username == "" || email == "" || password == "" || confirm_password == "") {
      alert("Please fill in all fields.");
      event.preventDefault(); // Prevent form submission
      return;
    }

    // Check if password and confirm password match
    if (password !== confirm_password) {
      alert("Passwords do not match.");
      event.preventDefault(); // Prevent form submission
    }
  });
});

