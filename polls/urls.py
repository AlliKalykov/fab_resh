from django.urls import path
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status

from .serializers import UserQuizCreateSerializer, UserQuizDetailSerializer
from .views import QuizListCreateView, QuizDetailView, UserQuizListCreateView, UserQuizDetailView, \
    QuestionListCreateView, QuestionDetailView


decorated_user_quiz_view = \
   swagger_auto_schema(
      method='post',
      request_body=UserQuizCreateSerializer,
      responses={status.HTTP_200_OK: UserQuizDetailSerializer}
   )(UserQuizListCreateView.as_view())

urlpatterns = [
    # gets all user quiz and create a new quiz
    path('quiz/', QuizListCreateView.as_view(), name='all-quiz'),
    # retrieves quiz details
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),

    path('user-quiz/', decorated_user_quiz_view, name='all-user-quiz'),
    path('user-quiz/<int:pk>/', UserQuizDetailView.as_view(), name='user-quiz-detail'),

    path('question/', QuestionListCreateView.as_view(), name='all-questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),

]
