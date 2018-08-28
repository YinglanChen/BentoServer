from django.urls import path
from . import views

app_name = 'bento'
urlpatterns = [
    path('res/login/', views.restaurant_login),
    path('res/addmenu/', views.add_menu),
    path('res/deletemenu/', views.delete_menu),
    path('res/updatetp/', views.update_timeplace),
    path('res/currentorder/', views.lookup_current_order),
    path('res/allorder/', views.lookup_all_order()),

    path('cus/allmenu/', views.lookup_menu),
]




