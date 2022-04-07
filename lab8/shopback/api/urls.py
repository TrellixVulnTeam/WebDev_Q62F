from django.urls import path, re_path
from api.views import product_list,product_detail, categories_list, categories_d, prod_list_category

urlpatterns=[
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('products/category/<int:product_category>/', prod_list_category),
    path('categories/', categories_list),
    path('categories/<int:cat_id>/', categories_d),
]