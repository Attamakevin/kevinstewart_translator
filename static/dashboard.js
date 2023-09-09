// dashboard.js

// Simulate user data
const userData = {
    username: "JohnDoe",
    email: "johndoe@example.com",
};

// Function to update user information in the dashboard
function updateUserInformation() {
    const usernameElement = document.getElementById("username");
    const emailElement = document.getElementById("email");

    usernameElement.textContent = userData.username;
    emailElement.textContent = `Email: ${userData.email}`;
}

// Function to handle navigation
function handleNavigation() {
    const homeLink = document.getElementById("home-link");
    const messagesLink = document.getElementById("messages-link");
    const notificationsLink = document.getElementById("notifications-link");

    homeLink.addEventListener("click", () => {
        // Handle home link click, e.g., show home content
        document.querySelector(".content").innerHTML = "<h3>Welcome to Your Dashboard</h3><p>This is the home page content.</p>";
    });

    messagesLink.addEventListener("click", () => {
        // Handle messages link click, e.g., show messages content
        document.querySelector(".content").innerHTML = "<h3>Messages</h3><p>You have 3 new messages.</p>";
    });

    notificationsLink.addEventListener("click", () => {
        // Handle notifications link click, e.g., show notifications content
        document.querySelector(".content").innerHTML = "<h3>Notifications</h3><p>You have 5 new notifications.</p>";
    });
}

// Initialize the dashboard
function initDashboard() {
    updateUserInformation();
    handleNavigation();
}

// Call the initialization function when the document is loaded
document.addEventListener("DOMContentLoaded", initDashboard);

