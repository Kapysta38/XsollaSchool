from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProductDetailSerializer, ProductsListSerializer
from .models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer

    @staticmethod
    def check_filter(data):
        result = Product.objects.all()
        if not data:
            return result
        if 'type' in data:
            result = result.filter(product_type=data['type'][0])
        if 'price' in data:
            result = result.filter(price=data['price'][0])
        if 'by_price' in data:
            if data['by_price'][0].replace('.', '').isdigit():
                result = result.filter(price__gte=float(data['by_price'][0]))
        if 'to_price' in data:
            if data['to_price'][0].replace('.', '').isdigit():
                result = result.filter(price__lt=float(data['to_price'][0]))
        return result

    def get(self, request, *args, **kwargs):
        self.queryset = self.check_filter(dict(request.GET))
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

