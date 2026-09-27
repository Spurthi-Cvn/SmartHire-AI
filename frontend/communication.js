// =====================================
// COMMUNICATION ROUND
// =====================================

const questions = [

    {
        question:
            "Choose the most professional response when a colleague asks for help.",

        options: [
            "I don't have time for this.",
            "You should figure it out yourself.",
            "Sure, I'll help you. Let's discuss the issue.",
            "Ask someone else."
        ],

        answer: 2,

        explanation:
            "A professional response should be polite, cooperative, and willing to help."
    },


    {
        question:
            "Which sentence is grammatically correct?",

        options: [
            "He don't like working late.",
            "He doesn't likes working late.",
            "He doesn't like working late.",
            "He not like working late."
        ],

        answer: 2,

        explanation:
            "With 'he', use 'doesn't' followed by the base form of the verb: 'doesn't like'."
    },


    {
        question:
            "What is the best way to communicate during a team disagreement?",

        options: [
            "Interrupt everyone.",
            "Listen to others and explain your point respectfully.",
            "Ignore the discussion.",
            "Argue until everyone agrees."
        ],

        answer: 1,

        explanation:
            "Effective communication involves active listening and respectfully expressing your viewpoint."
    },


    {
        question:
            "Choose the most appropriate sentence for a professional email.",

        options: [
            "Send me the file ASAP.",
            "Hey, send the file.",
            "Could you please share the file when convenient?",
            "I need the file now."
        ],

        answer: 2,

        explanation:
            "Professional emails should use polite and respectful language."
    },


    {
        question:
            "If you do not understand an instruction from your manager, what should you do?",

        options: [
            "Pretend that you understood.",
            "Ignore the instruction.",
            "Politely ask for clarification.",
            "Ask another employee to do the work."
        ],

        answer: 2,

        explanation:
            "Asking for clarification helps avoid mistakes and demonstrates responsible communication."
    }

];


// =====================================
// VARIABLES
// =====================================

let currentQuestion = 0;

let score = 0;

let userAnswers = [];

let timeLeft = 600;

let countdown;


// =====================================
// ELEMENTS
// =====================================

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


// =====================================
// LOAD QUESTION
// =====================================

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
                    for="option${index}"
                >
                    ${option}
                </label>

            `;

            optionsContainer.appendChild(div);

        }
    );

}


// =====================================
// NEXT QUESTION
// =====================================

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


// =====================================
// FINISH TEST
// =====================================

function finishTest() {

    clearInterval(countdown);


    questionContainer.style.display =
        "none";


    nextBtn.style.display =
        "none";


    const percentage =
        Math.round(
            (score / questions.length) * 100
        );


    // =====================================
    // MARK COMMUNICATION STAGE
    // =====================================

    if (percentage >= 60) {

        localStorage.setItem(
            "stage_communication",
            "completed"
        );

    }
    else {

        localStorage.removeItem(
            "stage_communication"
        );

    }


    // =====================================
    // SHOW SCORE
    // =====================================

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


// =====================================
// ANSWER REVIEW
// =====================================

function showAnswerReview() {

    const reviewContainer =
        document.createElement("div");


    reviewContainer.className =
        "mt-4";


    const heading =
        document.createElement("h4");


    heading.innerText =
        "📋 Communication Answer Review";


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

                    ${question.options[userAnswer] ?? "Not answered"}
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


// =====================================
// TIMER
// =====================================

countdown =
    setInterval(
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


// =====================================
// START
// =====================================

loadQuestion();