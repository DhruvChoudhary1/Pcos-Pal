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

    
    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {
            event.preventDefault(); 
            const username = document.getElementById('username').value;
            

            
            console.log(`Login attempt with username: ${username}`);

            alert('Login successful! Redirecting to the main page...');
            window.location.href = 'index.html'; // Redirect to index.html
        });
    }

    
    if (signupForm) {
        signupForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent actual form submission
            const newUsername = document.getElementById('newUsername').value;
            
            
            console.log(`Signup attempt with username: ${newUsername}`);

            alert('Sign up successful! Please login with your new account.');
            
            
            signupForm.style.display = 'none';
            loginForm.style.display = 'block'; 
            
            
            signupForm.reset(); 
            
        });
    }
});