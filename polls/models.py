from django.db import models

from accounts.models import UserProfile


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=300)
    sure = models.BooleanField(default=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, related_name='quiz_question')

    def __str__(self):
        return self.name


class UserQuiz(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='quiz', null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, related_name='user_quiz')
    pass_date = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    user_quiz = models.ForeignKey(UserQuiz, on_delete=models.PROTECT, related_name='user_quiz_answer')
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='question_for_answer')
    answer = models.CharField(max_length=150)

    def __str__(self):
        return self.answer
