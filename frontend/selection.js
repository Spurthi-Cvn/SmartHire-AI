// =====================================
// SELECTION STATUS
// =====================================

const candidateId =
    localStorage.getItem("candidate_id");

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
            "candidateEmail"
        ).innerText =
            data.email;

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

        console.error(error);

        alert(
            "Unable to load candidate details."
        );

    }

}

loadCandidate();
loadCandidate();


// =====================================
// MARK SELECTION STAGE AS COMPLETED
// =====================================

if (
    localStorage.getItem("stage_hr") === "completed"
) {

    localStorage.setItem(
        "stage_selection",
        "completed"
    );

}