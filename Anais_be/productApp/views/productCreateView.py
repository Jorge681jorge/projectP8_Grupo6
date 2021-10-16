from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from productApp.serializers.productSerializer import ProductSerializer

class ProductCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"name":request.data["name"], 
                     "precio":request.data["precio"],
                     "stock":request.data["stock"],
                     "imagen1":request.data["imagen1"],
                     "talla":request.data["talla"],
                     "color":request.data["color"]
                     }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)