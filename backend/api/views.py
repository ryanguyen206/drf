from django.http import JsonResponse
from products.models import Product
from django.http import HttpResponse
import json 
from rest_framework.response import Response
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_home(request):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)