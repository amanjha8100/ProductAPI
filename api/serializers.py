from django.db.models import fields
from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models = Product
        fields = "__all__"