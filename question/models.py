from django.db import models
from django.contrib.auth.models import User

from categories.models import Categories


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255, blank=True)
    incorrect_answer1 = models.CharField(max_length=255, blank=True)
    incorrect_answer2 = models.CharField(max_length=255, blank=True)
    incorrect_answer3 = models.CharField(max_length=255, blank=True)
    correct_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'ID {self.id}: {self.title}'
