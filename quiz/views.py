from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from rest_framework import generics
from rest_framework.response import Response

from quiz.models import Answer, Quiz, Question
from quiz.serializers import AnswerSerializer, QuizSerializer, QuestionSerializer


class AnswerCreateView(View):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def post(self, request, *args, **kwargs):
        """
        Requesting data for adding answer in system. Available at the link answers/
        :param request: requesting data, JSON. Looks like: {"user_id": int, "quiz": int, "question": int, "answer": str}
        :param args: unpacking arguments
        :param kwargs: unpacking named arguments
        :return: Response with requested data
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class QuizCreateView(View):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request):
        """
        return available quizs if they exists, else return HTTPResponse.
        """
        list_active_quizs = []
        time = timezone.now()
        quizs = Quiz.objects.all()
        for object in quizs:
            if object.end_time >= time:  # Is quiz available?
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
        """
        Show all user's quiz with some data
        :param pk: user's id
        :return: list of user's data
        """
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
