from rest_framework import serializers

from .models import Contact, User, Category, Shop, Product, ProductParameter, ProductInfo, OrderItem, Order

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state',)
        read_only_fields = ('id',)

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id',  'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
        real_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts')
        read_only_fields = ('id',)


