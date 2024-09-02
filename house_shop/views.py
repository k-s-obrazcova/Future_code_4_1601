from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets

from house_shop.forms import OrderForm
from house_shop.models import *
from house_shop.serializer import *


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



class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
