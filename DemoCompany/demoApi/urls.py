from django.urls import path
from .views import *

app_name = 'demoApi'
urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('product/all/', ProductsListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view())
]
