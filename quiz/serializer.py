from rest_framework import serializers
from .models import *


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'question','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz','question','answer',
        ]
