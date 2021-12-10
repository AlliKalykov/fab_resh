from django.contrib import admin

from .models import Quiz, Question, UserQuiz, Answer


admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserQuiz)
admin.site.register(Answer)

