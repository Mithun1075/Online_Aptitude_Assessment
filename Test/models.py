from django.db import models


class Candidate(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    mobile = models.CharField(max_length=15, unique=True)

    college_name = models.CharField(max_length=200)

    degree = models.CharField(max_length=100)

    year_of_passing = models.PositiveIntegerField()

    position = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="questions"
    )
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return self.question[:50]


class CandidateAnswer(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    selected_answer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.candidate.name} - Q{self.question.id}"


class Result(models.Model):
    candidate = models.OneToOneField(
        Candidate,
        on_delete=models.CASCADE
    )
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.name} - {self.score}/{self.total_questions}"