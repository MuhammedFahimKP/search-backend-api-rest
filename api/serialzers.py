# from api.models import Product



from rest_framework import serializers, reverse 

from .models import Product
from . import validators
from .min_serializers import userPublicSerializer

class UserProductInlineSerializer(serializers.Serializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field = 'pk',
        read_only = True
    )

    name = serializers.CharField(read_only=True)


class ProductSerialzer(serializers.ModelSerializer):
    user = userPublicSerializer(read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
   
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field = 'pk'
    )

    name = serializers.CharField(validators=[
        validators.validate_name_no_hello,
        validators.unique_product_name
    ])

    email = serializers.CharField(source="user.email",read_only=True)
    class Meta:
        model = Product

        
        fields = [

            'user',
            'url',
            'email' ,
            'edit_url',
            'id',
            'body',
            'name',
            'description',
            'price',
            'sale_price',
            'my_user_data',
            'my_discount',  
            'public'
        ]


    def get_edit_url(self,obj):
        req = self.context.get('request')
        
        if req is None:
            return None
        
        return reverse.reverse('product-edit',kwargs={'pk':obj.id},request=req)   
    
    def get_my_user_data(self,obj):
        return {"username":obj.user.username}
    
    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
        
   

    # def create(self,validated_data):
    #     email = validated_data.pop('email')
    #     print(email)
    #     obj = super().create(validated_data)
    #     return obj


