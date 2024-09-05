from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets

from house_shop.forms import OrderForm
from house_shop.models import *

from house_shop.serializer import *
from rest_framework import viewsets


# ___________________HOUSE_____________________
class HouseList(ListView):
    model = House
    template_name = 'house_shop/house/list.html'
    allow_empty = True
    paginate_by = 6

    def get_queryset(self):
        return House.objects.filter(is_exists=True)


@method_decorator(login_required(), name='dispatch')
class HouseDetail(DetailView):
    model = House
    template_name = 'house_shop/house/detail.html'


# ___________________ORDER_____________________
@method_decorator(login_required(), name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'house_shop/order/list.html'
    allow_empty = True
    paginate_by = 12


@method_decorator(login_required(), name='dispatch')
class OrderCreate(CreateView):
    model = Order
    template_name = 'house_shop/order/create.html'
    form_class = OrderForm


@method_decorator(login_required(), name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'house_shop/order/detail.html'


# ___________________SERVICES_____________________
@method_decorator(login_required(), name='dispatch')
class ServicesList(ListView):
    model = Services
    template_name = 'house_shop/services/list.html'
    allow_empty = True
    paginate_by = 12


@method_decorator(login_required(), name='dispatch')
class ServicesDetail(DetailView):
    model = Services
    template_name = 'house_shop/services/detail.html'


# ___________________DEVELOPER_____________________
@method_decorator(login_required(), name='dispatch')
class DeveloperList(ListView):
    model = Developer
    template_name = 'house_shop/developer/list.html'
    allow_empty = True
    paginate_by = 12


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('house_shop.view_developer'), name='dispatch')
class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'house_shop/developer/detail.html'


# _____________________API____________________________________
from rest_framework import permissions


class CustomPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class RealtorViewSet(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = [CustomPermissions]


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [CustomPermissions]


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [CustomPermissions]


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [CustomPermissions]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]


class DevelopmentViewSet(viewsets.ModelViewSet):
    queryset = Development.objects.all()
    serializer_class = DevelopmentSerializer
    permission_classes = [CustomPermissions]


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]


class PosDevelopmentViewSet(viewsets.ModelViewSet):
    queryset = PosDevelopment.objects.all()
    serializer_class = PosDevelopmentSerializer
    permission_classes = [CustomPermissions]
