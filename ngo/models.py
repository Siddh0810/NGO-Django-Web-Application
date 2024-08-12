from django.db import models

# Create your models here.
class teamMember(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Address = models.CharField(max_length=250)
    BirthDate = models.DateField()

    def _str_(self):
        return self.Name

class Donation(models.Model):
    Name = models.CharField(max_length=200)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Address = models.CharField(max_length=250)
    Amount = models.IntegerField()

    def __str__(self):
        return self.Name
    
class Review(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Text = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
    

