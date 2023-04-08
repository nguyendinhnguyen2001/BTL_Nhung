from django.db import models
from user.models import User
# Create your models here.

class History(models.Model):
    id_history=models.IntegerField(primary_key=True)
    ph=models.FloatField()
    turbidity=models.FloatField()
    tds=models.FloatField()
    result=models.CharField(max_length=50)
    time_posted=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_history
    