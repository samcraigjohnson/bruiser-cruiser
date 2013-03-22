from django.db import models

#Used as information about a specific store
class Store(models.Model):
    name = models.CharField(max_length=500)
    location = models.TextField()
    #owner = models.ForeignKey(Owner)
    description = models.TextField()
    category = models.CharField(max_length=100)
    url = models.URLField()
    
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
