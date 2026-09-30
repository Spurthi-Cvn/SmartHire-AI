// =====================================
// OFFER ACCEPTED PAGE
// =====================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        // =====================================
        // GET CANDIDATE ID
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

            return;
        }


        console.log(
            "Candidate ID:",
            candidateId
        );


        // =====================================
        // GENERATE CANDIDATE ID
        // =====================================

        const generatedCandidateId =
            "SH-2026-" +
            String(candidateId).padStart(
                4,
                "0"
            );


        const candidateIdElement =
            document.getElementById(
                "candidateId"
            );


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
                    "Calling candidate API..."
                );


                const response =
                    await fetch(
                        "http://127.0.0.1:8000/candidate/" +
                        candidateId
                    );


                console.log(
                    "API status:",
                    response.status
                );


                if (!response.ok) {

                    throw new Error(
                        "API Error: " +
                        response.status
                    );

                }


                const data =
                    await response.json();


                console.log(
                    "Candidate data:",
                    data
                );


                // =====================================
                // CHECK API RESPONSE
                // =====================================

                if (
                    !data ||
                    !data.name
                ) {

                    throw new Error(
                        "Candidate name not found in API response."
                    );

                }


                // =====================================
                // DISPLAY NAME
                // =====================================

                const candidateName =
                    document.getElementById(
                        "candidateName"
                    );


                if (!candidateName) {

                    throw new Error(
                        "candidateName element not found in HTML."
                    );

                }


                candidateName.innerText =
                    data.name;


                console.log(
                    "Candidate name displayed:",
                    data.name
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


                if (candidateName) {

                    candidateName.innerText =
                        "Unable to load";

                }

            }

        }


        // =====================================
        // START
        // =====================================

        loadCandidate();

    }
);