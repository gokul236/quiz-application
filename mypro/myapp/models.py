from django.db import models
class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    status=models.CharField(max_length=50)
class register(models.Model):
    username=models.CharField(max_length=30)
    phonenumber=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    photo = models.FileField()
    qualification=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirmpassword=models.CharField(max_length=30)
class questionstable(models.Model):
    questionid=models.IntegerField(max_length=30)
    question=models.CharField(max_length=3000)
    optiona=models.CharField(max_length=300)
    optionb=models.CharField(max_length=300)
    optionc=models.CharField(max_length=300)
    optiond=models.CharField(max_length=300)
    correctanswer=models.CharField(max_length=300)
    category=models.CharField(max_length=300)
