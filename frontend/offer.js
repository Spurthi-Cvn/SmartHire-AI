// =====================================
// OFFER LETTER
// =====================================

document.addEventListener("DOMContentLoaded", function () {

    const candidateId =
        localStorage.getItem("candidate_id");

    // =====================================
    // CHECK LOGIN
    // =====================================

    if (!candidateId) {

        alert(
            "Candidate ID not found. Please login again."
        );

        window.location.href = "login.html";

        return;
    }


    console.log("Candidate ID:", candidateId);


    // =====================================
    // SET OFFER DATE
    // =====================================

    const today = new Date();

    const formattedDate =
        today.toLocaleDateString(
            "en-IN",
            {
                day: "2-digit",
                month: "long",
                year: "numeric"
            }
        );

    const offerDate =
        document.getElementById("offerDate");

    if (offerDate) {
        offerDate.innerText =
            formattedDate;
    }


    // =====================================
    // GENERATE CANDIDATE ID
    // =====================================

    const generatedCandidateId =
        "SH-2026-" +
        String(candidateId).padStart(4, "0");


    const candidateIdElement =
        document.getElementById("candidateId");

    if (candidateIdElement) {

        candidateIdElement.innerText =
            generatedCandidateId;

    }


    // =====================================
    // LOAD CANDIDATE DETAILS
    // =====================================

    async function loadCandidate() {

        try {

            console.log(
                "Fetching candidate details..."
            );


            const url =
                `http://127.0.0.1:8000/candidate/${candidateId}`;


            console.log(
                "API URL:",
                url
            );


            const response =
                await fetch(url);


            console.log(
                "API status:",
                response.status
            );


            if (!response.ok) {

                throw new Error(
                    `API returned status ${response.status}`
                );

            }


            const data =
                await response.json();


            console.log(
                "Candidate API response:",
                data
            );


            // =====================================
            // CHECK DATA
            // =====================================

            if (
                !data ||
                !data.name ||
                !data.email
            ) {

                throw new Error(
                    "Candidate name or email missing from API response."
                );

            }


            // =====================================
            // CANDIDATE NAME
            // =====================================

            const candidateName =
                document.getElementById(
                    "candidateName"
                );

            if (candidateName) {

                candidateName.innerText =
                    data.name;

            }


            // =====================================
            // GREETING NAME
            // =====================================

            const candidateGreeting =
                document.getElementById(
                    "candidateGreeting"
                );

            if (candidateGreeting) {

                candidateGreeting.innerText =
                    data.name;

            }


            // =====================================
            // EMAIL
            // =====================================

            const candidateEmail =
                document.getElementById(
                    "candidateEmail"
                );

            if (candidateEmail) {

                candidateEmail.innerText =
                    data.email;

            }


            // =====================================
            // ACCEPTANCE NAME
            // =====================================

            const acceptanceName =
                document.getElementById(
                    "acceptanceName"
                );

            if (acceptanceName) {

                acceptanceName.innerText =
                    data.name;

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


            const candidateName =
                document.getElementById(
                    "candidateName"
                );

            const candidateEmail =
                document.getElementById(
                    "candidateEmail"
                );


            if (candidateName) {

                candidateName.innerText =
                    "Unable to load";

            }


            if (candidateEmail) {

                candidateEmail.innerText =
                    "Unable to load";

            }

        }

    }


    // =====================================
    // ACCEPT OFFER
    // =====================================

    window.acceptOffer = function () {

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


        localStorage.setItem(
            "stage_offer",
            "completed"
        );


        window.location.href =
            "offer-accepted.html";

    };


    // =====================================
    // DECLINE OFFER
    // =====================================

    window.declineOffer = function () {

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

    };


    // =====================================
    // LOAD
    // =====================================

    loadCandidate();

});