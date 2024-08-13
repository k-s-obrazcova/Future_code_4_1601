from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('product/all/', product_list, name='product_list'),
    path('product/one-filter/', get_one_filter_product, name='get_one_filter'),
    path('product/more-filter/', get_more_filter_product, name='get_more_filter'),
    path('product/all-filter/', product_catalog_with_filter, name='product_list_filter'),
    path('product/detail/<int:id>/', get_one_product, name='get_one_product'),

    path('supplier/', ListSupplier.as_view(), name='supplier_list'),
    path('supplier/create/', CreateSupplier.as_view(), name='supplier_create'),
    path('supplier/detail/<int:pk>/', DetailSupplier.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/', UpdateSupplier.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', DeleteSupplier.as_view(), name='supplier_delete'),

    path('order/<int:pk>/', OrderDetail.as_view(), name='order_detail'),

    path('api/', test_json, name='api_test'),
    path('api/orders/', order_api_list, name='api_order_list'),
    path('api/orders/<int:pk>/', order_api_detail, name='api_order_detail'),

    path('filter/', template_filter_django, name='template_filter_django'),
    path('tags/', template_tag_django, name='template_tag_django'),
]

router = routers.SimpleRouter()
router.register('api/products', ProductViewSet, basename='product')
router.register('api/product_simple', ProductViewSetDif, basename='product_simple')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/tag', TagViewSet, basename='tag')
router.register('api/parametr', ParametrViewSet, basename='parametr')
router.register('api/pos_parametr', Pos_parametrViewSet, basename='pos_parametr')
router.register('api/pos_order', Pos_orderViewSet, basename='pos_order')
router.register('api/pos_supply', Pos_supplyViewSet, basename='pos_supply')
router.register('api/warehouse', WarehouseViewSet, basename='warehouse')
router.register('api/inventory', InventoryViewSet, basename='inventory')
router.register('api/review', ReviewViewSet, basename='review')
router.register('api/supplier_admin', SupplierAdminViewSet, basename='supplier_admin')
urlpatterns += router.urls
