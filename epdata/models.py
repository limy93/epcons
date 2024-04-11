from django.db import models
from django.contrib.auth.models import User  # Import the User model
from django.utils import timezone

class CountryData(models.Model):
    country_code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class ElectricConsumption(models.Model):
    country = models.ForeignKey(CountryData, on_delete=models.CASCADE, related_name='electric_consumptions')
    year = models.IntegerField()
    consumption = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.country.country_name} {self.year}"

class CountryMetadata(models.Model):
    country = models.OneToOneField(CountryData, on_delete=models.CASCADE, primary_key=True, related_name='metadata')
    long_name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, null=True, blank=True)
    currency_unit = models.CharField(max_length=50, null=True, blank=True)
    income_group = models.CharField(max_length=50, null=True, blank=True)
    special_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.long_name
    
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    country = models.ForeignKey(CountryData, on_delete=models.CASCADE, related_name='purchases')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} purchased {self.country.country_name} for ${self.price}'