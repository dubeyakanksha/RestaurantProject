from django.db import models

class Starter(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Salad(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Specialty(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class table(models.Model):                             #booktable
    name =models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    phone =models.CharField(max_length=12)
    date =models.DateTimeField()
    persons = models.IntegerField()
    message = models.TextField()

class response(models.Model):                         #contact
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    message = models.TextField()


class program(models.Model):                         #events
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.DateTimeField()
    event = models.CharField(max_length=150)
    persons = models.IntegerField()