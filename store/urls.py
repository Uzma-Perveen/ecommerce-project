from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,              name='home'),
    path('register/',               views.register_view,     name='register'),
    path('login/',                  views.login_view,        name='login'),
    path('logout/',                 views.logout_view,       name='logout'),
    path('product/<int:pk>/',       views.product_detail,    name='product_detail'),
    path('cart/',                   views.cart_view,         name='cart'),
    path('cart/add/<int:pk>/',      views.add_to_cart,       name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('cart/remove/<int:item_id>/',   views.remove_item,       name='remove_item'),
    path('checkout/',               views.checkout,          name='checkout'),
    path('order/success/<int:pk>/', views.order_success,     name='order_success'),
    path('orders/',                 views.order_history,     name='order_history'),
    path('orders/<int:pk>/',        views.order_detail,      name='order_detail'),
]