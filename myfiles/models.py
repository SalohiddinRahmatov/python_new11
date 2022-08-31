from django.db import models

# Create your models here.
class Type(models.Model):
    nomi=models.CharField(max_length=20)
    def __str__(self):
        return self.nomi


class Maxsulotlar(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class Project(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class Project1(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class Services(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class About(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class Blog(models.Model):
    nomi=models.CharField(max_length=40)
    malumot=models.TextField()
#    rasm=models.ImageField(upload_to='media')
    tur=models.ForeignKey(Type , on_delete=models.CASCADE,)
    vaqt=models.DateTimeField(auto_now=True)

class Murojat(models.Model):
    ism=models.CharField(max_length=40)
    fam=models.CharField(max_length=40)
#    rasm=models.ImageField(upload_to='media')
    mail=models.EmailField()
    text=models.TextField()
    vaqt=models.DateTimeField(auto_now=True)

class Gmail(models.Model):
    gmail=models.EmailField()