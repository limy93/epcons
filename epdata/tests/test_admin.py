from django.contrib.admin import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase
from epdata.admin import CountryDataAdmin, CountryMetadataAdmin, ElectricConsumptionAdmin, PurchaseAdmin
from epdata.models import CountryData, CountryMetadata, ElectricConsumption, Purchase

class MockRequest:
    pass

request = MockRequest()

class AdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_CountryDataAdmin(self):
        admin = CountryDataAdmin(CountryData, self.site)
        self.assertIsInstance(admin, ModelAdmin)   # Basic test to confirm admin interface setup

    def test_CountryMetadataAdmin(self):
        admin = CountryMetadataAdmin(CountryMetadata, self.site)
        self.assertIsInstance(admin, ModelAdmin)

    def test_ElectricConsumptionAdmin(self):
        admin = ElectricConsumptionAdmin(ElectricConsumption, self.site)
        self.assertIsInstance(admin, ModelAdmin)

    def test_PurchaseAdmin(self):
        admin = PurchaseAdmin(Purchase, self.site)
        self.assertIsInstance(admin, ModelAdmin)

# Additional tests can be implemented as needed