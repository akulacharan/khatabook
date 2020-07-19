from django.db import models

# Create your models here.





class Customer(models.Model):
    fullname = models.CharField(max_length=200,default="")
    address = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=15,default="")
    balence = models.IntegerField(null=True)

    class Meta:
        abstract = True


    def __str__(self):
        return self.fullname



class Individual(Customer,models.Model):
    date_created = models.DateTimeField(auto_now=True)
    product = models.CharField(max_length=200,null=True)
    price = models.IntegerField(null=True)
    Total = models.IntegerField(null=True)





