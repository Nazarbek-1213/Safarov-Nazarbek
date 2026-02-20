from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=160, blank=True)  # masalan: Backend Developer
    location = models.CharField(max_length=120, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    about = models.TextField(blank=True)
    

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    instagram=models.URLField(blank=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=80)
    level = models.PositiveSmallIntegerField(default=70)  # 0..100

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    github = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=200, blank=True)  

    def __str__(self):
        return self.name


class Education(models.Model):
    university=models.CharField(max_length=10)
    place = models.CharField(max_length=160)
    program = models.CharField(max_length=160, blank=True)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-start_year"]

    def __str__(self):
        return self.place