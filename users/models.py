from django.db import models
from django.contrib.auth.models import User
from django.db import models 
from datetime import datetime

class Profile(models.Model):
    
    def __str__(self):
        return str(self.userid)
    
    userid = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    amount = models.IntegerField(default=100)
   
    

