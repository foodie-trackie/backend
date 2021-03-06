from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)
    number = models.IntegerField()
    production_date = models.DateField()
    shelf_life = models.IntegerField()
    expiration_date = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
