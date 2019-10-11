from django.db import models

# Create your models here.
class Author(models.Model):
    AID=models.IntegerField(primary_key=True)
    AName=models.CharField(max_length=30)
    A_Addr=models.TextField(max_length=150,unique=True)

    def __str__(self):
        return str(self.AID)
class Book(models.Model):
    BID=models.IntegerField(primary_key=True)
    BName=models.CharField(max_length=30)
    AID=models.ForeignKey(Author,on_delete=models.CASCADE)
    Cost=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.BID)

class Order_Details(models.Model):
    OID=models.AutoField(primary_key=True)
    BID=models.ForeignKey(Book,on_delete=models.CASCADE)
    Quantity=models.IntegerField()

    def __str__(self):
        return str(self.OID)


    








