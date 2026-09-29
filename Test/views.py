from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Candidate,
    Question,
    CandidateAnswer,
    Result
)

# from .tasks import calculate_score
from django.contrib import messages

def register(request):

    candidate_id = request.session.get("candidate_id")

    if candidate_id:
        messages.warning(request, "You are already registered.")
        return redirect("register_success")

    if request.method == "POST":

        email = request.POST.get("email")
        mobile = request.POST.get("mobile")

        if Candidate.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered.")
            return render(request, "Test/register.html")

        if Candidate.objects.filter(mobile=mobile).exists():
            messages.error(request, "This mobile number is already registered.")
            return render(request, "Test/register.html")

        candidate = Candidate.objects.create(
            name=request.POST.get("name"),
            email=email,
            mobile=mobile,
            college_name=request.POST.get("college_name"),
            degree=request.POST.get("degree"),
            year_of_passing=request.POST.get("year_of_passing"),
            position=request.POST.get("position"),
        )

        request.session["candidate_id"] = candidate.id

        return redirect("register_success")

    return render(request, "Test/register.html")

def register_success(request):

    candidate_id = request.session.get("candidate_id")

    if not candidate_id:
        return redirect("register")

    candidate = Candidate.objects.filter(id=candidate_id).first()

    if not candidate:
        request.session.flush()
        return redirect("register")

    return render(
        request,
        "Test/register_success.html",
        {
            "candidate": candidate
        }
    )

def assessment(request):

    candidate_id = request.session.get("candidate_id")

    if not candidate_id:
        return redirect("register")

    if Result.objects.filter(candidate_id=candidate_id).exists():
        return redirect("result")

    candidate = get_object_or_404(
        Candidate,
        id=candidate_id
    )

    # Generate questions only once
    if "question_ids" not in request.session:

        english = list(
            Question.objects.filter(
                category__name="English"
            ).order_by("?")[:5]
        )

        maths = list(
            Question.objects.filter(
                category__name="Maths"
            ).order_by("?")[:5]
        )

        python = list(
            Question.objects.filter(
                category__name="Python"
            ).order_by("?")[:5]
        )

        django = list(
            Question.objects.filter(
                category__name="Django"
            ).order_by("?")[:5]
        )

        request.session["question_ids"] = {
            "english": [q.id for q in english],
            "maths": [q.id for q in maths],
            "python": [q.id for q in python],
            "django": [q.id for q in django],
        }

    question_ids = request.session["question_ids"]

    context = {
        "candidate": candidate,

        "english_questions": Question.objects.filter(
            id__in=question_ids["english"]
        ),

        "maths_questions": Question.objects.filter(
            id__in=question_ids["maths"]
        ),

        "python_questions": Question.objects.filter(
            id__in=question_ids["python"]
        ),

        "django_questions": Question.objects.filter(
            id__in=question_ids["django"]
        ),
    }

    return render(
        request,
        "Test/assessment.html",
        context
    )

def submit_test(request):

    if request.method != "POST":
        return redirect("register")

    candidate_id = request.session.get("candidate_id")

    candidate = get_object_or_404(
        Candidate,
        id=candidate_id
    )

    CandidateAnswer.objects.filter(
        candidate=candidate
    ).delete()

    for key, value in request.POST.items():

        if key.startswith("question_"):

            question_id = key.split("_")[1]

            CandidateAnswer.objects.create(
                candidate=candidate,
                question_id=question_id,
                selected_answer=value
            )


    score = 0

    answers = CandidateAnswer.objects.filter(candidate=candidate)

    for answer in answers:
        if answer.selected_answer == answer.question.correct_answer:
            score += 1

    Result.objects.update_or_create(
        candidate=candidate,
        defaults={
            "score": score,
            "total_questions": answers.count(),
        }
    )

    request.session["test_submitted"] = True
    request.session.pop("question_ids", None)

    return redirect("result")



def result(request):

    candidate_id = request.session.get("candidate_id")

    if not candidate_id:
     
        return redirect("register")

    candidate = get_object_or_404(
        Candidate,
        id=candidate_id
    )

    result = get_object_or_404(
        Result,
        candidate=candidate
    )

    return render(
        request,
        "Test/result.html",
        {
            "candidate": candidate,
            "result": result
        }
    )


def finish(request):
    request.session.flush()
    return redirect("register")