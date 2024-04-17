from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from epdata.models import CountryData, CountryMetadata, ElectricConsumption, Purchase

class ViewTestCase(TestCase):
    def setUp(self):
        self.country = CountryData.objects.create(country_code='USA', country_name='United States')
        CountryMetadata.objects.create(country=self.country, long_name='United States of America')
        User.objects.create_user('testuser', 'test@example.com', '12345')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_country_detail_view_not_logged_in(self):
        response = self.client.get(reverse('country_detail', args=['USA']))
        self.assertRedirects(response, expected_url=reverse('login') + '?next=' + reverse('country_detail', args=['USA']))

    def test_country_detail_view_logged_in(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('country_detail', args=[self.country.country_code])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'country_detail.html')

    def test_country_detail_view_not_logged_in(self):
        # Access the country detail page without logging in
        response = self.client.get(reverse('country_detail', args=['USA']))
        self.assertEqual(response.status_code, 200, "The response status should be 200 OK")
        self.assertTemplateUsed(response, 'country_detail.html')  # Verify the correct template is used
 
    def test_dashboard_view_logged_in(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_registration_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('home'))