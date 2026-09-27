// =====================================
// EMPLOYEE ONBOARDING
// =====================================

const candidateId =
    localStorage.getItem("candidate_id");


// =====================================
// CHECK LOGIN
// =====================================

if (!candidateId) {

    alert(
        "Candidate ID not found. Please login again."
    );

    window.location.href =
        "login.html";

}


// =====================================
// DISPLAY CANDIDATE ID
// =====================================

document.getElementById(
    "candidateId"
).innerText =
    "SH-2026-" +
    String(candidateId).padStart(
        4,
        "0"
    );


// =====================================
// LOAD CANDIDATE
// =====================================

async function loadCandidate() {

    try {

        const response =
            await fetch(
                `http://127.0.0.1:8000/candidate/${candidateId}`
            );

        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                "Unable to load candidate."
            );

        }


        if (data.message) {

            alert(data.message);
            return;

        }


        document.getElementById(
            "candidateName"
        ).innerText =
            data.name;

    }
    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

        alert(
            "Unable to load candidate details."
        );

    }

}


loadCandidate();
localStorage.setItem(
    "stage_onboarding",
    "completed"
);