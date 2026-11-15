// =====================================
// DASHBOARD CONFIGURATION
// =====================================

const API_BASE_URL = "http://127.0.0.1:8000";

const candidateId = localStorage.getItem("candidate_id");

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
// LOGIN CHECK
// =====================================

if (!candidateId) {
    alert("Please login first.");
    window.location.href = "login.html";
}


// =====================================
// LOAD CANDIDATE PROFILE
// =====================================
async function loadCandidate() {

    try {

        const response = await fetch(
            `${API_BASE_URL}/candidate/${candidateId}`
        );

        if (!response.ok) {
            throw new Error("Unable to load candidate.");
        }

        const data = await response.json();

        const nameElement = document.getElementById("candidateName");
        const emailElement = document.getElementById("candidateEmail");
        const phoneElement = document.getElementById("candidatePhone");

        if (nameElement) {
            nameElement.innerText = data.name;
        }

        if (emailElement) {
            emailElement.innerText = data.email;
        }

        if (phoneElement) {
            phoneElement.innerText = data.phone;
        }

        console.log("Candidate profile loaded:", data);

    }

    catch (error) {

        console.error("Candidate loading error:", error);

    }
}


// =====================================
// CHECK WHETHER A STAGE IS COMPLETED
// =====================================

function isCompleted(status) {

    const completedStatuses = [
        "completed",
        "passed",
        "shortlisted",
        "selected",
        "offered",
        "joined"
    ];

    return completedStatuses.includes(
        String(status).toLowerCase()
    );
}


// =====================================
// LOAD RECRUITMENT PROGRESS FROM DATABASE
// =====================================

async function loadRecruitmentProgress() {

    try {

        const response = await fetch(
            `${API_BASE_URL}/candidate/${candidateId}/progress`
        );

        if (!response.ok) {
            throw new Error("Unable to load recruitment progress.");
        }

        const data = await response.json();

        console.log("Recruitment Progress:", data);

        updateRecruitmentProgress(data);

    }

    catch (error) {

        console.error("Progress loading error:", error);

        alert("Unable to load recruitment progress. Please try again.");

    }
}


// =====================================
// UPDATE DASHBOARD STAGES
// =====================================

function updateRecruitmentProgress(data) {

    const statusMap = {
        resume: data.current_stage !== "resume" ? "Completed" : "Unlocked",
        ats: data.ats_status,
        aptitude: data.aptitude_status,
        technical: data.technical_status,
        communication: data.communication_status,
        hr: data.hr_status,
        selection: data.selection_status,
        offer: data.offer_status,
        onboarding: data.onboarding_status
    };

    let completedCount = 0;

    const currentStageIndex = stages.indexOf(data.current_stage);

    stages.forEach(function(stage, index) {

        const row = document.getElementById("stage-" + stage);

        const button = document.getElementById(stage + "Button");

        if (!row || !button) {
            return;
        }

        const status = statusMap[stage];

        const completed = isCompleted(status);

        const unlocked =
            completed ||
            stage === data.current_stage ||
            (index === 0 && data.current_stage === "resume");

        row.classList.remove("locked", "completed");

        // =================================
        // COMPLETED STAGE
        // =================================

        if (completed) {

            completedCount++;

            row.classList.add("completed");

            button.innerText = "✓ Completed";
            button.style.background = "#16a34a";
            button.disabled = true;

            return;
        }

        // =================================
        // UNLOCKED STAGE
        // =================================

        if (unlocked) {

            row.classList.remove("locked");

            button.innerText = "Start";
            button.style.background = "#3b82f6";
            button.disabled = false;

            return;
        }

        // =================================
        // LOCKED STAGE
        // =================================

        row.classList.add("locked");

        button.innerText = "🔒 Locked";
        button.style.background = "#6b7280";

        button.onclick = function(event) {

            event.preventDefault();

            alert(
                "Please complete the previous recruitment stage first."
            );

        };

    });


    // =================================
    // CALCULATE PROGRESS
    // =================================

    const percentage = Math.round(
        (completedCount / stages.length) * 100
    );

    const progressBar = document.getElementById("progressBar");

    if (progressBar) {
        progressBar.style.width = percentage + "%";
    }

    const progressText = document.getElementById("progressText");

    if (progressText) {
        progressText.innerText = percentage + "%";
    }

}


// =====================================
// LOGOUT
// =====================================

function logout() {

    localStorage.removeItem("candidate_id");

    window.location.href = "login.html";

}


// =====================================
// INITIALIZE DASHBOARD
// =====================================

document.addEventListener("DOMContentLoaded", function() {

    loadCandidate();

    loadRecruitmentProgress();

});