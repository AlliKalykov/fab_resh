from django.urls import path

from .views import QuizListCreateView, QuizDetailView, UserQuizListCreateView, UserQuizDetailView


urlpatterns = [
    # gets all user quiz and create a new quiz
    path('quiz/', QuizListCreateView.as_view(), name='all-quiz'),
    # retrieves quiz details
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz-detail'),

    path('user-quiz/', UserQuizListCreateView.as_view(), name='all-users-quiz'),
    path('user-quiz/<int:pk>/', UserQuizDetailView.as_view(), name='user-quiz-detail'),

    # path('quiz/', QuizListCreateView.as_view(), name='all-quiz'),

]
