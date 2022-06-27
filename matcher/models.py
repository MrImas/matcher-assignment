from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Candidate(models.Model):
    skill = models.ManyToManyField(Skill)
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Job(models.Model):
    skill = models.ManyToManyField(Skill)
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
