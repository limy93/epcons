from django.contrib import admin
from .models import CountryData, CountryMetadata, ElectricConsumption, Purchase

# Register your models here.

class CountryDataAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_code', 'price')  # Display fields in the admin list view
    search_fields = ('country_name', 'country_code')  # Allow searching by country name and code
    list_filter = ('price',)  # Filter by price

admin.site.register(CountryData, CountryDataAdmin)

class CountryMetadataAdmin(admin.ModelAdmin):
    list_display = ('country', 'long_name', 'region', 'currency_unit', 'income_group', 'special_notes')
    search_fields = ('country__country_name', 'long_name')  # Enable search by related country's name
    list_filter = ('region', 'income_group')  # Filters for region and income group

admin.site.register(CountryMetadata, CountryMetadataAdmin)

class ElectricConsumptionAdmin(admin.ModelAdmin):
    list_display = ('country', 'year', 'consumption')
    search_fields = ('country__country_name', 'year')  # Search by country name and year
    list_filter = ('year', 'country__country_name')  # Add country name to the filter options
    ordering = ('country', 'year')  # Order entries by country and year

admin.site.register(ElectricConsumption, ElectricConsumptionAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'price', 'purchase_date')
    search_fields = ('user__username', 'country__country_name')  # Search by user username and country name
    list_filter = ('purchase_date', 'price', 'country__country_name')  # Filter by purchase date, price, and country
    ordering = ('-purchase_date',)  # Most recent purchases first

admin.site.register(Purchase, PurchaseAdmin)