from django.contrib import admin
from .models import (
    Candidate,
    Category,
    Question,
    CandidateAnswer,
    Result
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "question", "correct_answer")
    list_filter = ("category",)
    search_fields = ("question",)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")


@admin.register(CandidateAnswer)
class CandidateAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "question", "selected_answer")
    list_filter = ("candidate",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "score", "total_questions", "created_at")
    search_fields = ("candidate__name",)