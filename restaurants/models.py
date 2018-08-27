from django.db import models


class Restaurant(models.Model):
    res_name = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=50)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    entree = models.CharField(max_length=20)
    side = models.CharField(max_length=50)
    price = models.IntegerField()
    deleted = models.BooleanField(default=False)


class Order(models.Model):
    cus_id = models.CharField(max_length=50)
    timeplace = models.ForeignKey('TimePlace', on_delete=models.CASCADE)
    order = models.ForeignKey('OrderItem', on_delete=models.CASCADE)
    price = models.IntegerField()
    phone = models.IntegerField()
    deleted = models.BooleanField(default=False)


class OrderItem(models.Model):
    order_id = models.IntegerField()
    menu = models.ForeignKey('Menu', on_delte=models.CASCADE)
    amount = models.IntegerField()
    deleted = models.BooleanField(default=False)


class TimePlace(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
