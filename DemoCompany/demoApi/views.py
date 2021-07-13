from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductDetailSerializer, ProductsListSerializer
from .models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

