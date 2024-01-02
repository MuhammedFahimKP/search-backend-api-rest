from rest_framework import viewsets

from api.serialzers import ProductSerialzer
from api.models import Product



class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    lookup_field = 'pk'