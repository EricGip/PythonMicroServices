from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
import random 

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #get/api/
        # get all objects in product
        products = Product.objects.all()
        # many = True tells it to return an array
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def create(self, request): #post/api/products
    
        serializer = ProductSerializer(data = request.data)
        # verification
        serializer.is_valid(raise_exception = True)
        # save into model
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
    def retrieve(self, request, pk=None): #get /api/products/<str:id>
        # get item from object depending on primary key
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        # return data 
        return Response(serializer.data)

    def update(self, request, pk=None): #put /api/products/<str:id>
        # get item from object depending on key
        product = Product.objects.get(id.pk)

        serializer = ProductSerializer(instance = product, data=request.data)
        
        serializer.is_valid(raise_exception=True)
        #save data 
        serializer.save()
        # return data or 202 status
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #get /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })