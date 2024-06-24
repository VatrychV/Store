from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import AnonymousUser
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import JsonResponse
from .forms import CreateUserForm
from django.conf import settings
from django.views import View
import stripe
import json
from django.utils import timezone



stripe.api_key = settings.STRIPE_SECRET_KEY



def dec_auth_products(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = request.user.customer  
            order, created = Order.objects.get_or_create(customer=customer, complete=True)
            items = order.orderitem_set.all()
        else:
           
            items = []
            order = {'get_cart_total' : 0, 'get_total_items' : 0 }

        response = func(request, order=order, items=items, *args, **kwargs)
        return response
    return wrapper


def dec_add_categories_and_products(func):
    def wrapper(request, *args, **kwargs):
        categories = Category.objects.all()
        products = Product.objects.all()

        response = func(request, categories=categories, products=products, *args, **kwargs)

        return response

    return wrapper



# home
@dec_auth_products
@dec_add_categories_and_products
def index(request,order,items, categories, products):
        context = {
            'order': order,'items': items,
            'categories' : categories,
            'products': products,
            }
        return render(request, 'main/index.html', context)

    
@dec_auth_products
@dec_add_categories_and_products
def checkout(request,order,items, categories, products):
        context = {
                'order': order,'items': items,
                'categories' : categories,
                'products': products,
                }
        return render(request, 'main/checkout.html', context)


@dec_auth_products
@dec_add_categories_and_products
def women(request,order,items,categories,products):
        context = {
            'order' : order,'items': items,
            'categories' : categories,
            'products' : products.filter(category__name ='Women'),
            }
        return render(request, 'main/women.html', context)

@dec_auth_products
@dec_add_categories_and_products
def men(request,order,items,categories,products):
        context = {   
            'order' : order,'items': items,
            'categories' : categories,
            'products' : products.filter(category__name ='Men'),
            }
        return render(request, 'main/men.html', context)

@dec_auth_products
@dec_add_categories_and_products
def products(request,order,items,categories,products):
        context = {
            'order' : order,'items': items,
            'categories' : categories,
            'products' : products
            }
        return render(request, 'main/products.html', context)


@dec_auth_products
def single(request,order,items,product_id):
        product = get_object_or_404(Product, id=product_id)
        sizes = Product.objects.filter(name=product.name).values_list('size', flat=True).distinct()
        
        context = {
            'order' : order,'items': items,
            'product': product,'sizes': sizes,
        }
        return render(request, 'main/single.html', context)

from .forms import buy_and_shipForm


# DECORATOR_POST_METHOD_FOR_CARD_AD
def order_view(func):
    def wrapper(request, *args, **kwargs):
        if request.method == 'POST':
            form = buy_and_shipForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('stripee.html')  # Редірект на сторінку успіху
        else:
            form = buy_and_shipForm()

        kwargs['form'] = form  # Додаємо форму до kwargs
        response = func(request, *args, **kwargs)
        return response
    return wrapper

# CARD_AD
@dec_auth_products
@order_view
def cart_ad(request, order, items, form):  # Додаємо параметр form
    total = order.get('get_cart_total') if isinstance(order, dict) else order.get_cart_total()
    context = {
        'order': order,
        'items': items,
        'total': total,  
        'form': form
    }
    context['key'] = settings.STRIPE_PUBLIC_KEY
    return render(request, 'main/cart_ad.html', context)

def stripee(request):
        if request.user.is_authenticated:
            customer = request.user.customer  
            order, created = Order.objects.get_or_create(customer=customer, complete=True)
            items = order.orderitem_set.all()
        else:   
            items = []
            order = {'get_cart_total' : 0, 'get_total_items' : 0 }
        context = {
            'order': order,'items': items,
            }
        context['key'] = settings.STRIPE_PUBLIC_KEY
        return render(request, 'main/stripee.html', context)









def logout_view(request):
    logout(request) 
    return redirect('index.html')



from django.core.mail import send_mail
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


@dec_auth_products
def contact(request, order, items):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            email = form.cleaned_data.get('email', '')
            number = form.cleaned_data.get('number', '')
            message = form.cleaned_data.get('message', '')
            
            # Создание объекта Contact и установка значения для date_created
            contact = form.save(commit=False)
            contact.date_created = timezone.now()
            contact.save()

            subject = f'Інформація з форми від {name}'
            message_body = f'Ім\'я: {name}\nEmail: {email}\nНомер телефону: {number}\nПовідомлення: {message}'
            try:
                send_mail(subject, message_body, 
                        'YourFashion@gmail.com',
                        ['markizkit3@gmail.com'])
                return redirect("main:index")
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
    else:
        form = ContactForm()
    context = {'items': items ,'order' : order, 'form': form }
    return render(request, 'main/contact.html', context)




# Register
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request, f'Account was created for {user.username}')
            return redirect('account.html')  # Ім'я URL для перенаправлення після успішної реєстрації
             
    context = {'form': form}
    return render(request, 'main/register.html', context)


#LogIN
@dec_auth_products
def account(request, order, items):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                customer = Customer.objects.get_or_create(user=user)
                login(request, user)
                messages.success(request, 'You are now logged in')
                
                # Перенаправлення на головну сторінку після входу
                return redirect('index.html')  # або інший URL головної сторінки
            except Customer.DoesNotExist:
                messages.error(request, 'Customer does not exist')

    context = {'order':order}
    return render(request, 'main/account.html', context)


# updateItem in cart
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Product:', productId)
    
    customer = None
    if request.user != AnonymousUser():
        customer = request.user.customer
    product = Product.objects.get(id=productId)
    
    if customer:
        order, created = Order.objects.get_or_create(customer=customer, complete=True)
    else:
        order = Order.objects.create(complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1) if orderItem.quantity else 1
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1) if orderItem.quantity > 0 else 0
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added ', safe=False)


class SuccessView(TemplateView):
     template_name = 'main/success.html'

class CancelView(TemplateView):
    template_name = 'main/cancel.html'

