const API_BASE_URL = "http://127.0.0.1:8000";

// =====================================
// FETCH CANDIDATE APPLICATIONS
// =====================================

async function fetchMyApplications() {

    const candidateId = localStorage.getItem("candidate_id");

    const applicationsList = document.getElementById("applicationsList");
    const totalApplications = document.getElementById("totalApplications");

    // Check login
    if (!candidateId) {
        alert("Please login first.");
        window.location.href = "login.html";
        return;
    }

    try {

        const response = await fetch(
            `${API_BASE_URL}/my-applications/${encodeURIComponent(candidateId)}`
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Unable to fetch applications.");
        }

        // Display total applications
        totalApplications.textContent = data.total_applications;

        // Check empty applications
        if (data.applications.length === 0) {

            applicationsList.innerHTML = `
                <div class="empty-state">
                    <h3>No Applications Yet</h3>
                    <p>You haven't applied for any jobs yet.</p>
                    <a href="jobs.html">Explore Jobs</a>
                </div>
            `;

            return;
        }

        // Display application cards
        applicationsList.innerHTML = data.applications.map(app => `

            <div class="application-card">

                <h3>${escapeHTML(app.job_title)}</h3>

                <p>${escapeHTML(app.department || "Cloud & DevOps")}</p>

                <div class="application-details">

                    <span>📍 ${escapeHTML(app.location || "Not specified")}</span>

                    <span>💼 ${escapeHTML(app.employment_type || "Full Time")}</span>

                    <span>🎓 ${escapeHTML(app.experience || "Not specified")}</span>

                </div>

                <p>
                    <strong>Application ID:</strong>
                    ${Number(app.application_id)}
                </p>

                <p>
                    <strong>Applied On:</strong>
                    ${escapeHTML(app.application_date || "Not available")}
                </p>

                <span class="status-badge">
                    ${escapeHTML(app.application_status)}
                </span>

                <div class="application-actions">

                    <button
                        class="view-progress-btn"
                        onclick="viewProgress(${Number(app.application_id)})">

                        View Progress

                    </button>

                </div>

            </div>

        `).join("");

    } catch (error) {

        console.error("Application loading error:", error);

        applicationsList.innerHTML = `
            <div class="empty-state">
                <h3>Unable to load applications</h3>
                <p>${escapeHTML(error.message)}</p>
                <button onclick="fetchMyApplications()">
                    Try Again
                </button>
            </div>
        `;

    }
}


// =====================================
// VIEW APPLICATION PROGRESS
// =====================================

function viewProgress(applicationId) {

    alert(
        "Application ID: " + applicationId +
        "\n\nIndividual recruitment tracking will be connected next."
    );

}


// =====================================
// HTML SECURITY
// =====================================

function escapeHTML(value) {

    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[character]);

}


// =====================================
// LOAD APPLICATIONS
// =====================================

document.addEventListener("DOMContentLoaded", () => {

    fetchMyApplications();

});