from django.db import models

# Create your models here.

class Buyer(models.Model):
    '''
    Buyer model
    '''
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=2, max_digits=7)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name



class Game(models.Model):
    '''
    Game model
    '''
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    size = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers', blank=True)

    def __str__(self) -> str:
        return self.title
