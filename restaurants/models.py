from django.db import models

<<<<<<< HEAD
=======
class Order(models.Model):
    cus_id = models.CharField(max_length=50)
    pickup_location = models.CharField(max_length=20)
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)
    price = models.IntegerField()
    phone = models.IntegerField()
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.wechat_id

>>>>>>> 67344ae8c35c8902b457c6f3dac8601329da2cbf
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
