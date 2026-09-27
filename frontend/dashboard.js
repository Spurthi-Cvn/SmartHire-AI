// =====================================
// DASHBOARD
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
// LOAD CANDIDATE PROFILE
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

        const nameElement =
            document.getElementById(
                "candidateName"
            );

        if (nameElement) {
            nameElement.innerText =
                data.name;
        }


        // Candidate Email

        const emailElement =
            document.getElementById(
                "candidateEmail"
            );

        if (emailElement) {
            emailElement.innerText =
                data.email;
        }


        // Candidate Phone

        const phoneElement =
            document.getElementById(
                "candidatePhone"
            );

        if (phoneElement) {
            phoneElement.innerText =
                data.phone;
        }

    }

    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );

    }

}



// =====================================
// RECRUITMENT STAGES
// =====================================

const stages = [

    "resume",
    "ats",
    "aptitude",
    "technical",
    "communication",
    "hr",
    "selection",
    "offer",
    "onboarding"

];



// =====================================
// CHECK COMPLETED STAGE
// =====================================

function isCompleted(stage) {

    return (
        localStorage.getItem(
            "stage_" + stage
        ) === "completed"
    );

}



// =====================================
// UPDATE RECRUITMENT PROGRESS
// =====================================

function updateRecruitmentProgress() {

    let completedCount = 0;


    stages.forEach(
        function(stage, index) {

            const row =
                document.getElementById(
                    "stage-" + stage
                );

            const button =
                document.getElementById(
                    stage + "Button"
                );


            if (!row || !button) {
                return;
            }


            // =================================
            // CHECK COMPLETION
            // =================================

            const completed =
                isCompleted(stage);


            if (completed) {

                completedCount++;


                row.classList.remove(
                    "locked"
                );

                row.classList.add(
                    "completed"
                );


                button.innerText =
                    "✓ Completed";

                button.style.background =
                    "#16a34a";


                button.onclick = null;

                return;

            }


            // =================================
            // CHECK PREVIOUS STAGE
            // =================================

            const previousStage =
                index > 0
                    ? stages[index - 1]
                    : null;


            const unlocked =
                index === 0 ||
                isCompleted(previousStage);


            // =================================
            // UNLOCK CURRENT STAGE
            // =================================

            if (unlocked) {

                row.classList.remove(
                    "locked"
                );


                button.innerText =
                    "Start";


                button.style.background =
                    "#3b82f6";


                button.onclick = null;

            }


            // =================================
            // LOCK FUTURE STAGE
            // =================================

            else {

                row.classList.add(
                    "locked"
                );


                button.innerText =
                    "🔒 Locked";


                button.style.background =
                    "#6b7280";


                button.onclick =
                    function(event) {

                        event.preventDefault();

                        alert(
                            "Please complete the previous recruitment stage first."
                        );

                    };

            }

        }
    );


    // =================================
    // CALCULATE PROGRESS
    // =================================

    const percentage =
        Math.round(
            (
                completedCount /
                stages.length
            ) * 100
        );


    // Progress Bar

    const progressBar =
        document.getElementById(
            "progressBar"
        );


    if (progressBar) {

        progressBar.style.width =
            percentage + "%";

    }


    // Progress Text

    const progressText =
        document.getElementById(
            "progressText"
        );


    if (progressText) {

        progressText.innerText =
            percentage + "%";

    }

}



// =====================================
// LOGOUT
// =====================================

function logout() {

    localStorage.removeItem(
        "candidate_id"
    );

    window.location.href =
        "login.html";

}



// =====================================
// INITIALIZE DASHBOARD
// =====================================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        loadCandidate();

        updateRecruitmentProgress();

    }
);