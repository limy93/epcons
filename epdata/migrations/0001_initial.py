# Generated by Django 4.2.1 on 2024-04-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryData',
            fields=[
                ('country_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=100)),
                ('ep_1994', models.FloatField(blank=True, null=True)),
                ('ep_1995', models.FloatField(blank=True, null=True)),
                ('ep_1996', models.FloatField(blank=True, null=True)),
                ('ep_1997', models.FloatField(blank=True, null=True)),
                ('ep_1998', models.FloatField(blank=True, null=True)),
                ('ep_1999', models.FloatField(blank=True, null=True)),
                ('ep_2000', models.FloatField(blank=True, null=True)),
                ('ep_2001', models.FloatField(blank=True, null=True)),
                ('ep_2002', models.FloatField(blank=True, null=True)),
                ('ep_2003', models.FloatField(blank=True, null=True)),
                ('ep_2004', models.FloatField(blank=True, null=True)),
                ('ep_2005', models.FloatField(blank=True, null=True)),
                ('ep_2006', models.FloatField(blank=True, null=True)),
                ('ep_2007', models.FloatField(blank=True, null=True)),
                ('ep_2008', models.FloatField(blank=True, null=True)),
                ('ep_2009', models.FloatField(blank=True, null=True)),
                ('ep_2010', models.FloatField(blank=True, null=True)),
                ('ep_2011', models.FloatField(blank=True, null=True)),
                ('ep_2012', models.FloatField(blank=True, null=True)),
                ('ep_2013', models.FloatField(blank=True, null=True)),
                ('ep_2014', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountryMetadata',
            fields=[
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='epdata.countrydata')),
                ('long_name', models.CharField(max_length=100)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('currency_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('income_group', models.CharField(blank=True, max_length=50, null=True)),
                ('special_notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]