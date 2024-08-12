from django.shortcuts import render, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import AdminRenderer

from basket.forms import BasketAddProductForm
from shop.forms import ProductFilterForm, SupplierForm
from shop.models import *
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

import datetime

from shop.serializers import *
from shop.utils import CalculateMoney
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import views, viewsets
from rest_framework import permissions


# Create your views here.
def product_list(request):
    list_product = Product.objects.all()
    context = {
        'product_list': list_product
    }
    return render(request, 'shop/product/catalog.html', context)


def product_catalog_with_filter(request):
    list_product = Product.objects.all()
    if request.GET != None:
        product_form = ProductFilterForm(request.GET)
    else:
        product_form = ProductFilterForm()

    if product_form.is_valid():
        if product_form.cleaned_data.get('name') != "":
            list_product = list_product.filter(name__icontains=product_form.cleaned_data.get('name'))
        if product_form.cleaned_data.get('min_price'):
            list_product = list_product.filter(price__gte=product_form.cleaned_data.get('min_price'))
        if product_form.cleaned_data.get('max_price'):
            list_product = list_product.filter(price__lte=product_form.cleaned_data.get('max_price'))
        context = {
            'list_product': list_product,
            'form': product_form,
        }
        return render(request, 'shop/product/catalog_with_filter.html', context)


def get_one_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {
        'product': product,
        'form_basket': BasketAddProductForm
    }
    return render(request, 'shop/product/one_product.html', context)


def get_one_filter_product(request):
    find_product = Product.objects.filter(is_exists=request.GET.get('is_ex'))
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/filter_product.html', context)


def get_more_filter_product(request):
    find_product = Product.objects.filter(
        price__lte=request.GET.get('max_price'),
        price__gt=request.GET.get('min_price')
    )
    context = {
        'find_product': find_product
    }
    return render(request, 'shop/product/filter_product.html', context)


class ListSupplier(ListView):
    model = Supplier
    template_name = 'shop/supplier/supplier_list.html'
    allow_empty = True
    paginate_by = 1


class CreateSupplier(CreateView):
    model = Supplier
    extra_context = {
        'action': 'Создать'
    }
    template_name = 'shop/supplier/supplier_form.html'
    form_class = SupplierForm


class DetailSupplier(DetailView):
    model = Supplier
    template_name = 'shop/supplier/supplier_detail.html'


class UpdateSupplier(UpdateView):
    model = Supplier
    form_class = SupplierForm

    extra_context = {
        'action': 'Изменить'
    }
    template_name = 'shop/supplier/supplier_form.html'


class DeleteSupplier(DeleteView):
    model = Supplier
    # по умолчанию: название_приложения/название_model + _form.html
    template_name = 'shop/supplier/supplier_cofirm_delete.html'
    success_url = reverse_lazy('product_list_filter')


class OrderDetail(DetailView, CalculateMoney):
    model = Order
    template_name = 'shop/order.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        order = context.get('object')

        list_price = [pos_order.sum_price_count() for pos_order in order.pos_order_set.all()]

        context['sum_price'] = self.sum_price(prices=list_price)
        return context


def test_json(request):
    return JsonResponse({
        'massage': 'Данные в виде JSON',
        'product': reverse_lazy('product_list_filter'),
    })


@api_view(['GET', 'POST'])
def order_api_list(request, format=None):
    if request.method == 'GET':
        order_list = Order.objects.all()
        serializer = OrderSerializer(order_list, many=True)
        print(serializer.data)

        return Response({'orders': serializer.data})
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_api_detail(request, pk, format=None):
    order_obj = get_object_or_404(Order, pk=pk)
    if order_obj:
        if request.method == 'GET':
            serializer = OrderSerializer(order_obj)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = OrderSerializer(order_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response({'message': 'Данные успешно обновлены', 'order': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            order_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class PaginationPage(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 1


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


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationPage


class ProductViewSetDif(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductSerializer
        return ProductSerializerSimple


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermissions]


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ParametrViewSet(viewsets.ModelViewSet):
    queryset = Parametr.objects.all()
    serializer_class = ParametrSerializer


class Pos_parametrViewSet(viewsets.ModelViewSet):
    queryset = Pos_parametr.objects.all()
    serializer_class = Pos_parametrSerializer


class Pos_orderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = Pos_orderSerializer


class Pos_supplyViewSet(viewsets.ModelViewSet):
    queryset = Pos_supply.objects.all()
    serializer_class = Pos_supplySerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SupplierAdminViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    renderer_classes = [AdminRenderer]


def template_filter_django(request):
    context = {
        'digit': 84,
        'stringText': "SSome.Text Sew test http://127.0.0.1:8000/shop/filter/",
        'bool': True,
        'boolSecond': False,
        'datetimeNow': datetime.datetime.now(),
        'var1': 'Var',
        'var2': '',
        'var3': None,
        'dict_col': [
            {'name': 'Karina', 'price': 8900},
            {'name': 'Alice', 'price': 19785},
            {'name': 'Sam', 'price': 4000},
        ]
    }
    return render(request, 'shop/test_filter_tags/filters.html', context=context)
