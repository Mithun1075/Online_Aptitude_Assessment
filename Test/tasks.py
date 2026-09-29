from celery import shared_task

from .models import (
    Candidate,
    CandidateAnswer,
    Result
)


@shared_task
def calculate_score(candidate_id):

    try:
        candidate = Candidate.objects.get(id=candidate_id)

    except Candidate.DoesNotExist:
        return "Candidate not found"


    answers = CandidateAnswer.objects.filter(
        candidate=candidate
    )

    score = 0

    total_questions = answers.count()


    for answer in answers:

        if answer.selected_answer == answer.question.correct_answer:
            score += 1


    Result.objects.update_or_create(

        candidate=candidate,

        defaults={
            "score": score,
            "total_questions": total_questions,
        }

    )

    return f"Score calculated successfully ({score}/{total_questions})"