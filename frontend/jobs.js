const API_BASE_URL = "http://127.0.0.1:8000";

let allJobs = [];

// Fetch jobs from FastAPI
async function fetchJobs() {
    const jobsList = document.getElementById("jobsList");
    const jobCount = document.getElementById("jobCount");

    try {
        const response = await fetch(`${API_BASE_URL}/jobs`);

        if (!response.ok) {
            throw new Error("Unable to fetch jobs");
        }

        const data = await response.json();

        // Support either an array or an object containing a jobs array
        allJobs = Array.isArray(data)
            ? data
            : (data.jobs || []);

        loadJobs();

    } catch (error) {
        console.error("Error fetching jobs:", error);

        jobsList.innerHTML = `
            <div class="no-jobs">
                <h3>Unable to load jobs</h3>
                <p>Please check whether your FastAPI server is running.</p>
                <button onclick="fetchJobs()">Try Again</button>
            </div>
        `;

        jobCount.textContent = "0 jobs";
    }
}


// Search and filter jobs
function loadJobs() {
    const searchValue = document
        .getElementById("searchInput")
        .value.toLowerCase()
        .trim();

    const locationValue = document
        .getElementById("locationFilter")
        .value.toLowerCase();

    const experienceValue = document
        .getElementById("experienceFilter")
        .value.toLowerCase();

    const typeValue = document
        .getElementById("typeFilter")
        .value.toLowerCase();

    const filteredJobs = allJobs.filter(job => {

        const searchableText = `
            ${job.title}
            ${job.department}
            ${job.required_skills}
            ${job.description}
        `.toLowerCase();

        const matchesSearch = searchableText.includes(searchValue);

        const matchesLocation = !locationValue ||
            (job.location || "").toLowerCase().includes(locationValue);

        const matchesExperience = !experienceValue ||
            (job.experience || "").toLowerCase().includes(experienceValue);

        const matchesType = !typeValue ||
            (job.employment_type || "").toLowerCase() === typeValue;

        return matchesSearch &&
               matchesLocation &&
               matchesExperience &&
               matchesType;
    });

    displayJobs(filteredJobs);
}


// Display job cards
function displayJobs(jobs) {
    const jobsList = document.getElementById("jobsList");
    const jobCount = document.getElementById("jobCount");

    jobCount.textContent = `${jobs.length} jobs found`;

    if (jobs.length === 0) {
        jobsList.innerHTML = `
            <div class="no-jobs">
                <h3>No matching jobs found</h3>
                <p>Try changing your search or filters.</p>
            </div>
        `;
        return;
    }

    jobsList.innerHTML = jobs.map(job => `
        <div class="job-card">

            <h3>${escapeHTML(job.title)}</h3>

            <p>${escapeHTML(job.department || "Cloud & DevOps")}</p>

            <div class="job-meta">
                <span>📍 ${escapeHTML(job.location || "Not specified")}</span>
                <span>💼 ${escapeHTML(job.employment_type || "Full Time")}</span>
                <span>🎓 ${escapeHTML(job.experience || "Not specified")}</span>
            </div>

            <p>${escapeHTML(job.description || "")}</p>

            <p class="job-skills">
                <strong>Required Skills:</strong>
                ${escapeHTML(job.required_skills || "Not specified")}
            </p>

            <div class="job-bottom">
                <span class="job-salary">
                    ${escapeHTML(job.salary_range || "Salary not disclosed")}
                </span>

                <button
                    class="apply-btn"
                    onclick="applyForJob(${Number(job.id)})">
                    Apply Now
                </button>
            </div>

        </div>
    `).join("");
}


// Basic HTML escaping for database values
function escapeHTML(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[character]);
}


// Temporary Apply button
// We will connect this to the JobApplication API next.
// =====================================
// APPLY FOR A JOB
// =====================================

async function applyForJob(jobId) {

    // Get logged-in candidate ID
    const candidateId = localStorage.getItem("candidate_id");

    if (!candidateId) {
        alert("Please login before applying for a job.");
        window.location.href = "login.html";
        return;
    }

    const confirmApply = confirm(
        "Are you sure you want to apply for this job?"
    );

    if (!confirmApply) {
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/jobs/${jobId}/apply?candidate_id=${encodeURIComponent(candidateId)}`,
            {
                method: "POST"
            }
        );

        const data = await response.json();

        if (response.ok) {

            alert(
                "Application submitted successfully!\n\n" +
                "Job: " + data.job_title + "\n" +
                "Application ID: " + data.application_id + "\n" +
                "Status: " + data.application_status
            );

        } else if (response.status === 409) {

            alert("You have already applied for this job.");

        } else {

            alert(data.detail || "Unable to submit application.");

        }

    } catch (error) {

        console.error("Application error:", error);

        alert("Unable to connect to the server. Please try again.");

    }
}


// Automatically fetch jobs when the page opens
document.addEventListener("DOMContentLoaded", () => {

    fetchJobs();

    document.getElementById("searchInput")
        .addEventListener("input", loadJobs);

    document.getElementById("locationFilter")
        .addEventListener("change", loadJobs);

    document.getElementById("experienceFilter")
        .addEventListener("change", loadJobs);

    document.getElementById("typeFilter")
        .addEventListener("change", loadJobs);
});