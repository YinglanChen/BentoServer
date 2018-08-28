from django.http import HttpResponse
from django.core import serializers
from .models import *
from datetime import datetime
# Create your views here.


def foo(request):
    print(request)
    return HttpResponse("hello from foo")


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


def lookup_menu(request):
    try:
        restaurant_id = int(request.GET['id'])
    except:
        return HttpResponse('{}')
    menus = Menu.objects.filter(restaurant_id=restaurant_id, deleted=False)
    return HttpResponse(serializers.serialize('json', menus))


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
