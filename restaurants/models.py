from django.db import models

class Restaurant(models.Model):
    res_name = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=50)
    def __str__(self):
        return self.res_name

class Menu(models.Model):
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    entry = models.CharField(max_length=20)
    side = models.CharField(max_length=50)
    price = models.IntegerField()

class Order(models.Model):
    cus_id = models.CharField(max_length=50)
    pickup_location = models.CharField(max_length=20)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.IntegerField()
    phone = models.IntegerField()
    def __str__(self):
        return self.cus_id

class TimePlace(models.Model):
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
