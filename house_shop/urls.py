from django.urls import path, include
from rest_framework import routers

from .views import *

urlpatterns = [
    path('catalog/', HouseList.as_view(), name='house_list'),
    path('catalog/<int:pk>/', HouseDetail.as_view(), name='house_detail'),
]
router = routers.SimpleRouter()
router.register('api/house', HouseViewSet, basename='house')
router.register('api/developer', DeveloperViewSet, basename='developer')

urlpatterns += router.urls
