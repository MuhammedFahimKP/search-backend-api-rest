from rest_framework import serializers
from django.contrib.auth.models import User







class userPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    this_not_real = serializers.CharField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'id',
            'this_not_real',
        ]



    # def get_other_products(self,obj):
    #     # request = self.context.get('request')
    #     # print(obj)
    #     user = obj
    #     my_products_qs = user.product_set.all()
    #     return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data
    