from rest_framework import serializers
from.models import Category,Cars

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
         model = Category
         fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
         model = Cars
         fields = "__all__"
