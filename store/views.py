from django.shortcuts import render, redirect
from .models import Product, Order, OrderItem, Category
from django.contrib.auth.hashers import make_password

def home(request):

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(
        request,
        'store/home.html',
        context
    )
    

from django.shortcuts import get_object_or_404


def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )


    context = {

        'product': product

    }


    return render(
        request,
        'store/product_detail.html',
        context
    )
    

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

def register(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = User.objects.create_user(
            username=username,
            password=password
        )


        login(request, user)

        return redirect('home')


    return render(
        request,
        'store/register.html'
    )



def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user:

            login(request, user)

            return redirect('home')


    return render(
        request,
        'store/login.html'
    )



def user_logout(request):

    logout(request)

    return redirect('home')

def add_to_cart(request, id):

    cart = request.session.get('cart', {})


    if str(id) in cart:

        cart[str(id)] += 1

    else:

        cart[str(id)] = 1


    request.session['cart'] = cart


    return redirect('cart')

def cart(request):

    cart = request.session.get('cart', {})

    products = Product.objects.filter(
        id__in=cart.keys()
    )


    total = 0

    for product in products:

        total += product.price * cart[str(product.id)]


    context = {

        'products': products,
        'cart': cart,
        'total': total

    }


    return render(
        request,
        'store/cart.html',
        context
    )
    

def remove_from_cart(request, id):

    cart = request.session.get('cart', {})


    if str(id) in cart:

        del cart[str(id)]


    request.session['cart'] = cart


    return redirect('cart')

def checkout(request):

    cart = request.session.get('cart', {})


    products = Product.objects.filter(
        id__in=cart.keys()
    )


    total = 0


    for product in products:

        total += product.price * cart[str(product.id)]



    if request.method == "POST":


        customer_name = request.POST['customer_name']

        phone = request.POST['phone']

        address = request.POST['address']



        order = Order.objects.create(

            user=request.user,

            customer_name=customer_name,

            phone=phone,

            address=address,

            total_price=total

        )



        for product in products:


            OrderItem.objects.create(

                order=order,

                product=product,

                quantity=cart[str(product.id)],

                price=product.price

            )



        request.session['cart'] = {}



        return render(
            request,
            'store/order_success.html'
        )



    context = {

        'products': products,

        'total': total

    }



    return render(
        request,
        'store/checkout.html',
        context
    )
    
    
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')


    context = {

        'orders': orders

    }


    return render(
        request,
        'store/my_orders.html',
        context
    )
    
def update_cart(request, id, action):

    cart = request.session.get('cart', {})


    product_id = str(id)


    if product_id in cart:


        if action == "add":

            cart[product_id] += 1



        elif action == "remove":

            cart[product_id] -= 1



            if cart[product_id] <= 0:

                del cart[product_id]



    request.session['cart'] = cart


    return redirect('cart')

def products(request):

    products = Product.objects.all()


    context = {

        'products': products

    }


    return render(
        request,
        'store/products.html',
        context
    )
    
def about(request):

    return render(
        request,
        'store/about.html'
    )
    
def contact(request):

    return render(
        request,
        'store/contact.html'
    )
    
def search(request):

    query = request.GET.get('q')


    products = Product.objects.filter(
        name__icontains=query
    )


    context = {

        'products': products,

        'query': query

    }


    return render(
        request,
        'store/search.html',
        context
    )
    
def category_products(request, id):

    category = Category.objects.get(id=id)


    products = Product.objects.filter(
        category=category
    )


    context = {

        'category': category,

        'products': products

    }


    return render(
        request,
        'store/category_products.html',
        context
    )
    
