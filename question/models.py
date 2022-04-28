from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255, blank=True)
    incorrect_answer1 = models.CharField(max_length=255, blank=True)
    incorrect_answer2 = models.CharField(max_length=255, blank=True)
    incorrect_answer3 = models.CharField(max_length=255, blank=True)
    correct_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'ID {self.id}: {self.title}'
