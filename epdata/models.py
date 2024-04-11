from django.db import models
from django.utils import timezone

# Create your models here.

class CountryData(models.Model):
    country_code = models.CharField(max_length=3, primary_key=True)
    country_name = models.CharField(max_length=100)
    ep_1994 = models.FloatField(null=True, blank=True)
    ep_1995 = models.FloatField(null=True, blank=True)
    ep_1996 = models.FloatField(null=True, blank=True)
    ep_1997 = models.FloatField(null=True, blank=True)
    ep_1998 = models.FloatField(null=True, blank=True)
    ep_1999 = models.FloatField(null=True, blank=True)
    ep_2000 = models.FloatField(null=True, blank=True)
    ep_2001 = models.FloatField(null=True, blank=True)
    ep_2002 = models.FloatField(null=True, blank=True)
    ep_2003 = models.FloatField(null=True, blank=True)
    ep_2004 = models.FloatField(null=True, blank=True)
    ep_2005 = models.FloatField(null=True, blank=True)
    ep_2006 = models.FloatField(null=True, blank=True)
    ep_2007 = models.FloatField(null=True, blank=True)
    ep_2008 = models.FloatField(null=True, blank=True)
    ep_2009 = models.FloatField(null=True, blank=True)
    ep_2010 = models.FloatField(null=True, blank=True)
    ep_2011 = models.FloatField(null=True, blank=True)
    ep_2012 = models.FloatField(null=True, blank=True)
    ep_2013 = models.FloatField(null=True, blank=True)
    ep_2014 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.country_name

class CountryMetadata(models.Model):
    country = models.OneToOneField(CountryData, on_delete=models.CASCADE, primary_key=True)
    long_name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, null=True, blank=True)
    currency_unit = models.CharField(max_length=50, null=True, blank=True)
    income_group = models.CharField(max_length=50, null=True, blank=True)
    special_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.long_name