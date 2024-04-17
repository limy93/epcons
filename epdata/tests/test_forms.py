from django.contrib.auth.models import User
from django.test import TestCase
from epdata.forms import RegisterForm

class RegisterFormTest(TestCase):

    def test_register_form_valid_data(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_data(self):
        # Test non-matching passwords
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword'
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_register_form_email_field_required(self):
        # Test missing email (required field)
        form_data = {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_register_form_save(self):
        # Test saving the form creates a user
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        }
        form = RegisterForm(data=form_data)
        if form.is_valid():
            user = form.save()
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(user.username, 'newuser')
            self.assertEqual(user.email, 'newuser@example.com')