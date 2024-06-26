from django.contrib.auth.models import User
from django.db import models

class CountryData(models.Model):
    country_code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)   # Default price for naming rights

    def __str__(self):
        return self.country_name

class ElectricConsumption(models.Model):
    country = models.ForeignKey(CountryData, on_delete=models.CASCADE, related_name='electric_consumptions')
    year = models.IntegerField()
    consumption = models.FloatField(null=True, blank=True)   # Allows null for years with no data

    def __str__(self):
        return f"{self.country.country_name} {self.year} Consumption"

class CountryMetadata(models.Model):
    country = models.OneToOneField(CountryData, on_delete=models.CASCADE, primary_key=True, related_name='metadata')
    long_name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, null=True, blank=True)
    currency_unit = models.CharField(max_length=50, null=True, blank=True)
    income_group = models.CharField(max_length=50, null=True, blank=True)
    special_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Metadata for {self.country.country_name}"

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    country = models.ForeignKey(CountryData, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, default='Pending')   # Ensure this field exists

    def __str__(self):
        return f'{self.user.username} purchased naming rights for {self.country.country_name} for ${self.price}'