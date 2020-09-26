from django.urls import path

from . import views

urlpatterns = [
    path('api/products', views.GetAllProductsApiView.as_view(), ),
    path('api/SingleProduct/<int:pk>', views.SingleProductApiView.as_view(), )


]