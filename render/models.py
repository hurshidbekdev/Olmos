from django.db import models
# Create your models here.
class trenajerlar(models.Model):
    nomi=models.CharField(max_length=60)
    rasmi=models.ImageField(upload_to='')
    ishlash=models.TextField(max_length=100)
    def __str__(self):
        return self.nomi
class quljangi(models.Model):
    title=models.CharField(max_length=60)
    rasm=models.ImageField(upload_to='model/model/')
    haqida=models.TextField(max_length=1000)
    def __str__(self):
        return self.title
class bodybuild(models.Model):
    title=models.CharField(max_length=60)
    rasm=models.ImageField(upload_to='media/media/')
    haqida=models.TextField(max_length=1000)
    def __str__(self):
        return self.title
class fitnes(models.Model):
    title=models.CharField(max_length=60)
    rasm=models.ImageField(upload_to='media/media/')
    haqida=models.TextField(max_length=1000)
    def __str__(self):
        return self.title

class OlmosVideo(models.Model):
    title=models.CharField(max_length=60)
    video_url=models.FileField(upload_to='media/media/')
    def __str__(self):
        return self.title

class JamoaOlmos(models.Model):
    title=models.CharField(max_length=60)
    rasm=models.ImageField(upload_to='')
    nomer=models.CharField(max_length=40)
    facebook = models.URLField(max_length=1024)
    instagram = models.URLField(max_length=1024)
    telegram = models.URLField(max_length=1024)
    def __str__(self):
        return self.title

class MashqVideo(models.Model):
    title=models.CharField(max_length=60)
    image=models.ImageField(upload_to='media/media/')
    def __str__(self):
        return self.title

class Video3Etaj(models.Model):
    title=models.CharField(max_length=60)
    video=models.FileField(upload_to='media/media/')
    def __str__(self):
        return self.title

class Marosim(models.Model):
    title=models.CharField(max_length=100)
    video=models.FileField(upload_to='media/media/')
    def __str__(self):
        return self.title







