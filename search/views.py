from rest_framework import generics,mixins
from rest_framework.response import Response


from api import client
from api.models import Product
from api.serialzers import ProductSerialzer



class SearchListNewApiView(generics.GenericAPIView):

    queryset =  Product.objects.all()
    serializer_class = ProductSerialzer

    def get(self,*args, **kwargs):


        query = self.request.GET.get('q')

        if not query:
            return  Response('No Queries',status=400)
        
        results = client.perform_search(query) 
        
        return  Response(results)





class SearchListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Product.objects.all()
        if q is not None:
            user = self.request.user if self.request.user.is_authenticated else None
            results = qs.search(q,user)
        return results







# Create your views here.
