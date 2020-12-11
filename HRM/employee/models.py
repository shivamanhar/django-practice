from django.db import models
import datetime

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    #return self.pub_date >= timezone.now()- datetime.timedelta(days =1)


class Choice(models.Model):
    question =models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text= models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text

class Employes(models.Model):
    name = models.CharField(max_length=60)
    post = models.CharField(max_length=10)
    gender = models.TextChoices('Male', 'Female')

class Sudent(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE ='SO'
    JUNIOR = 'JS'
    SENIOR = 'SR'
    GRADUATE ='GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR,'Junior'),
        (GRADUATE, 'Graduate')
    ]

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    school_name = models.CharField(max_length=10,null=True,blank=True)

    def issubclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}