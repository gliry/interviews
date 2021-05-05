from django.contrib import admin
from quiz.models import Quiz, Question, Answer


class QuizAdmin(admin.ModelAdmin):
    list_display = ("quiz_id", "name", "start_time", "end_time", "description")


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "quiz",
        "question_id",
        "text",
        "type",
    )


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "quiz",
        "question",
        "answer",
    )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
