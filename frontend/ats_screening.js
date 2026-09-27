// ================= ATS SCREENING =================

const loading = document.getElementById("loading");
const result = document.getElementById("result");

const jobTitle = document.getElementById("jobTitle");
const requiredSkills = document.getElementById("requiredSkills");

const matchPercentage = document.getElementById("matchPercentage");
const matchedSkills = document.getElementById("matchedSkills");
const missingSkills = document.getElementById("missingSkills");
const screeningStatus = document.getElementById("screeningStatus");


// ================= LOAD ATS DATA =================

async function runATSScreening() {

    try {

        // Get job details
        const jobResponse = await fetch(
            "http://127.0.0.1:8000/job/aws-devops"
        );

        if (!jobResponse.ok) {
            throw new Error("Unable to load job details");
        }

        const jobData = await jobResponse.json();

        // Display job title
        jobTitle.textContent = jobData.role;


        // Display required skills
        requiredSkills.innerHTML = "";

        jobData.required_skills.forEach(function(skill) {

            const badge = document.createElement("span");

            badge.className = "badge bg-primary me-2 mb-2";

            badge.textContent = skill;

            requiredSkills.appendChild(badge);

        });


        // Get logged-in candidate
        const candidateId = localStorage.getItem("candidate_id");

        if (!candidateId) {

            alert("Please login first.");

            window.location.href = "login.html";

            return;

        }


        // Get candidate resume
        const resumeResponse = await fetch(
            `http://127.0.0.1:8000/resume/${candidateId}`
        );

        if (!resumeResponse.ok) {

            throw new Error(
                "Resume not found. Please upload your resume first."
            );

        }

        const resumeData = await resumeResponse.json();


        // Resume skills
        const resumeSkills = resumeData.skills || [];


        // Compare skills
        const required = jobData.required_skills.map(skill =>
            skill.toLowerCase()
        );


        const candidateSkills = resumeSkills.map(skill =>
            skill.toLowerCase()
        );


        const matched = jobData.required_skills.filter(skill =>
            candidateSkills.includes(skill.toLowerCase())
        );


        const missing = jobData.required_skills.filter(skill =>
            !candidateSkills.includes(skill.toLowerCase())
        );

        const percentage = Math.round(
            (matched.length / required.length) * 100
        );


        // =====================================
        // MARK ATS STAGE AS COMPLETED
        // =====================================

        if (percentage >= 70) {

            localStorage.setItem(
                "stage_ats",
                "completed"
            );

        } else {

            localStorage.removeItem(
                "stage_ats"
            );

        }

        // Hide loading
        loading.style.display = "none";

        // Show result
        result.style.display = "block";


        // Display percentage
        matchPercentage.textContent = percentage + "%";


        // Display matched skills
        matchedSkills.innerHTML = "";

        if (matched.length === 0) {

            matchedSkills.innerHTML =
                '<span class="text-danger">No required skills matched.</span>';

        } else {

            matched.forEach(function(skill) {

                const badge = document.createElement("span");

                badge.className = "badge bg-success me-2 mb-2";

                badge.textContent = skill;

                matchedSkills.appendChild(badge);

            });

        }


        // Display missing skills
        missingSkills.innerHTML = "";

        if (missing.length === 0) {

            missingSkills.innerHTML =
                '<span class="text-success">No missing skills 🎉</span>';

        } else {

            missing.forEach(function(skill) {

                const badge = document.createElement("span");

                badge.className = "badge bg-danger me-2 mb-2";

                badge.textContent = skill;

                missingSkills.appendChild(badge);

            });

        }


        // Screening decision
        if (percentage >= 70) {

            screeningStatus.textContent =
                "✅ Shortlisted for next round";

            screeningStatus.className = "text-success";

        } else {

            screeningStatus.textContent =
                "❌ Not shortlisted";

            screeningStatus.className = "text-danger";

        }


    } catch (error) {

        console.error("ATS Error:", error);

        loading.style.display = "none";

        alert(error.message);

    }

}


// Run ATS screening
runATSScreening();