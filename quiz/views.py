from django.shortcuts import render, get_object_or_404
import datetime
from django.utils import timezone
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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class QuizCreateView(View):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request):
        list_active_quizs = []
        time = timezone.now()
        quizs = Quiz.objects.all()
        for object in quizs:
            if object.end_time >= time:
                list_active_quizs.append(object)

        if list_active_quizs:
            return render(
                request, "quizs.quiz_list.html", {"quiz_list": list_active_quizs}
            )
        else:
            return HttpResponse("Нет активных опросов")


class QuestionCreateView(View):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, pk):
        answers = Answer.objects.filter(user_id=pk)
        list_data = []
        for elem in answers:
            quiz = elem.quiz
            question = elem.question
            user_id = elem.user_id
            answer = elem.answer
            data = {
                "quiz": quiz,
                "question": question,
                "user_id": user_id,
                "answer": answer,
            }
            list_data.append(data)

        return HttpResponse(list_data)
