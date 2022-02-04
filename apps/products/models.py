# from django.db import models
from djongo import models

class Product( models.Model ):
    
    name        = models.CharField ( max_length = 150, blank = False )
    description = models.CharField ( max_length = 250, blank = False )
    status      = models.BooleanField( default    = True )