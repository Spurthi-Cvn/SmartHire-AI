// =====================================
// JOINING FORMALITIES
// =====================================

const candidateId = localStorage.getItem("candidate_id");

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

        if (!response.ok) {
            throw new Error("Unable to load candidate.");
        }

        // Candidate Name
        const nameElement =
            document.getElementById("candidateName");

        if (nameElement) {
            nameElement.innerText = data.name;
        }


        // Candidate ID
        const idElement =
            document.getElementById("candidateId");

        if (idElement) {
            idElement.innerText =
                "SH-2026-" +
                String(candidateId).padStart(4, "0");
        }

    } catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

        const nameElement =
            document.getElementById("candidateName");

        const idElement =
            document.getElementById("candidateId");

        if (nameElement) {
            nameElement.innerText = "Unable to load";
        }

        if (idElement) {
            idElement.innerText = "Unable to load";
        }
    }
}


// =====================================
// INITIALIZE JOINING BUTTON
// =====================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        // Find checkbox automatically
        // No need to depend on a specific checkbox ID

        const confirmationCheckbox =
            document.querySelector(
                'input[type="checkbox"]'
            );


        const completeBtn =
            document.getElementById(
                "completeJoiningBtn"
            );


        // CHECKBOX NOT FOUND
        if (!confirmationCheckbox) {

            alert(
                "Joining confirmation checkbox not found."
            );

            return;
        }


        // BUTTON NOT FOUND
        if (!completeBtn) {

            alert(
                "Complete Joining button not found."
            );

            return;
        }


        // =====================================
        // BUTTON STATE
        // =====================================

        function updateButton() {

            completeBtn.disabled =
                !confirmationCheckbox.checked;
        }


        updateButton();


        // =====================================
        // CHECKBOX CHANGE
        // =====================================

        confirmationCheckbox.addEventListener(
            "change",
            updateButton
        );


        // =====================================
        // COMPLETE JOINING
        // =====================================

        completeBtn.addEventListener(
            "click",
            function () {

                if (!confirmationCheckbox.checked) {

                    alert(
                        "Please confirm the joining declaration first."
                    );

                    return;
                }


                // Store completion
                localStorage.setItem(
                    "joining_formalities",
                    "completed"
                );

                localStorage.setItem(
                    "stage_onboarding",
                    "completed"
                );


                alert(
                    "Joining formalities completed successfully."
                );


                // Go to joining letter
                window.location.href =
                    "joining-letter.html";
            }
        );

    }
);


// =====================================
// INITIALIZE
// =====================================

loadCandidate();