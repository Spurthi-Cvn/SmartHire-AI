console.log("resume.js loaded");


document.addEventListener("DOMContentLoaded", function () {

    const resumeForm = document.getElementById("resumeForm");

    const loading = document.getElementById("resumeLoading");

    const resumeFile = document.getElementById("resumeFile");


    if (!resumeForm) {

        console.error("Resume form not found!");

        return;

    }


    resumeForm.addEventListener("submit", async function (e) {

        e.preventDefault();


        console.log("Upload button clicked");


        // Get logged-in candidate ID

        const candidateId =
            localStorage.getItem("candidate_id");


        console.log(
            "Candidate ID:",
            candidateId
        );


        if (!candidateId) {

            alert(
                "Candidate ID not found. Please login again."
            );

            window.location.href = "login.html";

            return;

        }


        // Get selected file

        const file = resumeFile.files[0];


        if (!file) {

            alert(
                "Please select a PDF resume first."
            );

            return;

        }


        console.log(
            "Selected file:",
            file.name
        );


        loading.style.display = "block";


        // Create FormData

        const formData = new FormData();


        formData.append(
            "candidate_id",
            candidateId
        );


        formData.append(
            "file",
            file
        );


        try {

            console.log(
                "Sending resume to backend..."
            );


            const response = await fetch(
                "http://127.0.0.1:8000/upload-resume",
                {
                    method: "POST",
                    body: formData
                }
            );


            console.log(
                "Response status:",
                response.status
            );


            const data = await response.json();


            console.log(
                "Backend response:",
                data
            );


            loading.style.display = "none";


            if (!response.ok) {

                alert(
                    data.detail ||
                    data.message ||
                    "Resume upload failed."
                );

                return;

            }

                alert(data.message);

                localStorage.setItem(
                    "stage_resume",
                    "completed"
                );

                window.location.href = "dashboard.html";


            console.log(
                "Resume ID:",
                data.resume_id
            );


            console.log(
                "Skills:",
                data.skills
            );


            console.log(
                "Match percentage:",
                data.match_percentage
            );


            // Go to dashboard
            localStorage.setItem(
                "stage_resume",
                "completed"
            );

            window.location.href =
                "dashboard.html";


        }

        catch (error) {

            loading.style.display = "none";


            console.error(
                "Upload error:",
                error
            );


            alert(
                "Failed to connect to backend."
            );

        }

    });

});