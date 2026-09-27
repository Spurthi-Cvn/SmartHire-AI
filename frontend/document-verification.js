// =====================================
// DOCUMENT VERIFICATION
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
// DOCUMENT CONFIGURATION
// =====================================

const documents = [
    {
        key: "aadhaar",
        inputId: "aadhaar",
        name: "Aadhaar / Government ID"
    },
    {
        key: "pan",
        inputId: "pan",
        name: "PAN Card"
    },
    {
        key: "tenth",
        inputId: "tenth",
        name: "10th Marksheet"
    },
    {
        key: "twelfth",
        inputId: "twelfth",
        name: "12th Marksheet"
    },
    {
        key: "graduation",
        inputId: "graduation",
        name: "Graduation Certificate"
    },
    {
        key: "photo",
        inputId: "photo",
        name: "Passport Size Photograph"
    }
];


// =====================================
// CANDIDATE INFORMATION
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


        const candidateName =
            document.getElementById(
                "candidateName"
            );

        if (candidateName) {

            candidateName.innerText =
                data.name;

        }


        const candidateIdElement =
            document.getElementById(
                "candidateId"
            );

        if (candidateIdElement) {

            candidateIdElement.innerText =
                "SH-2026-" +
                String(candidateId).padStart(
                    4,
                    "0"
                );

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
// SAVE SELECTED DOCUMENT
// =====================================

function saveDocument(
    key,
    file
) {

    if (!file) {
        return;
    }


    // Save filename

    localStorage.setItem(
        "document_" + key,
        file.name
    );


    // Save file data for preview

    const reader =
        new FileReader();


    reader.onload =
        function(event) {

            localStorage.setItem(
                "document_data_" + key,
                event.target.result
            );

        };


    reader.readAsDataURL(file);

}


// =====================================
// DOCUMENT SUBMISSION
// =====================================

function submitDocuments() {

    let allUploaded = true;

    let missingDocuments = [];


    documents.forEach(
        function(doc) {

            const input =
                document.getElementById(
                    doc.inputId
                );


            if (!input || !input.files[0]) {

                allUploaded = false;

                missingDocuments.push(
                    doc.name
                );

                return;

            }


            saveDocument(
                doc.key,
                input.files[0]
            );

        }
    );


    // =================================
    // CHECK MISSING DOCUMENTS
    // =================================

    if (!allUploaded) {

        alert(
            "Please upload all required documents:\n\n" +
            missingDocuments.join("\n")
        );

        return;

    }


    // =================================
    // SHOW SUCCESS MESSAGE
    // =================================

    const status =
        document.getElementById(
            "verificationStatus"
        );


    if (status) {

        status.innerHTML = `

            <div class="alert alert-success">

                <i class="fa-solid fa-circle-check"></i>

                <strong>
                    Documents uploaded successfully.
                </strong>

                <br>

                Please review all uploaded documents
                before final confirmation.

            </div>

        `;

    }


    // =================================
    // GO TO REVIEW PAGE
    // =================================

    setTimeout(
        function() {

            window.location.href =
                "document-review.html";

        },
        800
    );

}


// =====================================
// FIND SUBMIT BUTTON
// =====================================

const submitButton =
    document.getElementById(
        "submitDocuments"
    );


if (submitButton) {

    submitButton.addEventListener(
        "click",
        function(event) {

            event.preventDefault();

            submitDocuments();

        }
    );

}


// =====================================
// INITIALIZE
// =====================================

loadCandidate();