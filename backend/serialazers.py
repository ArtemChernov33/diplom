from rest_framework import serializers

from .models import Contact, User, Category, Shop, Product, ProductParameter, ProductInfo, OrderItem, Order

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state',)
        read_only_fields = ('id',)