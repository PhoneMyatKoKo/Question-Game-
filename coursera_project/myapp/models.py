from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=100,verbose_name='menu_name')
    price=models.IntegerField()

    def __str__(self):
        return self.name
