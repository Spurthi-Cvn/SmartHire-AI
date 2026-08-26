console.log("script.js loaded");

// ================= REGISTER =================

const form = document.getElementById("registerForm");

if (form) {

    console.log("Register page detected");

    const loading = document.getElementById("loading");

    const nameInput = document.getElementById("name");
    const emailInput = document.getElementById("email");
    const phoneInput = document.getElementById("phone");
    const passwordInput = document.getElementById("password");

    form.addEventListener("submit", async function (e) {

        e.preventDefault();

        console.log("Register button clicked");

        loading.style.display = "block";

        const candidate = {
            name: nameInput.value,
            email: emailInput.value,
            phone: phoneInput.value,
            password: passwordInput.value
        };

        console.log(candidate);

        try {

            const response = await fetch("http://127.0.0.1:8000/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(candidate)
            });

            console.log("Response Status:", response.status);

            const data = await response.json();

            console.log(data);

            loading.style.display = "none";

            alert(data.message);

            form.reset();

            window.location.href = "login.html";

        } catch (error) {

            loading.style.display = "none";

            console.error(error);

            alert("Registration Failed: " + error.message);

        }

    });

}


// ================= LOGIN =================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    console.log("Login page detected");

    const loginLoading = document.getElementById("loginLoading");

    loginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        console.log("Login button clicked");

        loginLoading.style.display = "block";

        const user = {
            email: document.getElementById("loginEmail").value,
            password: document.getElementById("loginPassword").value
        };

        console.log(user);

        try {

            const response = await fetch("http://127.0.0.1:8000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(user)
            });

            console.log("Response Status:", response.status);

            const data = await response.json();

            console.log(data);

            loginLoading.style.display = "none";

            alert(data.message);

            if (data.candidate_id) {

                localStorage.setItem("candidate_id", data.candidate_id);

                window.location.href = "dashboard.html";

            }

        } catch (error) {

            loginLoading.style.display = "none";

            console.error(error);

            alert("Login Failed: " + error.message);

        }

    });

}