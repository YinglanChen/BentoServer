from django.urls import path
from . import views

app_name = 'alphalunch'
urlpatterns = [
    path('res/login/', views.restaurant_login),
    path('res/addmenu/', views.add_menu),
    path('res/deletemenu/', views.delete_menu),
    path('res/updatetp/', views.update_timeplace),
    path('res/currentorder/', views.lookup_current_order),
    path('res/allorder/', views.lookup_all_order),

    path('cus/restaurant/', views.lookup_restaurant),
    path('cus/placeorder/', views.place_order),
    path('cus/allorder/', views.lookup_customer_order),

    path('general/allmenu/', views.lookup_menu),
    path('general/orderdetail/', views.order_detail)
]




