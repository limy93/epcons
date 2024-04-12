# Generated by Django 4.2.1 on 2024-04-12 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epdata', '0002_remove_countrydata_ep_1994_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrydata',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=10),
        ),
    ]
