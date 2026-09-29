import csv
from django.core.management.base import BaseCommand
from Test.models import Category, Question


class Command(BaseCommand):
    help = "Import questions from CSV"

    def handle(self, *args, **kwargs):
        with open("questions.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                category, _ = Category.objects.get_or_create(
                    name=row["category"]
                )

                question, created = Question.objects.get_or_create(
                    category=category,
                    question=row["question"],
                    defaults={
                        "option1": row["option1"],
                        "option2": row["option2"],
                        "option3": row["option3"],
                        "option4": row["option4"],
                        "correct_answer": row["correct_answer"],
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f"Added: {row['question']}")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Skipped: {row['question']}")
                    )

        self.stdout.write(
            self.style.SUCCESS("Import completed successfully!")
        )