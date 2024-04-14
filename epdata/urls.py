from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.list_countries, name='list_countries'),
    path('countries/<str:country_code>/', views.country_detail, name='country_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('purchase/<str:country_code>/', views.purchase_view, name='purchase'),
    path('confirm_purchase/<str:country_code>/', views.confirm_purchase, name='confirm_purchase'),

    # Authentication URLs using reverse_lazy for deferred URL resolution
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html', next_page=reverse_lazy('dashboard')), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]