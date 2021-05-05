from django.shortcuts import render, get_object_or_404
import datetime
from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from quiz.models import Answer, Quiz, Question
from quiz.serializers import AnswerSerializer, QuizSerializer, QuestionSerializer


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def post(self, request, *args, **kwargs):
        pass


class QuizCreateView(View):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request):
        list_active_quizs = []
        quizs = Quiz.objects.all()
        for object in quizs:
            if object.start_time <= object.end_time:
                print(object.start_time > object.end_time)
                list_active_quizs.append(object)

        if list_active_quizs:
            return render(
                request, "quizs.quiz_list.html", {"quiz_list": list_active_quizs}
            )
        else:
            return HttpResponse("Нет активных опросов")


class QuestionCreateView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self):
        pass
