// ===============================
// APTITUDE TEST
// ===============================

const questions = [

    {
        question: "Which AWS service is mainly used to provide virtual servers?",
        options: [
            "Amazon S3",
            "Amazon EC2",
            "Amazon RDS",
            "Amazon Lambda"
        ],
        answer: 1,
        explanation:
            "Amazon EC2 provides virtual servers (instances) that can be used to run applications in the AWS cloud."
    },

    {
        question: "Which tool is commonly used for container orchestration?",
        options: [
            "Git",
            "Jenkins",
            "Kubernetes",
            "Terraform"
        ],
        answer: 2,
        explanation:
            "Kubernetes is a container orchestration platform used to deploy, manage, scale, and automate containers."
    },

    {
        question: "Which command is used to check the current Git status?",
        options: [
            "git check",
            "git status",
            "git current",
            "git show-status"
        ],
        answer: 1,
        explanation:
            "The 'git status' command shows the current state of your working directory and staging area."
    },

    {
        question: "What is Docker primarily used for?",
        options: [
            "Database management",
            "Containerization",
            "Version control",
            "Cloud billing"
        ],
        answer: 1,
        explanation:
            "Docker is primarily used for containerization, allowing applications and their dependencies to run in isolated containers."
    },

    {
        question: "Which tool is commonly used for Infrastructure as Code?",
        options: [
            "Terraform",
            "GitHub",
            "Docker",
            "MySQL"
        ],
        answer: 0,
        explanation:
            "Terraform is an Infrastructure as Code (IaC) tool used to define and provision infrastructure using configuration files."
    }

];


// ===============================
// VARIABLES
// ===============================

let currentQuestion = 0;

let score = 0;

let userAnswers = [];

let timeLeft = 300;


// ===============================
// ELEMENTS
// ===============================

const questionNumber =
    document.getElementById("questionNumber");

const questionText =
    document.getElementById("questionText");

const optionsContainer =
    document.getElementById("options");

const nextBtn =
    document.getElementById("nextBtn");

const timer =
    document.getElementById("timer");

const questionContainer =
    document.getElementById("questionContainer");

const result =
    document.getElementById("result");

const scoreText =
    document.getElementById("score");

const resultMessage =
    document.getElementById("resultMessage");


// ===============================
// LOAD QUESTION
// ===============================

function loadQuestion() {

    const question = questions[currentQuestion];

    questionNumber.innerText =
        `Question ${currentQuestion + 1} of ${questions.length}`;

    questionText.innerText =
        question.question;

    optionsContainer.innerHTML = "";


    question.options.forEach((option, index) => {

        const div = document.createElement("div");

        div.className = "form-check mb-3";

        div.innerHTML = `

            <input
                class="form-check-input"
                type="radio"
                name="answer"
                id="option${index}"
                value="${index}"
            >

            <label
                class="form-check-label"
                for="option${index}">

                ${option}

            </label>

        `;

        optionsContainer.appendChild(div);

    });

}


// ===============================
// NEXT QUESTION
// ===============================

nextBtn.addEventListener("click", function () {

    const selected =
        document.querySelector(
            'input[name="answer"]:checked'
        );


    if (!selected) {

        alert("Please select an answer.");

        return;

    }


    const selectedAnswer =
        parseInt(selected.value);


    // Store user's answer

    userAnswers.push(selectedAnswer);


    // Check answer

    if (
        selectedAnswer ===
        questions[currentQuestion].answer
    ) {

        score++;

    }


    currentQuestion++;


    if (currentQuestion < questions.length) {

        loadQuestion();

    } else {

        finishTest();

    }

});


// ===============================
// FINISH TEST
// ===============================

function finishTest() {

    questionContainer.style.display = "none";

    nextBtn.style.display = "none";

   const percentage = Math.round(
    (score / questions.length) * 100
);

// =====================================
// MARK APTITUDE STAGE AS COMPLETED
// =====================================

if (percentage >= 60) {

    localStorage.setItem(
        "stage_aptitude",
        "completed"
    );

} else {

    localStorage.removeItem(
        "stage_aptitude"
    );

}


    scoreText.innerText =
        `Score: ${score}/${questions.length} (${percentage}%)`;


    if (percentage >= 60) {

        resultMessage.innerText =
            "Congratulations! You have qualified for the next round. 🎉";

    } else {

        resultMessage.innerText =
            "Unfortunately, you did not qualify for the next round.";

    }


    // Show result section

    result.style.display = "block";


    // Create review section

    showAnswerReview();

}


// ===============================
// SHOW ANSWER REVIEW
// ===============================

function showAnswerReview() {

    const reviewContainer =
        document.createElement("div");

    reviewContainer.className =
        "mt-4 text-start";


    const heading =
        document.createElement("h4");

    heading.innerText =
        "📋 Answer Review";

    heading.className =
        "mb-4";

    reviewContainer.appendChild(heading);


    questions.forEach((question, index) => {

        const userAnswer =
            userAnswers[index];

        const correctAnswer =
            question.answer;


        const isCorrect =
            userAnswer === correctAnswer;


        const review =
            document.createElement("div");

        review.className =
            "p-3 mb-3 rounded border";


        if (isCorrect) {

            review.classList.add(
                "border-success"
            );

        } else {

            review.classList.add(
                "border-danger"
            );

        }


        review.innerHTML = `

            <h5>

                ${isCorrect ? "✅" : "❌"}

                Question ${index + 1}

            </h5>

            <p>

                <strong>
                    ${question.question}
                </strong>

            </p>

            <p>

                <strong>Your answer:</strong>

                ${question.options[userAnswer]}

            </p>


            ${
                !isCorrect
                ? `

                <p class="text-success">

                    <strong>
                        Correct answer:
                    </strong>

                    ${question.options[correctAnswer]}

                </p>

                `
                : ""
            }


            <p>

                <strong>Explanation:</strong>

                ${question.explanation}

            </p>

        `;


        reviewContainer.appendChild(review);

    });


    result.appendChild(reviewContainer);

}


// ===============================
// TIMER
// ===============================

const countdown =
    setInterval(function () {

        let minutes =
            Math.floor(timeLeft / 60);

        let seconds =
            timeLeft % 60;


        seconds =
            seconds < 10
                ? "0" + seconds
                : seconds;


        timer.innerText =
            `${minutes}:${seconds}`;


        timeLeft--;


        if (timeLeft < 0) {

            clearInterval(countdown);

            alert("Time is over!");

            finishTest();

        }

    }, 1000);


// ===============================
// START TEST
// ===============================

loadQuestion();