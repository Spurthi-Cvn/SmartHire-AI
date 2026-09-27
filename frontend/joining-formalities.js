// =====================================
// JOINING FORMALITIES
// =====================================

const candidateId =
    localStorage.getItem("candidate_id");

// =====================================
// LOGIN CHECK
// =====================================

if (!candidateId) {

    alert("Candidate ID not found. Please login again.");

    window.location.href = "login.html";

}


// =====================================
// LOAD CANDIDATE DETAILS
// =====================================

async function loadCandidate() {

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/candidate/${candidateId}`
        );

        const data = await response.json();

        console.log("Candidate data:", data);


        if (!response.ok) {

            throw new Error(
                data.message || "Unable to load candidate."
            );

        }


        // ==============================
        // CANDIDATE NAME
        // ==============================

        const nameElement =
            document.getElementById("candidateName");

        if (nameElement) {

            nameElement.innerText =
                data.name;

        }


        // ==============================
        // CANDIDATE ID
        // ==============================

        const idElement =
            document.getElementById("candidateId");

        if (idElement) {

            idElement.innerText =
                "SH-2026-" +
                String(candidateId).padStart(4, "0");

        }


        console.log(
            "Candidate details loaded successfully."
        );

    }

    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

        const nameElement =
            document.getElementById("candidateName");

        const idElement =
            document.getElementById("candidateId");


        if (nameElement) {

            nameElement.innerText =
                "Unable to load";

        }

        if (idElement) {

            idElement.innerText =
                "Unable to load";

        }

    }

}


// =====================================
// COMPLETE JOINING FORMALITIES
// =====================================

function completeJoiningFormalities() {

    const confirmation =
        document.getElementById(
            "joiningConfirmation"
        );


    if (!confirmation.checked) {

        alert(
            "Please confirm that you are ready to complete the joining formalities."
        );

        return;

    }


    localStorage.setItem(
        "stage_onboarding",
        "completed"
    );


    localStorage.setItem(
        "joining_formalities",
        "completed"
    );


    alert(
        "Joining formalities completed successfully."
    );


    // Move to Joining Letter

    window.location.href =
        "joining-letter.html";

}


// =====================================
// INITIALIZE
// =====================================

loadCandidate();