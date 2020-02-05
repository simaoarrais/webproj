from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    cuisine = models.CharField(max_length=100)
    img = models.ImageField(upload_to="app/static/img", blank=True)

    def getById():
        query = Restaurant.objects.order_by("id")
        return query

    def getAll():
        query = Restaurant.objects.order_by("name")
        return query

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.CharField(max_length=70)

    def __str__(self):
        return self.first_name
