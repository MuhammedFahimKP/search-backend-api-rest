from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register



from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    
    model = Product

    fields = [

            'name',
            'description',
            'price',
            'user',
            'is_public'
    ]