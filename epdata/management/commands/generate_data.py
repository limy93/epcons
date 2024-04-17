import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from epdata.models import CountryData, Purchase
from faker import Faker

class Command(BaseCommand):
    help = 'Generate fake data for users and purchases'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, help='Number of fake users to be created')
        parser.add_argument('--purchases', type=int, help='Number of fake purchases to be created')

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to generate fake data...'))
        fake = Faker()
        self.create_users(fake, options['users'])
        self.create_purchases(fake, options['purchases'])
        self.stdout.write(self.style.SUCCESS('Finished generating fake data.'))

    def create_users(self, fake, number):
        for _ in range(number):
            username = fake.user_name()
            email = fake.email()
            user = User.objects.create_user(username=username, email=email, password='testpass123')
            self.stdout.write(self.style.SUCCESS(f'Created user: {username}'))

    def create_purchases(self, fake, number):
        users = list(User.objects.all())
        countries = list(CountryData.objects.all())
        for _ in range(number):
            user = random.choice(users)
            country = random.choice(countries)
            Purchase.objects.create(user=user, country=country, price=country.price)
            self.stdout.write(self.style.SUCCESS(f'Created purchase for {country.country_name} by {user.username}'))