from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Card(models.Model):
    name = models.CharField(max_length=200)
    dot = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

