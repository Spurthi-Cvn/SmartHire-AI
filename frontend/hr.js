// =====================================
// HR ROUND
// =====================================

const questions = [

    {
        question:
            "Tell us about yourself. Which response is most appropriate in an HR interview?",

        options: [
            "I don't know what to say.",
            "I am a hardworking person and I have no weaknesses.",
            "I recently completed my graduation, developed technical skills through projects and training, and I am looking forward to starting my professional career.",
            "My friends can explain everything about me."
        ],

        answer: 2,

        explanation:
            "A good introduction should briefly cover your education, relevant skills or experience, and career objective."
    },


    {
        question:
            "You are working on a team project and a teammate is struggling with their task. What should you do?",

        options: [
            "Ignore them because it is their responsibility.",
            "Report them immediately without discussing the issue.",
            "Offer help, understand the problem, and work together toward a solution.",
            "Complete their entire task without informing them."
        ],

        answer: 2,

        explanation:
            "Supporting teammates and solving problems collaboratively demonstrates teamwork and responsibility."
    },


    {
        question:
            "Your manager gives you a task with a deadline that you think is difficult to meet. What should you do?",

        options: [
            "Ignore the deadline.",
            "Complain to your colleagues.",
            "Discuss the requirements and timeline with your manager and communicate any concerns early.",
            "Wait until the deadline and then explain why it was not completed."
        ],

        answer: 2,

        explanation:
            "Professional communication means discussing concerns early and working with your manager to manage expectations."
    },


    {
        question:
            "What would you do if you made a mistake at work?",

        options: [
            "Hide the mistake.",
            "Blame someone else.",
            "Accept responsibility, inform the appropriate person, and work on correcting it.",
            "Ignore it and hope nobody notices."
        ],

        answer: 2,

        explanation:
            "Taking responsibility and correcting mistakes demonstrates accountability and professionalism."
    },


    {
        question:
            "Where do you see yourself in the next few years?",

        options: [
            "I have no plans.",
            "I want to develop my skills, take on greater responsibilities, and contribute to the organization's goals.",
            "I only want a higher salary.",
            "I don't want to learn anything new."
        ],

        answer: 1,

        explanation:
            "A strong career response should demonstrate learning, growth, responsibility, and contribution to the organization."
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


   const percentage = Math.round(
    (score / questions.length) * 100
);

// =====================================
// MARK HR STAGE AS COMPLETED
// =====================================

if (percentage >= 60) {

    localStorage.setItem(
        "stage_hr",
        "completed"
    );

} else {

    localStorage.removeItem(
        "stage_hr"
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
        "📋 HR Answer Review";


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