from django.shortcuts import render
from rest_framework import authentication,generics,mixins,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.permissions import IsStaffEditorPermission
from api.mixins import (
    StaffEditorMixin,
    UserQuerySetMixin
)
from api.models import Product
from api.serialzers import ProductSerialzer
from api.authentication import TokenAuthentication as tk

# Create your views here.



class ProductDetailView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]  
    permission_classes = [IsStaffEditorPermission]


class ProductCreateView(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]  
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):

        #serializer.save(user=self.request.user)
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('description')
        content = name
            
        serializer.save(description=content)



class ProductListView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]   
    permission_classes = [IsStaffEditorPermission]

class ProductListCreateView(generics.ListCreateAPIView):  
    
    
    
    queryset = Product.objects.all()
    serializer_class = ProductSerialzer    


    # permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):

        #serializer.save(user=self.request.user)
        
        name = serializer.validated_data.get('name')
        content = serializer.validated_data.get('description')
        content = name    
        serializer.save(description=content)


    
    # def get_queryset(self,*args, **kwargs):
    #     qs = super().get_queryset(*args,**kwargs)
    #     if not self.request.user.is_authenticated:
    #         return Product.objects.none()
    #     print(self.request.user)
    #     return qs.filter(user=self.request.user) 
    
    
# @api_view(["GET","POST"])
# def create_list_view(request,*args,**kwargs):

#     method = request.method 

#     if method == "GET":

#         queryset = Product.objects.all()

#         data = ProductSerialzer(queryset,many=True).data
#         return Response(data)


#     if method == "POST":
#         serializer = ProductSerialzer(data=request.data)
#         if  serializer.is_valid():
#             instance = serializer.save()
#             print(instance)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
    




class ProductUpdateView(generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer  
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]  
    permission_classes = [IsStaffEditorPermission]  

  
    

class ProductDeleteView(generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerialzer  
    authentication_classes = [authentication.SessionAuthentication,authentication.TokenAuthentication]  
    permission_classes = [IsStaffEditorPermission]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)



# class ProductMixinView(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialzer
#     lookup_field = 'pk'

#     def get(self,request,*args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(self.request,*args,**kwargs)
#         return self.list(self.request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(self.request,*args, **kwargs)


