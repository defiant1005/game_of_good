from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=55)

    def __str__(self):
        return f'ID {self.id}: {self.category}'
