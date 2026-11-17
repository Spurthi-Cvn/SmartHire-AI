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

const stageLinks = {
    resume: "upload_resume.html",
    ats: "ats_screening.html",
    aptitude: "aptitude.html",
    technical: "technical.html",
    communication: "communication.html",
    hr: "hr.html",
    selection: "selection.html",
    offer: "offer.html",
    onboarding: "onboarding.html"
};

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
            throw new Error("Unable to load candidate profile.");
        }

        const data = await response.json();

        const name = data.name || "Candidate";
        const email = data.email || "Not available";
        const phone = data.phone || "Not available";

        document.getElementById("candidateName").innerText = name;
        document.getElementById("candidateEmail").innerText = email;
        document.getElementById("candidatePhone").innerText = phone;

        document.getElementById("welcomeName").innerText = name;
        document.getElementById("topbarCandidateName").innerText = name;

        const initial = name.charAt(0).toUpperCase();

        document.getElementById("profileAvatar").innerText = initial;
        document.getElementById("largeAvatar").innerText = initial;

    } catch (error) {

        console.error("Profile loading error:", error);

    }
}


// =====================================
// LOAD RECRUITMENT PROGRESS
// =====================================

async function loadRecruitmentProgress() {

    try {

        const [progressResponse, resumeResponse] = await Promise.all([

            fetch(`${API_BASE_URL}/candidate/${candidateId}/progress`),

            fetch(`${API_BASE_URL}/resume/${candidateId}`)

        ]);

        if (!progressResponse.ok) {
            throw new Error("Unable to load recruitment progress.");
        }

        const progress = await progressResponse.json();

        // Resume may not exist yet for a new candidate.
        let resume = {};

        if (resumeResponse.ok) {
            resume = await resumeResponse.json();
        }

        updateRecruitmentProgress(progress, resume);

    } catch (error) {

        console.error("Progress loading error:", error);

    }
}


// =====================================
// CHECK COMPLETED STATUS
// =====================================

function isCompleted(status) {

    return [
        "Passed",
        "Completed",
        "Selected",
        "Offered",
        "Joined"
    ].includes(status);

}


// =====================================
// UPDATE RECRUITMENT DASHBOARD
// =====================================

function updateRecruitmentProgress(progress, resume) {

    const resumeUploaded = Boolean(
        resume.resume_uploaded ||
        resume.filename ||
        resume.id
    );

    const statusMap = {

        resume: resumeUploaded ? "Completed" : "Pending",

        ats: progress.ats_status,

        aptitude: progress.aptitude_status,

        technical: progress.technical_status,

        communication: progress.communication_status,

        hr: progress.hr_status,

        selection: progress.selection_status,

        offer: progress.offer_status,

        onboarding: progress.onboarding_status

    };

    let completedCount = 0;

    stages.forEach((stage) => {

        const row = document.getElementById(`stage-${stage}`);

        const button = document.getElementById(`${stage}Button`);

        if (!row || !button) return;

        const status = statusMap[stage];

        const completed = isCompleted(status);

        const failed = status === "Failed" || status === "Rejected";

        const unlocked =
            progress.current_stage === stage ||
            (stage === "resume" && !resumeUploaded);

        row.classList.remove("locked", "completed", "failed");

        button.onclick = null;

        button.removeAttribute("aria-disabled");

        if (completed) {

            completedCount++;

            row.classList.add("completed");

            button.innerText = "✓ Completed";

            button.style.background = "";

            button.removeAttribute("href");

        }

        else if (failed) {

            row.classList.add("failed");

            button.innerText = status;

            button.style.background = "";

            button.removeAttribute("href");

        }

        else if (unlocked) {

            button.innerText = "Start";

            button.style.background = "";

            button.href = stageLinks[stage];

        }

        else {

            row.classList.add("locked");

            button.innerText = "🔒 Locked";

            button.style.background = "";

            button.removeAttribute("href");

            button.onclick = function(event) {

                event.preventDefault();

                alert(
                    "Please complete the previous recruitment stage first."
                );

            };

        }

    });


    // =====================================
    // UPDATE PROGRESS PERCENTAGE
    // =====================================

    const percentage = Math.round(
        (completedCount / stages.length) * 100
    );

    document.getElementById("progressBar").style.width =
        percentage + "%";

    document.getElementById("progressText").innerText =
        percentage + "%";

    document.getElementById("statProgress").innerText =
        percentage + "%";

    document.getElementById("completedStages").innerText =
        `${completedCount} / ${stages.length}`;


    // =====================================
    // APPLICATION STATUS
    // =====================================

    let applicationStatus = "In Progress";

    if (progress.current_stage === "completed") {

        applicationStatus = "Completed";

    } else if (progress.selection_status === "Rejected") {

        applicationStatus = "Not Selected";

    } else if (progress.selection_status === "Selected") {

        applicationStatus = "Selected";

    }

    document.getElementById("applicationStatus").innerText =
        applicationStatus;


    // =====================================
    // OFFER AND ONBOARDING SUMMARY
    // =====================================

    const offerStatus = progress.offer_status || "Pending";

    const onboardingStatus = progress.onboarding_status || "Pending";

    const offerSummary = document.getElementById("offerSummaryStatus");

    if (offerSummary) {

        if (onboardingStatus === "Completed") {

            offerSummary.innerText = "Onboarding Completed";

        } else if (offerStatus === "Offered") {

            offerSummary.innerText = "Offer Generated";

        } else {

            offerSummary.innerText = "Awaiting Offer";

        }

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
// LOAD DASHBOARD
// =====================================

document.addEventListener("DOMContentLoaded", function() {

    if (!candidateId) return;

    loadCandidate();

    loadRecruitmentProgress();

});