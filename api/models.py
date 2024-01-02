from django.db import models
from django.contrib.auth.models import User
from django.db.models import  Q
# Create your models here.


class ProductQuerySet(models.QuerySet):

    def is_public(self):
        return self.filter(public=True)
    

    def search(self,query,user=None):
        lookup = Q(name__icontains=query) | Q(description__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            
            qs2 = self.filter(user=user).filter(lookup)
            qs  = (qs | qs2).distinct()
        return qs
            
    

class ProductManger(models.Manager):

    def get_queryset(self,*args,**kwargs):
        return ProductQuerySet(self.model,using=self._db)

    def search(self,query,user=None):
        return self.get_queryset().is_public().filter(name__icontains=query)




class Product(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500,blank=True,null=True)
    price = models.IntegerField(default=0)
    public = models.BooleanField(default=True)


    """
        custom product manger
    """
    objects = ProductManger()

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return "122"
    

    def __str__(self) -> str :
        return  self.name
    

    @property
    def body(self) -> str:
        return {
            
             f"{self.name}" : self.description
        } 


    @property
    def is_public(self) -> str:
        if self.public:
            return f"Public"
        else:
            return f"Not Public"