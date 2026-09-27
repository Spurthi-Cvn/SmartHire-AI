// =====================================
// JOINING LETTER
// =====================================

const candidateId =
    localStorage.getItem("candidate_id");


// =====================================
// LOGIN CHECK
// =====================================

if (!candidateId) {

    alert("Please login first.");

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


        // Candidate Name

        document.getElementById(
            "candidateName"
        ).innerText =
            data.name;


        // Candidate ID

        document.getElementById(
            "candidateId"
        ).innerText =
            "SH-2026-" +
            String(candidateId)
                .padStart(4, "0");


        // Letter Date

        const today =
            new Date();

        document.getElementById(
            "letterDate"
        ).innerText =
            today.toLocaleDateString(
                "en-IN",
                {
                    day: "2-digit",
                    month: "long",
                    year: "numeric"
                }
            );

    }

    catch (error) {

        console.error(
            "Joining letter error:",
            error
        );

    }

}


// =====================================
// MARK JOINING COMPLETED
// =====================================

localStorage.setItem(
    "stage_onboarding",
    "completed"
);


// =====================================
// INITIALIZE
// =====================================

loadCandidate();