from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]