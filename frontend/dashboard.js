console.log("dashboard.js loaded");


document.addEventListener("DOMContentLoaded", async function () {


    // =========================
    // GET CANDIDATE ID
    // =========================

    const candidateId =
        localStorage.getItem("candidate_id");


    console.log(
        "Candidate ID:",
        candidateId
    );


    if (!candidateId) {

        alert(
            "Please login first."
        );

        window.location.href =
            "login.html";

        return;

    }



    // =========================
    // GET CANDIDATE DETAILS
    // =========================

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/candidate/${candidateId}`
        );


        console.log(
            "Candidate response:",
            response.status
        );


        if (!response.ok) {

            throw new Error(
                "Unable to load candidate details"
            );

        }


        const candidate =
            await response.json();


        console.log(
            "Candidate:",
            candidate
        );


        document.getElementById(
            "candidateName"
        ).textContent =
            candidate.name;


        document.getElementById(
            "candidateEmail"
        ).textContent =
            candidate.email;


        document.getElementById(
            "candidatePhone"
        ).textContent =
            candidate.phone;


    }

    catch (error) {

        console.error(
            "Candidate error:",
            error
        );

    }



    // =========================
    // GET RESUME
    // =========================

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/resume/${candidateId}`
        );


        console.log(
            "Resume response:",
            response.status
        );


        if (!response.ok) {

            throw new Error(
                "Unable to load resume"
            );

        }


        const resume =
            await response.json();


        console.log(
            "Resume:",
            resume
        );


        // =========================
        // NO RESUME
        // =========================

        if (!resume.resume_uploaded) {

            document.getElementById(
                "resumeNotUploaded"
            ).style.display = "block";


            document.getElementById(
                "resumeUploaded"
            ).style.display = "none";


            return;

        }



        // =========================
        // RESUME EXISTS
        // =========================

        document.getElementById(
            "resumeNotUploaded"
        ).style.display = "none";


        document.getElementById(
            "resumeUploaded"
        ).style.display = "block";



        // Filename

        document.getElementById(
            "resumeFilename"
        ).textContent =
            resume.filename;



        // Match percentage

        document.getElementById(
            "matchPercentage"
        ).textContent =
            resume.match_percentage + "%";



        // =========================
        // SKILLS
        // =========================

        const skillsList =
            document.getElementById(
                "skillsList"
            );


        skillsList.innerHTML = "";


        if (
            resume.skills &&
            resume.skills.length > 0
        ) {

            resume.skills.forEach(
                function (skill) {

                    const badge =
                        document.createElement("span");


                    badge.className =
                        "badge bg-primary me-2 mb-2";


                    badge.textContent =
                        skill;


                    skillsList.appendChild(
                        badge
                    );

                }
            );

        }

        else {

            skillsList.innerHTML =
                "<p>No skills detected.</p>";

        }


    }

    catch (error) {

        console.error(
            "Resume error:",
            error
        );

    }

});



// =========================
// LOGOUT
// =========================

function logout() {

    localStorage.removeItem(
        "candidate_id"
    );


    window.location.href =
        "login.html";

}