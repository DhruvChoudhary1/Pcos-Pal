document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const showSignupLink = document.getElementById('showSignupLink');
    const showLoginLink = document.getElementById('showLoginLink');

    
    if (showSignupLink) {
        showSignupLink.addEventListener('click', (event) => {
            event.preventDefault(); 
            loginForm.style.display = 'none';
            signupForm.style.display = 'block'; 
        });
    }

    if (showLoginLink) {
        showLoginLink.addEventListener('click', (event) => {
            event.preventDefault(); 
            signupForm.style.display = 'none';
            loginForm.style.display = 'block'; 
        });
    }

    
    loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const email = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const res = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const result = await res.json();

        if (res.ok) {
            alert("Login successful!");
            // Save user ID in localStorage for prediction
            localStorage.setItem("user_id", result.user_id);
            window.location.href = "index.html";
        } else {
            alert("Login failed: " + result.error);
        }
    } catch (err) {
        alert("Error during login: " + err.message);
    }
    console.log("Logging in with:", email, password);


});


    
   signupForm.addEventListener('submit', async (event) => {
    event.preventDefault(); 

    const name = document.getElementById('newUsername').value;
    const email = document.getElementById('newEmail').value;
    const password = document.getElementById('newPassword').value;

    try {
        const res = await fetch("http://127.0.0.1:5000/signup", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, email, password })
        });

        const result = await res.json();

        if (res.ok) {
            alert("Sign up successful! Please login with your new account.");
            signupForm.style.display = 'none';
            loginForm.style.display = 'block';
            signupForm.reset();
        } else {
            alert("Signup failed: " + result.error);
        }
    } catch (err) {
        alert("Error during signup: " + err.message);
    }
});
});