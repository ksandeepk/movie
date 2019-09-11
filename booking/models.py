from django.db import models

# Create your models here.
class udata(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)

class movie(models.Model):
    lang_choice=(
            ('ENGLISH','English'),
            ('HINDI','Hindi'),
            ('TAMIL','Tamil'),
            ('TELUGU','Telugu'),
            ('MALAYALAM','Malayalam'),
            ('KANNADA','Kannada'),
            
        )
    movie_name=models.CharField(max_length=120)
    cast=models.CharField(max_length=200)
    director=models.CharField(max_length=120)
    language=models.CharField(max_length=20,choices=lang_choice)
    image=models.ImageField(upload_to='images/')

class theatre(models.Model):
    theatre_name=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

class confirm(models.Model):
    ticket_id=models.CharField(max_length=20)
    movie_name=models.CharField(max_length=50)
    theatre_name=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=20)
    seat=models.CharField(max_length=20)
        