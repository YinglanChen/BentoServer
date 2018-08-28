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
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    phone = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    amount = models.IntegerField()


class TimePlace(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
