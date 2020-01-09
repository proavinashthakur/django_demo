from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Products
from . serializers import ProductSerializer


class Product(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return Response({"status": False, "msg": "Sorry, Something went wrong"})
        return Response({"status": True, "data": serializer.data})

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"status": True, "data":serializer.data})

    def delete(self, request, pk):
        try:
            Products.objects.get(id=pk).delete()
            products = Products.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response({"status": True, "data": serializer.data})
        except:
            return Response({"status": False, "msg": "Sorry, failed to delete the product"})

    def put(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                products = Products.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response({"status": True, "data": serializer.data})
            else:
                return Response({"status": False, "msg": "Sorry, invalid data"})
        except:
            return Response({"status": False, "msg": "Sorry, Something went wrong"})

