from django.db import models

class Restaurant(models.Model):
    res_name = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=50)
    def __str__(self):
        return self.res_name

class Menu(models.Model):
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    entree = models.CharField(max_length=20)
    side = models.CharField(max_length=50)
    price = models.IntegerField()
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.res_id

class Order(models.Model):
    cus_id = models.CharField(max_length=50)
    pickup_location = models.CharField(max_length=20)
    order_id = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    price = models.IntegerField()
    phone = models.IntegerField()
    def __str__(self):
        return self.cus_id

class OrderItem(models.Model):
    order_id = models.IntegerField(primary_key=true)
    menu_id = models.ForeignKey(Menu, on_delte=models.CASCADE)
    amount - models.IntegerField()
    def __str__(self):
        return self.order_id

class TimePlace(models.Model):
    res_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    time = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    def __str__(self):
        return self.res_id
