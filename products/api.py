from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer , BrandSerializer
from .models import Product , Brand


@api_view(['GET'])
def product_list_api(request):
    queryset = Product.objects.all()[:10]
    data = ProductSerializer(queryset,many=True,context={'request':request}).data
    return Response({'data':data})


@api_view(['GET'])
def product_detail_api(request,product_id):
    queryset = Product.objects.get(id=product_id)
    data = ProductSerializer(queryset,context={'request':request}).data
    return Response({'data':data})



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer