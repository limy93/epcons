from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.conf import settings
from .models import CountryData, CountryMetadata, Purchase
from .forms import RegisterForm  # Assuming you have a custom registration form

def home(request):
    """ Render the home page. """
    return render(request, 'home.html')

def list_countries(request):
    country_code = request.GET.get('country_code')
    if country_code:
        return redirect('country_detail', country_code=country_code)
    countries = CountryData.objects.all()
    return render(request, 'list_countries.html', {'countries': countries})

def country_detail(request, country_code):
    country = get_object_or_404(CountryData, country_code=country_code)
    metadata = get_object_or_404(CountryMetadata, country=country)
    return render(request, 'country_detail.html', {
        'country': country,
        'metadata': metadata
    })

def login_required_message(function):
    """ Decorator to display a message if the user is not authenticated. """
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Check if the specific message is already in the messages storage
            if not any(message.message == "Please log in to proceed with purchasing." for message in messages.get_messages(request)):
                messages.info(request, "Please log in to proceed with purchasing.")
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return function(request, *args, **kwargs)
    return wrapper

@login_required
def dashboard(request):
    if request.user.is_superuser:
        active_users_count = User.objects.filter(is_active=True).count()
        total_orders_count = Purchase.objects.count()
        recent_orders = Purchase.objects.all().order_by('-purchase_date')[:10]
        return render(request, 'dashboard.html', {
            'active_users_count': active_users_count,
            'total_orders_count': total_orders_count,
            'recent_orders': recent_orders
        })
    else:
        purchases = Purchase.objects.filter(user=request.user).order_by('-purchase_date')
        return render(request, 'dashboard.html', {'purchases': purchases})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required_message
def purchase_view(request, country_code):
    country = get_object_or_404(CountryData, country_code=country_code)
    if request.method == 'POST':
        purchase = Purchase(
            user=request.user,
            country=country,
            price=100.00  # Assuming a fixed price
        )
        purchase.save()
        return redirect('dashboard')
    return render(request, 'purchase.html', {'country': country})

@login_required_message
def confirm_purchase(request, country_code):
    country = get_object_or_404(CountryData, country_code=country_code)
    if request.method == 'POST':
        purchase = Purchase(
            user=request.user,
            country=country,
            price=100.00  # Assuming a fixed price
        )
        purchase.save()
        return redirect('dashboard')
    return redirect('purchase_view', country_code=country_code)