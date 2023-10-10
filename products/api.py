from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ProductSerializer , BrandSerializer,BrandDetailSerializer
from .models import Product , Brand
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter
from .pagination import MyPagination



# @api_view(['GET'])
# def product_list_api(request):
#     queryset = Product.objects.all()[:10]
#     data = ProductSerializer(queryset,many=True,context={'request':request}).data
#     return Response({'data':data})


# @api_view(['GET'])
# def product_detail_api(request,product_id):
#     queryset = Product.objects.get(id=product_id)
#     data = ProductSerializer(queryset,context={'request':request}).data
#     return Response({'data':data})


class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['brand', 'flag','name','price']
    filterset_class = ProductFilter
    ordering_fields = ['price', 'flag']
    pagination_class = MyPagination
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'subtitle']

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['price', 'flag']




class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer



class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer