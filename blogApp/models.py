from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class User(models.Model):
    user_name = models.CharField(max_length=50)
    age = models.IntegerField(default=10)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

    def calc(self, x, y):
        return x <= 5 <= y


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # 下面3行是为了在后台设置（admin.py）list_display更加友好的展示 was_published_recently 此列
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text