document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form'); // Get the first form on the page

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Determine whether it's a registration or login form
        const isRegistrationForm = form.classList.contains('registration-form');

        // Collect form data
        const formData = {
            email: form.querySelector('[name="email"]').value,
            password: form.querySelector('[name="password"]').value,
        };

        if (isRegistrationForm) {
            formData.username = form.querySelector('[name="username"]').value;
            formData.confirm = form.querySelector('[name="confirm"]').value;
        }

        // Determine the URL for the fetch request based on the form type
        const url = isRegistrationForm ? '/register' : '/login';

        // Send a POST request to your server with JSON data
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData),
        })
        .then(response => {
            if (response.status === 200) {
                // Registration or login was successful
                const successMessage = isRegistrationForm
                    ? 'Registration successful! You can now log in.'
                    : 'Login successful! Welcome back.';
                alert(successMessage);
                window.location.href = '/'; // Redirect to the home page or wherever you prefer
            } else {
                // Registration or login failed, show an error message
                const errorMessage = isRegistrationForm
                    ? 'Registration failed. Please try again.'
                    : 'Login failed. Please try again.';
                alert(errorMessage);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});

