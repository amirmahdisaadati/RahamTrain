from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from . import serializer
import coreapi
from rest_framework.schemas import AutoSchema
# Create your views here.


class GetAllProductsApiView(APIView):

    def get(self, requset):

            products = Product.objects.all()
            print(products)
            serialized_data = serializer.ProductSerializer(products, many=True)
            print(serialized_data)
            data = serialized_data.data
            return Response({'data': data, 'status': "status.HTTP_200_OK"})


            #return Response({'status': "Internal Server Error, We'll Check It Later"},
                        #    status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleProductApiView(APIView):

        def get(self, request, pk):
                product = Product.objects.get(id=pk)
                print(product)
                serilized_data=serializer.SingleProductSerializer(product)
                print(serilized_data)
                data = serilized_data.data
                return Response({'data': data})

