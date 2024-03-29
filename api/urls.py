from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("list/",views.productList,name="products"),
    path("list/<int:pk>/",views.product,name="product"),
    path("create/",views.createProduct,name="add"),
    path("update/<int:pk>/",views.updateProduct,name="update"),
    path("list/delete/<int:pk>",views.delete,name="delete"),
]