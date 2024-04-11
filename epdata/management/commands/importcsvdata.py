from django.core.management.base import BaseCommand
import csv
import os
from django.conf import settings
from epdata.models import CountryData, CountryMetadata
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

class Command(BaseCommand):
    help = 'Automatically imports data and metadata from CSV files in the data folder, clearing previous entries.'

    def handle(self, *args, **options):
        # Constructing file paths relative to the manage.py file
        base_dir = settings.BASE_DIR
        data_csv_path = os.path.join(settings.BASE_DIR, 'epdata', 'data', 'epcons_data.csv')
        metadata_csv_path = os.path.join(settings.BASE_DIR, 'epdata', 'data', 'epcons_metadata.csv')

        self.stdout.write(self.style.SUCCESS('Clearing existing data...'))
        CountryMetadata.objects.all().delete()  # Delete metadata first due to the FK constraint
        CountryData.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Importing new data...'))
        with transaction.atomic():  # Use a transaction to ensure data integrity
            self.parse_country_data(data_csv_path)
            self.parse_country_metadata(metadata_csv_path)
        self.stdout.write(self.style.SUCCESS('Data import completed successfully.'))

    def parse_country_data(self, csv_file_path):
        with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                CountryData.objects.update_or_create(
                    country_code=row['Country Code'],
                    defaults={
                        'country_name': row['Country Name'],
                        'ep_1994': row['1994'] or None,
                        'ep_1995': row['1995'] or None,
                        'ep_1996': row['1996'] or None,
                        'ep_1997': row['1997'] or None,
                        'ep_1998': row['1998'] or None,
                        'ep_1999': row['1999'] or None,
                        'ep_2000': row['2000'] or None,
                        'ep_2001': row['2001'] or None,
                        'ep_2002': row['2002'] or None,
                        'ep_2003': row['2003'] or None,
                        'ep_2004': row['2004'] or None,
                        'ep_2005': row['2005'] or None,
                        'ep_2006': row['2006'] or None,
                        'ep_2007': row['2007'] or None,
                        'ep_2008': row['2008'] or None,
                        'ep_2009': row['2009'] or None,
                        'ep_2010': row['2010'] or None,
                        'ep_2011': row['2011'] or None,
                        'ep_2012': row['2012'] or None,
                        'ep_2013': row['2013'] or None,
                        'ep_2014': row['2014'] or None,
                    }
                )

    def parse_country_metadata(self, csv_file_path):
        with open(csv_file_path, newline='', encoding='ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    country_data = CountryData.objects.get(country_code=row['Country Code'])
                    CountryMetadata.objects.update_or_create(
                        country=country_data,
                        defaults={
                            'long_name': row['Long Name'],
                            'region': row['Region'] or None,
                            'currency_unit': row['Currency Unit'] or None,
                            'income_group': row['Income Group'] or None,
                            'special_notes': row['Special Notes'] or None,
                        }
                    )
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Country data not found for {row['Country Code']}, skipping metadata entry."))