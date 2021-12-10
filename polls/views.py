from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Quiz, UserQuiz, Answer

from .serializers import QuizSerializer, QuizDetailSerializer, UserQuizSerializer, UserQuizDetailSerializer,\
    UserQuizCreateSerializer


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

    # def perform_create(self, serializer):
    #     if self.request.user:
    #         serializer.save(user=self.request.user)


class UserQuizDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserQuiz.objects.all()
    serializer_class = UserQuizDetailSerializer
