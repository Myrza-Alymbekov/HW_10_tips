from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, QuestionAnswer
from .paginations import QAPagePagination
from .serializers import CategorySerializer, QuestionAnswerSerializer, QuestionDetailSerializer


class CategoryApiView(viewsets.ModelViewSet):
    """
        API для создания, получения, изменения и удаления категорий вопросов
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerApiView(generics.ListCreateAPIView):
    """
        API для создания и получения вопросов
    """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'question']
    ordering_fields = ['importance', ]
    pagination_class = QAPagePagination


class QuestionAnswerDetailApiView(viewsets.ModelViewSet):
    """
        API для детального просмотра и редактирвания вопросов
    """

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionDetailSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['category', 'question']
    ordering_fields = ['importance', ]
    pagination_class = QAPagePagination

