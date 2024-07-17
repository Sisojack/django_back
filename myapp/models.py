from django.db import models

# Create your models here.
class People(models.Model):
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField()
    age= models.IntegerField(null= True, blank=True)
    def __str__(self):
        return self.first_name + '' + self.last_name
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length= 13)
    course = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.name