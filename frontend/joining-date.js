// =====================================
// JOINING DATE
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


        document.getElementById(
            "candidateName"
        ).innerText =
            data.name;


        document.getElementById(
            "candidateId"
        ).innerText =
            "SH-2026-" +
            String(candidateId)
                .padStart(4, "0");

    }

    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

    }

}


// =====================================
// CONTINUE
// =====================================

document
    .getElementById("continueBtn")
    .addEventListener(
        "click",
        function () {

            window.location.href =
                "joining-formalities.html";

        }
    );


// =====================================
// INITIALIZE
// =====================================

loadCandidate();