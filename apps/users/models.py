# from django.db import models
from djongo import models

class User( models.Model ):
    
    user_name = models.CharField   ( max_length = 70, blank = False )
    password  = models.CharField   ( max_length = 100, blank = False )
    status    = models.BooleanField( default    = True )
