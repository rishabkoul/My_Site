from django.db import models
from django.utils import timezone


class Resume(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    address = models.TextField(blank=True)
    mail = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.mail


class Education(models.Model):
    institute = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.institute


class Skills(models.Model):
    name = models.CharField(max_length=255, unique=True)
    level = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    p_type = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Achievements(models.Model):

    name = models.CharField(max_length=255, unique=True)
    link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    a_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.email
