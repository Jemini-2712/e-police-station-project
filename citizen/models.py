from django.db import models

#from secrets import choice

# Create your models here.

class User(models.Model):
    choice = [('Gujarat','Gujarat'),('Maharastra','Maharastra'),('U.P','U.P'),('M.P','M.P'),('A.P','A.P')]
    
    uname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    state = models.CharField(max_length=50,choices=choice)


    def __str__(self):
        return self.email



class Feedback(models.Model):

    fpname = models.CharField(max_length=30)
    fphone = models.CharField(max_length=20)
    feedback = models.TextField()

    def __str__(self):
        return self.fpname