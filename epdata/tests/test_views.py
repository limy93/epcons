import re
from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from epdata.models import CountryData, CountryMetadata, ElectricConsumption, Purchase

class ViewTestCase(TestCase):
    def setUp(self):
        self.country = CountryData.objects.create(country_code='USA', country_name='United States')
        CountryMetadata.objects.create(country=self.country, long_name='United States of America')
        self.user = User.objects.create_user('testuser', 'test@example.com', '12345')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_country_detail_view_not_logged_in(self):
        # Access the country detail page without logging in
        response = self.client.get(reverse('country_detail', args=['USA']))
        self.assertEqual(response.status_code, 200, "The response status should be 200 OK")
        self.assertTemplateUsed(response, 'country_detail.html')

    def test_country_detail_view_logged_in(self):
        self.client.login(username='testuser', password='12345')
        url = reverse('country_detail', args=[self.country.country_code])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'country_detail.html')

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

    # Test cases for password reset
    def test_password_reset_request(self):
        response = self.client.post(reverse('password_reset'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)

    def test_password_reset_done_view(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'password_reset_done.html')

def test_password_reset_confirm_and_complete(self):
    # Initiate the password reset
    response = self.client.post(reverse('password_reset'), {'email': 'test@example.com'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(len(mail.outbox), 1)

    # Extract the reset URL from the email body
    email_body = mail.outbox[0].body
    match = re.search(r'http://testserver(?P<url>/reset/\S+/\S+)/', email_body)
    self.assertIsNotNone(match, "Reset URL not found in the email body")
    reset_url = match.group('url')

    # Follow the reset link (simulate clicking the link in the email)
    response = self.client.get(reset_url, follow=True)
    self.assertEqual(response.status_code, 200, "Reset page did not return HTTP 200")

    # Submit the new password
    post_response = self.client.post(reset_url, {
        'new_password1': 'newpassword123',
        'new_password2': 'newpassword123'
    }, follow=True)
    print(response.redirect_chain) 

    # Verify redirect to the password reset complete page
    self.assertRedirects(post_response, reverse('password_reset_complete'), status_code=301, target_status_code=200)