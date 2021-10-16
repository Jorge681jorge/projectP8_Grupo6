from rest_framework import serializers
from productApp.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Product
        fields = ['id', 'name', 'precio', 'stock', 'imagen1', 'talla', 'color']

    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)
          
        return {
                    'id': product.id, 
                    'name': product.name,
                    'precio': product.precio,
                    'stock': product.stock,
                    'imagen1': product.imagen1,
                    'talla': product.talla,
                    'color': product.color
                }