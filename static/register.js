document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('register-form');
    const loginForm = document.getElementById('login-form');

    // Add form submission logic, validation, and authentication
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const username = registerForm.querySelector('input[name="username"]').value;
        const email = registerForm.querySelector('input[name="email"]').value;
        const password = registerForm.querySelector('input[name="password"]').value;
        const confirmPassword = registerForm.querySelector('input[name="confirmPassword"]').value;

        // Perform client-side validation
        if (!isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        if (password !== confirmPassword) {
            alert('Passwords do not match. Please try again.');
            return;
        }

        // Registration logic (replace with server-side code)
        // Here, you can send the registration data to your server for processing
        // After successful registration, you can redirect the user
        // For now, we'll just display an alert
        alert('Registration successful! You can now log in.');
        registerForm.reset();
    });

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const email = loginForm.querySelector('input[name="email"]').value;
        const password = loginForm.querySelector('input[name="password"]').value;

        // Perform client-side validation (you can add more checks)
        if (!isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Authentication logic (replace with server-side code)
        // Here, you can send the login data to your server for authentication
        // After successful login, you can redirect the user to their dashboard
        // For now, we'll just display an alert
        alert('Login successful! Redirecting to dashboard...');
        loginForm.reset();
    });

    // Function to validate email format
    function isValidEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});
// register.js

// Initialize Google Sign-In
gapi.load('auth2', function() {
    gapi.auth2.init({
        client_id: '160112374519-a963oshs8nfjk0ilecet0d42l8kubgig.apps.googleusercontent.com' // Replace with your Google OAuth client ID
    });
});

// Handle sign-in callback
function onGoogleSignIn(googleUser) {
    // Retrieve the user's Google profile information
    var profile = googleUser.getBasicProfile();
    var googleEmail = profile.getEmail();
    var googleIdToken = googleUser.getAuthResponse().id_token;

    // You can now use the 'googleEmail' and 'googleIdToken' for registration or login
    // Send these values to your server for verification and user creation
    // Example:
    // fetch('/google-login', {
    //     method: 'POST',
    //     body: JSON.stringify({ email: googleEmail, idToken: googleIdToken }),
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    // })
    // .then(response => response.json())
    // .then(data => {
    //     // Handle the server's response here
    //     console.log(data);
    // })
    // .catch(error => {
    //     console.error('Error:', error);
    // });
}

