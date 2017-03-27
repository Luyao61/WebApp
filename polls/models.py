from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published');

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class EyewitnessStimuli(models.Model):
    CONFIDENCE_SCORE = ( 60, 80, 100, )
    LINEUP_RACE = ('B', 'W', )
    LINEUP_NUMBER = (
        'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
        'W1', 'W2', 'W3', 'W4', 'W5', 'W6',
    )
    CATEGORY = ('O1', 'Omany', 'R', 'U1', 'F', )
    CHOICE = (1,2,3,4,5,6)

    score = models.IntegerField(choices=CONFIDENCE_SCORE)
    lineup_race = models.CharField(max_length=1, choices=LINEUP_RACE)
    lineup_number = models.CharField(max_length=2, choices=LINEUP_NUMBER)
    category = models.CharField(max_length=10, choices=CATEGORY)
    statement = models.TextField(max_length=100)
    chosen_face = models.PositiveSmallIntegerField(choices=CHOICE)
    lineup_order = models.CharField(max_length=14)

