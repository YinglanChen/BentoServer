from django.http import HttpResponse
from django.core import serializers
from .models import *
from datetime import datetime
# Create your views here.


def foo(request):
    print(request)
    return HttpResponse("hello from foo")


# Restaurant
def restaurant_login(request):
    try:
        admin_id = int(request.GET['id'])
        restaurant = Restaurant.objects.get(admin_id=admin_id)
    except:
        return HttpResponse('-1')
    return HttpResponse(str(restaurant.pk))


def add_menu(request):
    try:
        restaurant_id = int(request.POST['id'])
        entree = request.POST['entree']
        side = request.POST['side']
        price = int(request.POST['price'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except:
        return HttpResponse('Invalid Parameters')
    menu = Menu()
    menu.restaurant = restaurant
    menu.entree = entree
    menu.side = side
    menu.price = price
    menu.save()
    return HttpResponse("Success")


def delete_menu(request):
    try:
        restaurant_id = int(request.POST['rid'])
        menu_id = int(request.POST['mid'])
        menu = Menu.objects.get(pk=menu_id)
    except:
        return HttpResponse('Invalid Parameter')
    if menu.restaurant.pk != restaurant_id:
        return HttpResponse('Invalid Parameter')
    menu.deleted = True
    menu.save()
    return HttpResponse('Success')


def update_timeplace(request):
    try:
        restaurant_id = int(request.POST['rid'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        tplist = request.POST.getlist('tp')
    except:
        return HttpResponse('Invalid Parameter')
    TimePlace.objects.filter(restaurant=restaurant).delete()
    for tp in tplist:
        elems = tp.split(',')
        obj = TimePlace()
        obj.restaurant = restaurant
        obj.time = elems[0]
        obj.place = elems[1]
        obj.save()
    return HttpResponse('Success')


def lookup_current_order(request):
    try:
        restaurant_id = int(request.GET['rid'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except:
        return HttpResponse('{}')
    orders = Order.objects.filter(restaurant=restaurant, deleted=False)
    return HttpResponse(serializers.serialize('json', orders))


def lookup_all_order(request):
    try:
        restaurant_id = int(request.GET['rid'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except:
        return HttpResponse('{}')
    orders = Order.objects.filter(restaurant=restaurant)
    return HttpResponse(serializers.serialize('json', orders))


# Customer
def lookup_restaurant(request):
    return HttpResponse(serializers.serialize('json', Restaurant.objects.all()))


def place_order(request):
    try:
        customer_id = request.POST['id']
        location = request.POST['location']
        phone = request.POST['phone']
        item_list = request.POST.getlist('items')
    except:
        return HttpResponse('Invalid Parameter')
    order = Order()
    order.cus_id = customer_id
    order.location = location
    order.phone = phone
    order.price = 0
    order.save()
    try:
        for item in item_list:
            elems = item.split(',')
            menu = Menu.objects.get(pk=int(elems[0]))
            order_item = OrderItem()
            order_item.menu = menu
            order_item.order = order
            order_item.amount = int(elems[1])
            order.price += order_item.amount * menu.price
    except:
        order.delete()
        return HttpResponse('Invalid Parameter')
    order.save()
    return HttpResponse('Success')


def lookup_customer_order(request):
    try:
        customer_id = request.GET['id']
    except:
        return HttpResponse('{}')
    return HttpResponse(serializers.serialize(Order.objects.filter(customer_id=customer_id)))


# General
def lookup_menu(request):
    try:
        restaurant_id = int(request.GET['id'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
    except:
        return HttpResponse('{}')
    menus = Menu.objects.filter(restaurant=restaurant, deleted=False)
    return HttpResponse(serializers.serialize('json', menus))


def order_detail(request):
    try:
        order_id = int(request.GET['id'])
        order = Order.objects.get(pk=order_id)
    except:
        return HttpResponse('{}')
    return HttpResponse(serializers.serialize('json', OrderItem.objects.filter(order=order)))
