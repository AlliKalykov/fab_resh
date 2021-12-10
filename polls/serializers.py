from rest_framework import serializers

from .models import Quiz, Question, UserQuiz, Answer

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuizDetailSerializer(serializers.ModelSerializer):
    quiz_question = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class UserQuizSerializer(serializers.ModelSerializer):
    user_quiz = QuizSerializer

    class Meta:
        model = UserQuiz
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class UserQuizDetailSerializer(serializers.ModelSerializer):
    user_quiz = QuizSerializer
    user_quiz_answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = UserQuiz
        fields = '__all__'


class QuestionAnswerSerializer(serializers.Serializer):
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    answer = serializers.CharField(max_length=150)


class UserQuizCreateSerializer(serializers.Serializer):
    # TODO добавление авторизованного юзера
    # user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), allow_null=True)
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
    question_answer = QuestionAnswerSerializer(many=True)

    def validate(self, attrs):
        questions = Question.objects.filter(quiz=attrs["quiz"])

        sure_questions = questions.filter(sure=True)
        user_answer_questions = []

        for q_a in attrs['question_answer']:
            user_answer_questions.append(q_a['question'])
            if q_a['question'] not in questions:
                raise serializers.ValidationError(
                    detail='Check quiz questions',
                    code='quiz_question_id_is_incorrect'
                )

        for sure in sure_questions:
            if sure not in user_answer_questions:
                raise serializers.ValidationError(
                    detail='Please, ask sure questions',
                    code='ask_sure_questions'
                )

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user

        u_q = UserQuiz(quiz=validated_data.get('quiz'))
        u_q.save()

        if user.is_authenticated:
            u_q.user = UserProfile.objects.get(user=user)
            u_q.save()

        for q_a in validated_data.get('question_answer'):
            answer = Answer(user_quiz=u_q, question=q_a["question"], answer=q_a["answer"])
            answer.save()

        return u_q

    def to_representation(self, instance):

        return UserQuizDetailSerializer(instance, context=self.context).data
