from django.db import models

class ContactData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=100)
class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.IntegerField()
    date = models.DateTimeField()
    feedback = models.CharField(max_length=500)
class ServicesData(models.Model):
    cno = models.IntegerField()
    cname = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    fees = models.IntegerField()
    content = models.FileField(upload_to='files')
    def __str__(self):
        return self.cname

