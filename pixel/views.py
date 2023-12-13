from rest_framework import status
from rest_framework.response import Response
from .models import CatProducts, Product
from .serializers import CatProductsSerializer, ProductSerializer, OrderedSerializer
from rest_framework.views import APIView


class CatProductsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = CatProducts.objects.all()
        serializer = CatProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        main_product = Product.objects.all()
        serializer = ProductSerializer(main_product, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class OrderedAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
