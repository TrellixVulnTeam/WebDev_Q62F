from django.urls import path, re_path
from api.views import fmethod, product_list,prod_list_html,product_detail, categories_l, categories_d
urlpatterns=[
    path('', fmethod, name = "mainMenu"),
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/', categories_l),
    path('categories/<int:cat_id>/', categories_d)
]