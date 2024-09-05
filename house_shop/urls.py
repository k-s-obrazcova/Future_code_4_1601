from django.urls import path, include

from .views import *

from rest_framework import routers

urlpatterns = [
    path('catalog/', HouseList.as_view(), name='house_list'),
    path('catalog/<int:pk>/', HouseDetail.as_view(), name='house_detail'),

    path('developer/', DeveloperList.as_view(), name='developer_list'),

    path('developer/<int:pk>/', DeveloperDetail.as_view(), name='developer_detail'),
]

router = routers.SimpleRouter()
router.register('api/house', HouseViewSet, basename='house')
router.register('api/realtor', RealtorViewSet, basename='realtor')
router.register('api/developer', DeveloperViewSet, basename='developer')
router.register('api/services', ServicesViewSet, basename='services')
router.register('api/order', OrderViewSet, basename='order')
router.register('api/development', DevelopmentViewSet, basename='development')
router.register('api/pos_order', PosOrderViewSet, basename='pos_order')
router.register('api/pos_development', PosDevelopmentViewSet, basename='pos_development')
urlpatterns += router.urls
