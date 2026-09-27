// =====================================
// DOCUMENT REVIEW
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
        name: "Aadhaar / Government ID",
        icon: "fa-id-card"
    },

    {
        key: "pan",
        name: "PAN Card",
        icon: "fa-credit-card"
    },

    {
        key: "tenth",
        name: "10th Marksheet",
        icon: "fa-school"
    },

    {
        key: "twelfth",
        name: "12th Marksheet",
        icon: "fa-school"
    },

    {
        key: "graduation",
        name: "Graduation Certificate",
        icon: "fa-graduation-cap"
    },

    {
        key: "photo",
        name: "Passport Size Photograph",
        icon: "fa-image"
    }

];


// =====================================
// LOAD CANDIDATE
// =====================================

async function loadCandidate() {

    try {

        const response =
            await fetch(
                `http://127.0.0.1:8000/candidate/${candidateId}`
            );

        if (!response.ok) {

            throw new Error(
                "Candidate API request failed."
            );

        }

        const data =
            await response.json();


        // Candidate Name

        const nameElement =
            document.getElementById(
                "candidateName"
            );

        if (nameElement) {

            nameElement.innerText =
                data.name ||
                "Not Available";

        }


        // Candidate ID

        const idElement =
            document.getElementById(
                "candidateId"
            );

        if (idElement) {

            idElement.innerText =
                "SH-2026-" +
                String(candidateId)
                    .padStart(4, "0");

        }

    }
    catch (error) {

        console.error(
            "Candidate loading error:",
            error
        );


        const nameElement =
            document.getElementById(
                "candidateName"
            );

        const idElement =
            document.getElementById(
                "candidateId"
            );


        if (nameElement) {

            nameElement.innerText =
                "Unable to load";

        }


        if (idElement) {

            idElement.innerText =
                "SH-2026-" +
                String(candidateId)
                    .padStart(4, "0");

        }

    }

}


// =====================================
// LOAD DOCUMENTS
// =====================================

function loadDocuments() {

    const documentList =
        document.getElementById(
            "documentList"
        );


    if (!documentList) {

        console.error(
            "documentList element not found."
        );

        return;

    }


    documentList.innerHTML = "";


    let uploadedCount = 0;


    // =================================
    // DISPLAY EACH DOCUMENT
    // =================================

    documents.forEach(function(doc) {

        const fileName =
            localStorage.getItem(
                "document_" + doc.key
            );


        const fileData =
            localStorage.getItem(
                "document_data_" + doc.key
            );


        const row =
            document.createElement("div");


        row.className =
            "border rounded p-3 mb-3";


        // =================================
        // DOCUMENT NOT UPLOADED
        // =================================

        if (!fileName) {

            row.innerHTML = `

                <div
                    class="d-flex
                           justify-content-between
                           align-items-center"
                >

                    <div>

                        <strong>

                            <i
                                class="fa-solid ${doc.icon}"
                            ></i>

                            ${doc.name}

                        </strong>

                        <br>

                        <small class="text-danger">

                            Document not uploaded

                        </small>

                    </div>


                    <span
                        class="badge bg-danger"
                    >

                        ✕ Missing

                    </span>

                </div>

            `;

        }


        // =================================
        // DOCUMENT UPLOADED
        // =================================

        else {

            uploadedCount++;


            row.innerHTML = `

                <div
                    class="d-flex
                           justify-content-between
                           align-items-center"
                >

                    <div>

                        <strong>

                            <i
                                class="fa-solid ${doc.icon}"
                            ></i>

                            ${doc.name}

                        </strong>

                        <br>

                        <small class="text-muted">

                            ${fileName}

                        </small>

                    </div>


                    <div>

                        <span
                            class="badge bg-success me-2"
                        >

                            ✓ Uploaded

                        </span>


                        ${
                            fileData
                            ?

                            `

                            <button
                                class="btn
                                       btn-sm
                                       btn-outline-primary"

                                onclick="
                                    viewDocument('${doc.key}')
                                "
                            >

                                <i
                                    class="fa-solid fa-eye"
                                ></i>

                                View

                            </button>

                            `

                            :

                            ""

                        }

                    </div>

                </div>

            `;

        }


        documentList.appendChild(row);

    });


    // =====================================
    // CHECK ALL DOCUMENTS
    // =====================================

    const confirmCheckbox =
        document.getElementById(
            "confirmDocuments"
        );


    const confirmBtn =
        document.getElementById(
            "confirmBtn"
        );


    // =====================================
    // NOT ALL DOCUMENTS UPLOADED
    // =====================================

    if (
        uploadedCount !==
        documents.length
    ) {

        if (confirmCheckbox) {

            confirmCheckbox.disabled =
                true;

            confirmCheckbox.checked =
                false;

        }


        if (confirmBtn) {

            confirmBtn.disabled =
                true;

        }

    }


    // =====================================
    // ALL DOCUMENTS UPLOADED
    // =====================================

    else {

        if (confirmCheckbox) {

            confirmCheckbox.disabled =
                false;

        }

    }

}


// =====================================
// VIEW DOCUMENT
// =====================================

function viewDocument(key) {

    const fileData =
        localStorage.getItem(
            "document_data_" + key
        );


    if (!fileData) {

        alert(
            "Preview is not available for this document."
        );

        return;

    }


    const newWindow =
        window.open();


    if (!newWindow) {

        alert(
            "Please allow pop-ups to view the document."
        );

        return;

    }


    newWindow.document.write(`

        <!DOCTYPE html>

        <html>

        <head>

            <title>
                Document Preview
            </title>

        </head>


        <body
            style="
                margin:0;
                padding:20px;
                background:#f5f5f5;
                text-align:center;
            "
        >

            <h3>
                Document Preview
            </h3>


            <iframe

                src="${fileData}"

                style="
                    width:95%;
                    height:85vh;
                    border:1px solid #ccc;
                    background:white;
                "

            ></iframe>

        </body>

        </html>

    `);

}


// =====================================
// CONFIRMATION CHECKBOX
// =====================================

const confirmCheckbox =
    document.getElementById(
        "confirmDocuments"
    );


const confirmBtn =
    document.getElementById(
        "confirmBtn"
    );


if (
    confirmCheckbox &&
    confirmBtn
) {

    confirmCheckbox.addEventListener(
        "change",
        function() {

            confirmBtn.disabled =
                !confirmCheckbox.checked;

        }
    );

}


// =====================================
// CONFIRM DOCUMENTS
// =====================================

if (confirmBtn) {

    confirmBtn.addEventListener(
        "click",
        function() {

            // =========================
            // CHECKBOX VALIDATION
            // =========================

            if (
                !confirmCheckbox ||
                !confirmCheckbox.checked
            ) {

                alert(
                    "Please review and confirm all documents first."
                );

                return;

            }


            // =========================
            // MARK VERIFICATION COMPLETE
            // =========================

            localStorage.setItem(
                "document_verification",
                "completed"
            );


            localStorage.setItem(
                "stage_document_verification",
                "completed"
            );


            // =========================
            // SHOW SUCCESS MESSAGE
            // =========================

            const reviewStatus =
                document.getElementById(
                    "reviewStatus"
                );


            if (reviewStatus) {

                reviewStatus.innerHTML = `

                    <div
                        class="alert alert-success"
                    >

                        <i
                            class="fa-solid
                                   fa-circle-check"
                        ></i>

                        <strong>

                            All documents confirmed
                            successfully.

                        </strong>

                        <br>

                        Moving to Background
                        Verification...

                    </div>

                `;

            }


            // =========================
            // DISABLE BUTTON
            // =========================

            confirmBtn.disabled =
                true;


            // =========================
            // NEXT PAGE
            // =========================

            setTimeout(
                function() {

                    window.location.href =
                        "background-verification.html";

                },
                1500
            );

        }
    );

}


// =====================================
// INITIALIZE
// =====================================

loadCandidate();

loadDocuments();