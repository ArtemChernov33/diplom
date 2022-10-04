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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        real_only_fields = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('name', 'category',)

class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = ('parameter', 'value',)

class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_parameters = ProductParameterSerializer(read_only=True, many=True)
    class Meta:
        model = ProductInfo
        fields = ('id', 'model', 'product', 'shop', 'quantity', 'price', 'price_rrc', 'product_parameters',)
        read_only_fields = ('id',)
        ordering = ['-id']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'quantity', 'order', 'product_info')
        read_only_fields = ('id',)
        extra_kwargs = {
            'order': {'write_only': True}
        }

class OrderCreateItemSerializer(serializers.ModelSerializer):
    product_info = ProductInfoSerializer(read_only=True)
    class Meta:
        model = OrderItem
        #fields = ('id', 'order', 'product_info', 'quantity')
        fields = ("__all__")
        #read_only_fields = ('id',)
class OrderSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(read_only=True)
    order_items = OrderCreateItemSerializer(read_only=True)
    total_sum = serializers.IntegerField()
    class Meta:
        model = Order
        fields = ('id', 'dt', 'state', 'contact', 'order_items', 'total_sum', )
        read_only_fields = ('id',)

