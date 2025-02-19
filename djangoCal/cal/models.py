from django.db import models

# Create your models here.
class Calculator(models.Model):
    first_num=models.DecimalField(max_digits=7,decimal_places=3)
    second_num=models.DecimalField(max_digits=7,decimal_places=3)
    operators=models.CharField(max_length=10)
    result=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_num}{self.operators}{self.second_num} ={self.result}"