from django.urls import path
from . import views

app_name = 'example'
urlpatterns =[
    path('',views.show, name="show"),
    path('<int:id>/', views.product_detail, name="product_detail"),
]
