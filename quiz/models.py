from django.db import models


class Quiz(models.Model):
    quiz_id = models.PositiveIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=256, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    CHOICES = (
        ("Text", "Text response"),
        ("Single", "Single choice"),
        ("Multiple", "Multiple choice"),
    )
    question_id = models.PositiveIntegerField(unique=True, primary_key=True)
    text = models.CharField(max_length=256, blank=False)
    type = models.CharField(max_length=256, choices=CHOICES)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.PositiveIntegerField(unique=True, primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    answer = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.question.text
