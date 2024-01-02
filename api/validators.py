from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


# def validate_name(value):
#         qs = Product.objects.filter(name__exact=value)

#         if qs.exists():
            
#             raise serializers.ValidationError(

#                 f"{value} is already exists"
#             )
         
#         return value   

def validate_name_no_hello(value):
      
      if "hello" in value.lower():
            raise serializers.ValidationError(
                  f"hello is not allowed"
            )
      
      return value      
            
unique_product_name = UniqueValidator(
      queryset=Product.objects.all()
)           