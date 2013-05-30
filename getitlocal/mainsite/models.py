from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

LOCATIONS = (
    ('DURHAM', 'Durham'), 
    ('INDIANAPOLIS', 'Indianapolis'), 
    ('BALTIMORE', 'Baltimore')
    )
CATS = (('GOODS', 'Goods'),
        ( 'SERVICES', 'Services'),
        ('RESTAURANTS', 'Restaurants')
        )

#Used as information about a specific store
class Store(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=25, choices=LOCATIONS)
    owner = models.ForeignKey(User, editable=False)
    description = models.TextField()
    category = models.CharField(max_length=15, choices=CATS)
    displayurl = models.CharField(max_length=500)
    url = models.URLField(editable=False)
    
    def __unicode__(self):
        return self.name

#Used for advertisements on the page
class Ads(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateTimeField("date bought")
    location_on_page = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return self.email

class StoreForm(ModelForm):
    class Meta:
        model = Store
