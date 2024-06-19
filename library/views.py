from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def book_list(request):
    list_books = Books.objects.filter(exists=True)
    context = {
        'list_books': list_books
    }
    return render(request, 'library/books/catalog.html', context)

def book_details(request, id):
    book = get_object_or_404(Books, pk = id)
    context = {
        'book_object': book
    }
    return render(request, 'library/books/details.html', context)

def publishing_house_create(request):
    if request.method == "POST":
        form_publishing_house = Publishing_houseForm(request.POST)
        if form_publishing_house.is_valid():
            new_publishing_house = Publishing_house(**form_publishing_house.cleaned_data)
            new_publishing_house.save()
            return redirect('catalog_book_page')
        else:
            context = {
                'form': form_publishing_house
            }
            return render(request, 'library/publishing_house/create.html', context)
    else:
        form_publishing_house = Publishing_houseForm()
        context = {
            'form': form_publishing_house
        }
        return render(request, 'library/publishing_house/create.html', context)

def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('catalog_book_page')
        messages.error(request, 'Что-то пошло не так')
    else:
        form = RegistrationForm()
    return render(request, 'library/auth/registration.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)

            login(request, user)

            print('anonim', request.user.is_anonymous)
            print('auth', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизованы')
            return redirect('catalog_book_page')
        messages.error('Данные заполнены не верно')

    else:
        form = LoginForm()
        return render(request, 'library/auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('log in')

def home(request):
    return render(request, 'library/index.html')

def anonim(request):
    print('is_active:', request.user.is_active)
    print('is_staff:', request.user.is_staff)
    print('is_admin:', request.user.is_superuser)
    print('is_anonim:', request.user.is_anonymous)
    print('is_auth:', request.user.is_authenticated)

    print('Может ли изменять издательство?', request.user.has_perm('library.change_publishing_house'))
    print('Может ли изменять и добавлять издательство?', request.user.has_perms(['library.change_publishing_house',
                                                                                 'library.add_publishing_house']))

    return render(request, 'library/test/anonim.html')

@login_required()
def auth(request):
    return render(request, 'library/test/auth.html')

@permission_required('library.change_publishing_house')
def can_change_publishing_house(request):
    return render(request, 'library/test/change_publishing_house.html')

@permission_required(['library.change_publishing_house', 'library.add_publishing_house'])
def can_add_change_publishing_house(request):
    return render(request, 'library/test/add_change_publishing_house.html')

@permission_required('library.change_only_telephone')
def change_only_telephone(request):
    return render(request, 'library/test/change_only_telephone.html')
