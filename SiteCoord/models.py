from django.db import models

class Sites(models.Model):
    SiteID = models.CharField(verbose_name='Site ID', max_length=6)
    SiteName = models.CharField(verbose_name='Site Name', max_length=50)
    SiteManager = models.CharField(verbose_name='Site Manager', max_length=40)
    SiteEngineer = models.CharField(verbose_name='Site Engineer', max_length=40)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    
    def __str__(self):
        return self.SiteID
