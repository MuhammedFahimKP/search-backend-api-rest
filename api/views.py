import json
from django.http import JsonResponse,HttpResponse
from .models import Product
from django.forms.models import model_to_dict
from .serialzers import ProductSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["POST"])
def api_home(request,*args,**kwargs):


    if request.method == "POST":
        serializer = ProductSerialzer(data=request.data)
        if  serializer.is_valid():
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({"message": "Only POST requests are allowed."}, status=405)


# Create your views here.
