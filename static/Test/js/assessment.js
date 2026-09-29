/* ===========================================================
   Online Aptitude Assessment — assessment.js
   Handles option selection highlighting, form validation,
   and submit confirmation on the assessment page.
   =========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    var assessmentForm = document.getElementById("assessmentForm");

    // If we are not on the assessment page, stop here.
    if (!assessmentForm) {
        return;
    }

    var questionCards = document.querySelectorAll(".question-card");

    /* -----------------------------------------------------
       1. Highlight selected option card
    ----------------------------------------------------- */
    questionCards.forEach(function (card) {
        var optionInputs = card.querySelectorAll(".option-input");

        optionInputs.forEach(function (input) {
            input.addEventListener("change", function () {
                // Remove selected state from all options in this card
                card.querySelectorAll(".option-card").forEach(function (optionCard) {
                    optionCard.classList.remove("option-selected");
                });

                // Add selected state to the chosen option
                if (input.checked) {
                    input.closest(".option-card").classList.add("option-selected");
                }

                // Clear the "unanswered" warning state once answered
                card.classList.remove("question-unanswered");
            });
        });
    });

    /* -----------------------------------------------------
       2. Validate all questions are answered, then confirm
    ----------------------------------------------------- */
    assessmentForm.addEventListener("submit", function (event) {
        var unansweredCards = [];

        questionCards.forEach(function (card) {
            var answered = card.querySelector(".option-input:checked");
            if (!answered) {
                unansweredCards.push(card);
                card.classList.add("question-unanswered");
            } else {
                card.classList.remove("question-unanswered");
            }
        });

        if (unansweredCards.length > 0) {
            event.preventDefault();

            alert(
                "Please answer all questions before submitting. " +
                "You have " + unansweredCards.length + " unanswered question(s)."
            );

            unansweredCards[0].scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

            return;
        }

        var confirmSubmit = confirm(
            "Are you sure you want to submit your assessment? You cannot change your answers later."
        );

        if (!confirmSubmit) {
            event.preventDefault();
        }
    });

});
