from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RegisterForm
from .models import CountryData, CountryMetadata, ElectricConsumption, Purchase

def home(request):
    """Render the home page."""
    return render(request, 'home.html')

def list_countries(request):
    """Display a list of countries. Optionally filter by country code from query."""
    country_code = request.GET.get('country_code')
    if country_code:
        return redirect('country_detail', country_code=country_code)
    countries = CountryData.objects.all()
    return render(request, 'list_countries.html', {'countries': countries})

def country_detail(request, country_code):
    """Display details for a specific country, including metadata, pricing, and yearly electric consumption data."""
    country = get_object_or_404(CountryData, country_code=country_code)
    consumptions = ElectricConsumption.objects.filter(country=country).order_by('year')
    years = [consumption.year for consumption in consumptions]
    data = [consumption.consumption for consumption in consumptions]

    return render(request, 'country_detail.html', {
        'country': country,
        'years': years,
        'data': data,
        'metadata': country.metadata
    })

def about(request):
    """Render the about page."""
    return render(request, 'about.html')

def login_required_message(function):
    """Decorator to display a message if the user is not authenticated."""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            if not any(message.message == "Please log in to proceed with purchasing." for message in messages.get_messages(request)):
                messages.info(request, "Please log in to proceed with purchasing.")
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        return function(request, *args, **kwargs)
    return wrapper

@login_required
def dashboard(request):
    """Display dashboard with different content for superusers and regular users."""
    if request.user.is_superuser:
        active_users_count = User.objects.filter(is_active=True).count()
        total_orders_count = Purchase.objects.count()
        active_users = User.objects.filter(is_active=True).order_by('-date_joined')   # Show the newest users first
        recent_orders = Purchase.objects.all().order_by('-purchase_date')
        return render(request, 'dashboard.html', {
            'active_users_count': active_users_count,
            'total_orders_count': total_orders_count,
            'active_users': active_users,
            'recent_orders': recent_orders
        })
    else:
        purchases = Purchase.objects.filter(user=request.user).order_by('-purchase_date')
        return render(request, 'dashboard.html', {'purchases': purchases})

def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # Automatically log in the new user
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

def user_logout(request):
    """Log out the user and redirect to home page."""
    logout(request)
    return redirect('home')

@login_required_message
def purchase_view(request, country_code):
    """Display purchase view where users can confirm purchase details."""
    country = get_object_or_404(CountryData, country_code=country_code)
    if request.method == 'POST':
        purchase = Purchase(
            user=request.user,
            country=country,
            price=country.price   # Use the dynamic price
        )
        purchase.save()
        return redirect('dashboard')
    return render(request, 'purchase.html', {'country': country})

@login_required_message
def confirm_purchase(request, country_code):
    """Handle the final confirmation and processing of a purchase."""
    country = get_object_or_404(CountryData, country_code=country_code)
    if request.method == 'POST':
        purchase = Purchase(
            user=request.user,
            country=country,
            price=country.price   # Use the secure price from the database
        )
        purchase.save()
        return redirect('dashboard')
    return redirect('purchase_view', country_code=country_code)