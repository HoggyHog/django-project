from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(max_length=100,default="")
    roll=models.CharField(max_length=100,default="")
    phone=models.DecimalField(max_digits=10,decimal_places=0)
    dept=models.CharField(max_length=100,default="")

    web=models.CharField(max_length=100,default=" ",null=" ")
    ui=models.CharField(max_length=100,default=" ",null=" ")
    business=models.CharField(max_length=100,default=" ",null=" ")

    comments=models.CharField(max_length=100,default="")
    
    def __str__(self):
            return self.name