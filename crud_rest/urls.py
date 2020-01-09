from django.urls import path
from . import views
urlpatterns = [
    path("add-product", views.Product.as_view(), name="add-product"),
    path("list-products", views.Product.as_view(), name="list-product"),
    path("delete-product/<int:pk>", views.Product.as_view(), name="delete-product"),
    path("update-product/<int:pk>", views.Product.as_view(), name="update-product"),

]
