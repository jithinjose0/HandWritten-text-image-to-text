from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Comp(models.Model):
    snum = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    cus_id= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def text_as_list(self):
        return self.snum.split()