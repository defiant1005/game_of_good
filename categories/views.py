from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from categories.models import Categories
from categories.serializers import CategoriesSerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
