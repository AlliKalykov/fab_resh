from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Quiz, UserQuiz, Question

from .serializers import QuizSerializer, QuizDetailSerializer, UserQuizSerializer, UserQuizDetailSerializer,\
    UserQuizCreateSerializer, QuestionSerializer

from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from drf_yasg2 import openapi


class QuizListCreateView(ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuizDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer


class UserQuizListCreateView(ListCreateAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserQuizSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):

        serializer = UserQuizCreateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserQuizDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizDetailSerializer


class QuestionListCreateView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('quiz', 'sure')


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
