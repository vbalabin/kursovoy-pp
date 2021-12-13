from rest_framework.serializers import ModelSerializer

from store.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'availability']
