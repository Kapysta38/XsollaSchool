from django.urls import path
from rest_framework.schemas import get_schema_view
from .views import *

app_name = 'demoApi'
urlpatterns = [
    path('openapi/', get_schema_view(
        title="Project for XsollaSchool",
        description="API for all things",
        version="1.0.0"
    ), name='openapi-schema'),
    path('product/create/', ProductCreateView.as_view()),
    path('product/all/', ProductsListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view())
]
