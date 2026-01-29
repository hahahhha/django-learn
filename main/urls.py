from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # главный путь 
    path('', views.product_list, name='product_list'),
    # фильтрация по категориям
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # об одном продукте
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail')
]