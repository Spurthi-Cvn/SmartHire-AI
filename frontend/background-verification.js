// =====================================
// BACKGROUND VERIFICATION
// =====================================

const candidateId =
    localStorage.getItem("candidate_id");


// =====================================
// LOGIN CHECK
// =====================================

if (!candidateId) {

    alert(
        "Candidate ID not found. Please login again."
    );

    window.location.href =
        "login.html";
}


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

        document.getElementById(
            "candidateName"
        ).innerText =
            data.name;

        document.getElementById(
            "candidateId"
        ).innerText =
            "SH-2026-" +
            String(candidateId).padStart(
                4,
                "0"
            );

    }

    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

    }

}


// =====================================
// START VERIFICATION
// =====================================

function startVerification() {

    const consent =
        document.getElementById(
            "verificationConsent"
        );


    if (!consent.checked) {

        alert(
            "Please confirm the verification declaration before continuing."
        );

        return;

    }


    // =====================================
    // MARK BACKGROUND VERIFICATION COMPLETED
    // =====================================

    localStorage.setItem(
        "background_verification",
        "completed"
    );


    alert(
        "Background verification request submitted successfully."
    );


    // =====================================
    // NEXT STAGE
    // =====================================

    window.location.href =
        "joining-date.html";

}


// =====================================
// INITIALIZE
// =====================================

loadCandidate();