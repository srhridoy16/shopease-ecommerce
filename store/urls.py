from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path(
        'product/<int:id>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),
    
    path(
    'add-cart/<int:id>/',
    views.add_to_cart,
    name='add_to_cart'
),


path(
    'cart/',
    views.cart,
    name='cart'
),


path(
    'remove-cart/<int:id>/',
    views.remove_from_cart,
    name='remove_from_cart'
),
path(
    'checkout/',
    views.checkout,
    name='checkout'
),
path(
    'my-orders/',
    views.my_orders,
    name='my_orders'
),
path(
    'update-cart/<int:id>/<str:action>/',
    views.update_cart,
    name='update_cart'
),
path(
    'products/',
    views.products,
    name='products'
),
path(
    'about/',
    views.about,
    name='about'
),
path(
    'contact/',
    views.contact,
    name='contact'
),
path(
    'search/',
    views.search,
    name='search'
),
path(
    'category/<int:id>/',
    views.category_products,
    name='category_products'
),

]