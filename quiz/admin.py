from django.contrib import admin
from quiz.models import Quiz, Question


class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'name', 'start_time', 'end_time', 'description')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question_id', 'text', 'type',)


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
