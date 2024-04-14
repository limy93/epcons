from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from epdata.models import CountryData, ElectricConsumption, CountryMetadata, Purchase
from decimal import Decimal

class CountryDataModelTest(TestCase):
    def setUp(self):
        CountryData.objects.create(country_code='USA', country_name='United States of America', price=150.00)

    def test_string_representation(self):
        country = CountryData.objects.get(country_code='USA')
        self.assertEqual(str(country), 'United States of America')

    def test_country_data(self):
        country = CountryData.objects.get(country_code='USA')
        self.assertEqual(country.price, Decimal('150.00'))

class ElectricConsumptionModelTest(TestCase):
    def setUp(self):
        country = CountryData.objects.create(country_code='USA', country_name='United States')
        ElectricConsumption.objects.create(country=country, year=2020, consumption=1000.5)

    def test_string_representation(self):
        consumption = ElectricConsumption.objects.get(year=2020)
        self.assertEqual(str(consumption), 'United States 2020 Consumption')

    def test_consumption_data(self):
        consumption = ElectricConsumption.objects.get(year=2020)
        self.assertEqual(consumption.consumption, 1000.5)

class CountryMetadataModelTest(TestCase):
    def setUp(self):
        country = CountryData.objects.create(country_code='USA', country_name='United States')
        CountryMetadata.objects.create(country=country, long_name='United States', region='North America')

    def test_string_representation(self):
        metadata = CountryMetadata.objects.get(country__country_code='USA')
        self.assertEqual(str(metadata), 'Metadata for United States')

class PurchaseModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', password='doe')
        country = CountryData.objects.create(country_code='USA', country_name='United States', price=150.00)
        Purchase.objects.create(user=user, country=country, price=150.00)

    def test_string_representation(self):
        purchase = Purchase.objects.get(user__username='john')
        self.assertEqual(str(purchase), 'john purchased naming rights for United States for $150.00')

    def test_purchase_data(self):
        purchase = Purchase.objects.get(user__username='john')
        self.assertTrue(purchase.purchase_date <= timezone.now())