from django.db import models


# Create your models here.
from django.db.models import CharField


class WebInput( models.Model ):
    JobDescription = models.TextField()
    JobTitle = models.CharField( max_length=255 )
    URL = models.CharField(max_length = 255)

class UserInsert( models.Model ):
    Keyword = models.CharField( max_length=255 )
    Location = models.CharField( max_length=255 )
    Email=models.CharField( max_length=255 )
    CV =  models.TextField("")
