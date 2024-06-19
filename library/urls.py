from django.urls import path
from .views import *

urlpatterns = [
    path('books/', book_list, name='catalog_book_page'),
    path('books/details/<int:id>/', book_details, name='details_book_page'),
    path('publishing_house/create/', publishing_house_create, name='create_publishing_house_page'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('index/', home, name='home_page'),
    path('anonim/', anonim, name='anonim'),
    path('auth/', auth, name='auth'),
    path('can_change_publishing_house/', can_change_publishing_house, name='change_house'),
    path('can_add_change_publishing_house/', can_add_change_publishing_house, name='add_change_house'),
    path('change_only_telephone/', change_only_telephone, name='telephone'),

]