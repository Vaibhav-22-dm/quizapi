from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    roll = models.CharField(max_length=400, blank=True, null=True)
    department = models.CharField(max_length=400, blank=True, null=True)
    course = models.CharField(max_length=400, null=True, blank=True)
    college = models.CharField(max_length=400, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Test(models.Model):
    subjects = [
        ('P', 'Physics'),
        ('C', 'Chemistry'),
        ('M', 'Mathematics'),
        ('B', 'Biology'),
        ('E', 'English')
    ]
    numberOfQuestions = models.IntegerField(null=True, blank=True)
    time = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=200, choices=subjects, default='P')
    title = models.CharField(max_length=200, null=True, blank=True)
    creator = models.ForeignKey(User, null=True, blank=True, related_name='creator', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '(' + self.subject + ')'

class Question(models.Model):
    subjects = [
        ('P', 'Physics'),
        ('C', 'Chemistry'),
        ('M', 'Mathematics'),
        ('B', 'Biology'),
        ('E', 'English')
    ]
    question = models.CharField(max_length=200, null=True, blank=True)
    answer = models.TextField(blank=True, null=True)
    uniqueID = models.UUIDField(default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=200, choices=subjects, default='P')
    test = models.ForeignKey(Test, null=True, blank=True, related_name='test', on_delete=models.CASCADE)

    def __str__(self):
        return self.question



