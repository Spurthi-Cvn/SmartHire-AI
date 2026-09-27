// =====================================
// OFFER LETTER
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
// SET OFFER DATE
// =====================================

const today =
    new Date();

const formattedDate =
    today.toLocaleDateString(
        "en-IN",
        {
            day: "2-digit",
            month: "long",
            year: "numeric"
        }
    );

document.getElementById(
    "offerDate"
).innerText =
    formattedDate;


// =====================================
// GENERATE CANDIDATE ID
// =====================================

const generatedCandidateId =
    "SH-2026-" +
    String(candidateId).padStart(
        4,
        "0"
    );

document.getElementById(
    "candidateId"
).innerText =
    generatedCandidateId;


// =====================================
// GET CANDIDATE DETAILS
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
                "Unable to load candidate details."
            );

        }


        if (data.message) {

            alert(
                data.message
            );

            return;

        }


        document.getElementById(
            "candidateName"
        ).innerText =
            data.name;


        document.getElementById(
            "candidateGreeting"
        ).innerText =
            data.name;


        document.getElementById(
            "candidateEmail"
        ).innerText =
            data.email;


        document.getElementById(
            "acceptanceName"
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


// =====================================
// ACCEPT OFFER
// =====================================

function acceptOffer() {

    const confirmed =
        confirm(
            "Are you sure you want to accept this offer?"
        );


    if (!confirmed) {
        return;
    }


    localStorage.setItem(
        "offer_status",
        "accepted"
    );


    window.location.href =
        "offer-accepted.html";
}


// =====================================
// DECLINE OFFER
// =====================================

function declineOffer() {

    const confirmed =
        confirm(
            "Are you sure you want to decline this offer?"
        );


    if (!confirmed) {
        return;
    }


    alert(
        "You have declined the offer."
    );

}


// =====================================
// LOAD DATA
// =====================================

loadCandidate(); 