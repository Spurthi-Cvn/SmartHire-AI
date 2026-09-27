// ===============================
// TECHNICAL INTERVIEW
// ===============================

const questions = [

    {
        question:
            "Which AWS service provides scalable virtual servers in the cloud?",

        options: [
            "Amazon S3",
            "Amazon EC2",
            "Amazon RDS",
            "Amazon VPC"
        ],

        answer: 1,

        explanation:
            "Amazon EC2 provides resizable compute capacity using virtual servers called instances."
    },


    {
        question:
            "Which Docker command is used to create an image from a Dockerfile?",

        options: [
            "docker run",
            "docker start",
            "docker build",
            "docker push"
        ],

        answer: 2,

        explanation:
            "docker build reads the Dockerfile and creates a Docker image."
    },


    {
        question:
            "Which Kubernetes object is commonly used to manage and maintain a set of identical Pods?",

        options: [
            "Service",
            "ConfigMap",
            "Deployment",
            "Secret"
        ],

        answer: 2,

        explanation:
            "A Kubernetes Deployment manages ReplicaSets and maintains the desired number of Pods."
    },


    {
        question:
            "Which tool is primarily used for Infrastructure as Code?",

        options: [
            "Jenkins",
            "Terraform",
            "Docker",
            "Git"
        ],

        answer: 1,

        explanation:
            "Terraform is an Infrastructure as Code tool used to define and provision infrastructure through configuration files."
    },


    {
        question:
            "Which Git command downloads changes from a remote repository and integrates them into the current branch?",

        options: [
            "git push",
            "git clone",
            "git pull",
            "git init"
        ],

        answer: 2,

        explanation:
            "git pull fetches changes from the remote repository and integrates them into the current local branch."
    }

];


// ===============================
// VARIABLES
// ===============================

let currentQuestion = 0;

let score = 0;

let userAnswers = [];

let timeLeft = 600;
let countdown;



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

    const question =
        questions[currentQuestion];


    questionNumber.innerText =
        `Question ${currentQuestion + 1} of ${questions.length}`;


    questionText.innerText =
        question.question;


    optionsContainer.innerHTML = "";


    question.options.forEach(
        function(option, index) {

            const div =
                document.createElement("div");


            div.className =
                "form-check mb-3";


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

        }
    );

}


// ===============================
// NEXT QUESTION
// ===============================

nextBtn.addEventListener(
    "click",
    function() {

        const selected =
            document.querySelector(
                'input[name="answer"]:checked'
            );


        if (!selected) {

            alert(
                "Please select an answer."
            );

            return;

        }


        const selectedAnswer =
            parseInt(selected.value);


        userAnswers.push(
            selectedAnswer
        );


        if (
            selectedAnswer ===
            questions[currentQuestion].answer
        ) {

            score++;

        }


        currentQuestion++;


        if (
            currentQuestion <
            questions.length
        ) {

            loadQuestion();

        }

        else {

            finishTest();

        }

    }
);


// ===============================
// FINISH TEST
// ===============================

function finishTest() {

    clearInterval(countdown);

    questionContainer.style.display =
        "none";

    nextBtn.style.display =
        "none";

    const percentage = Math.round(
    (score / questions.length) * 100
);

// =====================================
// MARK TECHNICAL STAGE AS COMPLETED
// =====================================

if (percentage >= 60) {

    localStorage.setItem(
        "stage_technical",
        "completed"
    );

} else {

    localStorage.removeItem(
        "stage_technical"
    );

}


    scoreText.innerText =
        `Score: ${score}/${questions.length} (${percentage}%)`;


    if (percentage >= 60) {

        resultMessage.innerText =
            "Congratulations! You have qualified for the next round. 🎉";

    }

    else {

        resultMessage.innerText =
            "You did not qualify for the next round.";

    }


    result.style.display =
        "block";


    showAnswerReview();

}


// ===============================
// ANSWER REVIEW
// ===============================

function showAnswerReview() {

    const reviewContainer =
        document.createElement("div");


    reviewContainer.className =
        "mt-4";


    const heading =
        document.createElement("h4");


    heading.innerText =
        "📋 Technical Answer Review";


    heading.className =
        "mb-4";


    reviewContainer.appendChild(
        heading
    );


    questions.forEach(
        function(question, index) {

            const userAnswer =
                userAnswers[index];


            const correctAnswer =
                question.answer;


            const isCorrect =
                userAnswer ===
                correctAnswer;


            const review =
                document.createElement("div");


            review.className =
                "p-3 mb-3 rounded border";


            if (isCorrect) {

                review.classList.add(
                    "border-success"
                );

            }

            else {

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

                    <strong>
                        Your answer:
                    </strong>

                    ${question.options[userAnswer]}

                </p>


                ${
                    !isCorrect
                    ?
                    `

                    <p class="text-success">

                        <strong>
                            Correct answer:
                        </strong>

                        ${question.options[correctAnswer]}

                    </p>

                    `
                    :
                    ""
                }


                <p>

                    <strong>
                        Explanation:
                    </strong>

                    ${question.explanation}

                </p>

            `;


            reviewContainer.appendChild(
                review
            );

        }
    );


    result.appendChild(
        reviewContainer
    );

}


// ===============================
// TIMER
// ===============================

countdown = setInterval(
        function() {

            let minutes =
                Math.floor(
                    timeLeft / 60
                );


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

                clearInterval(
                    countdown
                );


                alert(
                    "Time is over!"
                );


                finishTest();

            }

        },
        1000
    );


// ===============================
// START
// ===============================

loadQuestion();