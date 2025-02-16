const usersDatabase = ["johnDoe", "parisa123", "alexUser"]; 

function checkLogin() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();  
    const errorMessage = document.getElementById("error-message");
    const signupButton = document.getElementById("signup-button");  

    if (!errorMessage) {
        console.error("ERROR: 'error-message' element not found in HTML.");
        return;
    }
    if (!signupButton) {
        console.error("ERROR: 'signup-button' element not found in HTML.");
        return;
    }

    errorMessage.style.display = "none";  
    signupButton.style.display = "none";  

    if (!username || !password) {
        errorMessage.textContent = "Please fill in both username and password.";
        errorMessage.style.display = "block"; 
        return;
    }

    if (!usersDatabase.includes(username)) {
        errorMessage.textContent = "Looks like you do not have an account! Click the Sign Up button to create one!";
        errorMessage.style.display = "block";  
        signupButton.style.display = "block";  
        return;
    } 

    alert("Login Successful!");
    window.location.href = "/account_connect"; 
}

function redirectToSignUp() {
    window.location.href = "/signup.html"; 
}