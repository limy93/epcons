from django.shortcuts import render, get_object_or_404
from .models import CountryData, CountryMetadata
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def list_countries(request):
    countries = CountryData.objects.all()
    return render(request, 'list_countries.html', {'countries': countries})

def country_detail(request, country_code):
    country = get_object_or_404(CountryData, country_code=country_code)
    metadata = get_object_or_404(CountryMetadata, country=country)
    return render(request, 'country_detail.html', {'country': country, 'metadata': metadata})

@login_required
def dashboard(request):
    if request.user.is_superuser:
        # Logic for admin dashboard
        return render(request, 'admin_dashboard.html')
    else:
        # Logic for user dashboard
        return render(request, 'user_dashboard.html')

# Add views for purchase, login, logout, and registration as needed.