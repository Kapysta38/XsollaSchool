import coreapi
import coreschema
from rest_framework import generics
from rest_framework.exceptions import ParseError
from .models import Product
from .serializers import ProductDetailSerializer, ProductsListSerializer
from rest_framework.schemas import AutoSchema, ManualSchema


class ProductCreateView(generics.CreateAPIView):
    """
    Method for adding a new product
    """
    serializer_class = ProductDetailSerializer


class ProductsListView(generics.ListAPIView):
    """
    A method to get a catalog of product
    """
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field('type',
                          required=False,
                          location='query',
                          schema=coreschema.String(),
                          description="not work, IDK"
                          ),
            coreapi.Field('price',
                          required=False,
                          location='query',
                          description='not work, IDK',
                          schema=coreschema.String(),
                          ),
            coreapi.Field('by_price',
                          required=False,
                          location='query',
                          description='not work, IDK',
                          schema=coreschema.String(),
                          ),
            coreapi.Field('to_price',
                          required=False,
                          location='query',
                          description='not work, IDK',
                          schema=coreschema.String(),
                          ),

        ]
    )
    serializer_class = ProductsListSerializer

    @staticmethod
    def check_value(key, value):
        if not value.replace('.', '').isdigit():
            raise ParseError(detail=f'Параметр {key} должен иметь тип float or int')
        return True

    def get_queryset(self):
        data = dict(self.request.query_params)
        result = Product.objects.all()
        if not data:
            return result
        type_ = data.get('type', None)
        result = result.filter(product_type=type_[0]) if (
                    type_ is not None and self.check_value('type', type_[0])) else result
        price = data.get('price', None)
        result = result.filter(price=price[0]) if (
                    price is not None and self.check_value('price', price[0])) else result
        by_price = data.get('by_price', None)
        result = result.filter(price__gte=by_price[0]) if (
                    by_price is not None and self.check_value('by_price', by_price[0])) else result
        to_price = data.get('to_price', None)
        result = result.filter(price__lt=to_price[0]) if (
                    to_price is not None and self.check_value('to_price', to_price[0])) else result
        return result


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View/change/delete one item method
    """
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
