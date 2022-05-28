from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from question.models import Question
from question.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['title']
    search_fields = ['title', 'correct_answer']
    ordering_fields = ['title']
