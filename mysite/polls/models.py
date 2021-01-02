import datetime

from django.db import models
from django.utils import timezone



class Question(models.Model):
  title = models.CharField(max_length=200)
    link = models.URLField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):  # __unicode__ on Python 2
        return self.choice_text