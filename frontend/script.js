console.log("SmartHire AI script.js loaded");

// ================= API CONFIGURATION =================

const API_BASE_URL = "http://127.0.0.1:8000";


// ================= REGISTER =================

const form = document.getElementById("registerForm");

if (form) {

    console.log("Register page detected");

    const loading = document.getElementById("loading");
    const registerButton = form.querySelector('button[type="submit"]');

    form.addEventListener("submit", async function (e) {

        e.preventDefault();

        loading.style.display = "block";
        registerButton.disabled = true;

        const candidate = {
            name: document.getElementById("name").value.trim(),
            email: document.getElementById("email").value.trim(),
            phone: document.getElementById("phone").value.trim(),
            password: document.getElementById("password").value
        };

        try {

            const response = await fetch(`${API_BASE_URL}/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(candidate)
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(
                    data.detail || data.message || "Registration failed"
                );
            }

            alert(data.message || "Registration successful!");

            form.reset();

            window.location.href = "login.html";

        } catch (error) {

            console.error("Registration error:", error);

            alert("Registration Failed: " + error.message);

        } finally {

            loading.style.display = "none";
            registerButton.disabled = false;

        }

    });

}


// ================= LOGIN =================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    console.log("Login page detected");

    const loginLoading = document.getElementById("loginLoading");
    const loginButton = loginForm.querySelector('button[type="submit"]');

    loginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        loginLoading.style.display = "block";
        loginButton.disabled = true;

        const user = {
            email: document.getElementById("loginEmail").value.trim(),
            password: document.getElementById("loginPassword").value
        };

        try {

            const response = await fetch(`${API_BASE_URL}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user)
            });

            const data = await response.json();

            if (!response.ok || !data.candidate_id) {
                throw new Error(
                    data.detail || data.message || "Invalid login credentials"
                );
            }

            // Store candidate information
            localStorage.setItem("candidate_id", data.candidate_id);

            alert("Login successful!");

            window.location.href = "dashboard.html";

        } catch (error) {

            console.error("Login error:", error);

            alert("Login Failed: " + error.message);

        } finally {

            loginLoading.style.display = "none";
            loginButton.disabled = false;

        }

    });

}