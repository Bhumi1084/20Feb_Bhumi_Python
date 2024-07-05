from django.db import models

# Create your models here.

class product_master(models.Model):
    pname = models.CharField(max_length=100)

    def __str__(self):
        return self.pname
    
class sub_product(models.Model):
    pname = models.ForeignKey(product_master,on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')
    pmodel = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)

    def __str__(self):
        return self.pname.pname