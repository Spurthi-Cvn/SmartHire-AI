// =====================================
// JOINING LETTER
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


        if (!response.ok) {
            throw new Error("Unable to load candidate.");
        }


        // =====================================
        // CANDIDATE NAME
        // =====================================

        const candidateName =
            document.getElementById("candidateName");

        if (candidateName) {

            candidateName.innerText =
                data.name;
        }


        // =====================================
        // CANDIDATE ID
        // =====================================

        const candidateIdElement =
            document.getElementById("candidateId");

        if (candidateIdElement) {

            candidateIdElement.innerText =
                "SH-2026-" +
                String(candidateId).padStart(4, "0");
        }


        // =====================================
        // LETTER DATE
        // =====================================

        const letterDate =
            document.getElementById("letterDate");

        if (letterDate) {

            const today = new Date();

            letterDate.innerText =
                today.toLocaleDateString(
                    "en-IN",
                    {
                        day: "2-digit",
                        month: "long",
                        year: "numeric"
                    }
                );
        }

    }
    catch (error) {

        console.error(
            "Joining Letter Error:",
            error
        );

        const candidateName =
            document.getElementById("candidateName");

        const candidateIdElement =
            document.getElementById("candidateId");

        const letterDate =
            document.getElementById("letterDate");


        if (candidateName) {
            candidateName.innerText =
                "Unable to load";
        }

        if (candidateIdElement) {
            candidateIdElement.innerText =
                "Unable to load";
        }

        if (letterDate) {
            letterDate.innerText =
                "Unable to load";
        }
    }
}


// =====================================
// INITIALIZE
// =====================================

loadCandidate();