from django.shortcuts import render
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


class HouseDetail(DetailView):
    model = House
    template_name = 'house_shop/house/detail.html'


# ___________________ORDER_____________________

class OrderList(ListView):
    model = Order
    template_name = 'house_shop/order/list.html'
    allow_empty = True
    paginate_by = 12


class OrderCreate(CreateView):
    model = Order
    template_name = 'house_shop/order/create.html'
    form_class = OrderForm


class OrderDetail(DetailView):
    model = Order
    template_name = 'house_shop/order/detail.html'


# ___________________SERVICES_____________________
class ServicesList(ListView):
    model = Services
    template_name = 'house_shop/services/list.html'
    allow_empty = True
    paginate_by = 12


class ServicesDetail(DetailView):
    model = Services
    template_name = 'house_shop/services/detail.html'


# ___________________DEVELOPER_____________________
class DeveloperList(ListView):
    model = Developer
    template_name = 'house_shop/developer/list.html'
    allow_empty = True
    paginate_by = 12


class DeveloperDetail(DetailView):
    model = Developer
    template_name = 'house_shop/developer/detail.html'


# _____________________API____________________________________
class RealtorViewSet(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DevelopmentViewSet(viewsets.ModelViewSet):
    queryset = Development.objects.all()
    serializer_class = DevelopmentSerializer


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer


class PosDevelopmentViewSet(viewsets.ModelViewSet):
    queryset = PosDevelopment.objects.all()
    serializer_class = PosDevelopmentSerializer
