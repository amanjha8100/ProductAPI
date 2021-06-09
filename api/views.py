from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializers import ProductSerializer
from . models import Product

# Create your views here.
@api_view(["GET"])
def index(request):
    res = {
        "aman":"hello"
    }
    return Response(res)

@api_view(["GET"])
def productList(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product,many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product(request,pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
def updateProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def delete(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return Response("Successfully deleted")