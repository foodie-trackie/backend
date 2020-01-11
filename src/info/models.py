from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField()
    production_date = models.DateField()
    shelf_life = models.IntegerField()
    expiration_date = models.DateField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.name
