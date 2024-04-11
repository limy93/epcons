"""
URL configuration for epcons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views
from epdata.views import (home, list_countries, country_detail, dashboard,
                          register, user_logout, purchase_view, confirm_purchase)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('countries/', list_countries, name='list_countries'),  # List countries
    path('countries/<str:country_code>/', country_detail, name='country_detail'),  # Country detail
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard
    path('register/', register, name='register'),  # Registration page
    path('purchase/<str:country_code>/', purchase_view, name='purchase'),  # Purchase page
    path('confirm_purchase/<str:country_code>/', confirm_purchase, name='confirm_purchase'),  # Confirm purchase

    # Login and logout URLs using Django's built-in views
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Custom template for login under 'accounts/login/'
    path('logout/', user_logout, name='logout'),  # Custom logout view that redirects to home page

    # Additional paths might be added below as needed.
]