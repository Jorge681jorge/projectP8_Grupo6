from django.conf import settings
from rest_framework import generics

from productApp.models.product import Product
from productApp.serializers.productSerializer import ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
            
        return super().get(request, *args, **kwargs)