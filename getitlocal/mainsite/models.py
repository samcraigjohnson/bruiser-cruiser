from django.db import models

#Used to hold the data for the owner of a store
class Owner(models.Model):
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    billing_info = models.CharField(max_length=500)

    def __unicode__(self):
        return self.email

#Used as information about a specific store
class Store(models.Model):
    name = models.CharField(max_length=500)
    location = models.TextField()
    owner = models.ForeignKey(Owner)
    description = models.TextField()
    category = models.CharField(max_length=100)
    url = models.URLField()
    
    def __unicode__(self):
        return self.name
        
#Used to hold average user data
class User(models.Model):
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    favorties = models.TextField()

    def __unicode__(self):
        return self.email

#Used for advertisements on the page
class Ads(models.Model):
    store = models.ForeignKey(Store)
    date = models.DateTimeField("date bought")
    location_on_page = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
        return self.email
