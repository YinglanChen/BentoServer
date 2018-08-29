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
        admin_id = request.GET['id']
        restaurant = Restaurant.objects.get(admin_id=admin_id)
    except:
        return HttpResponse('-1')
    return HttpResponse(str(restaurant.pk))


def add_menu(request):
    try:        
        restaurant_id = int(request.GET['id'])
        entree = request.GET['entree']
        side = request.GET['side']
        price = int(request.GET['price'])
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
        restaurant_id = int(request.GET['rid'])
        menu_id = int(request.GET['mid'])
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
        restaurant_id = int(request.GET['rid'])
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        tplist = request.GET.getlist('tp')
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
        customer_id = request.GET['cid']
        res_id = int(request.GET['rid'])
        location = request.GET['location']
        phone = request.GET['phone']
        item_list = request.GET.getlist('items')
        restaurant = Restaurant.objects.get(pk=res_id)
    except:
        return HttpResponse('Invalid Parameter')
    order = Order()
    order.cus_id = customer_id
    order.restaurant = restaurant
    order.location = location
    order.phone = phone
    order.price = 0
    order.save()
    try:
        if len(item_list) == 0:
            raise Exception('Invalid Items')
        for item in item_list:
            elems = item.split(',')
            menu = Menu.objects.get(pk=int(elems[0]))
            if menu.restaurant != restaurant or menu.deleted:
                raise Exception('Invalid Menus')
            order_item = OrderItem()
            order_item.menu = menu
            order_item.order = order
            order_item.amount = int(elems[1])
            order_item.save()
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
    return HttpResponse(serializers.serialize('json', Order.objects.filter(cus_id=customer_id)))


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
