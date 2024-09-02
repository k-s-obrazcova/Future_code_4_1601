from django.db import models
from django.urls import reverse_lazy

MAX_LENGTH = 255


class Developer(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Застройщик'
        verbose_name_plural = 'Застройщики'


class Services(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название услуги для дома')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class House(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    size = models.CharField(max_length=MAX_LENGTH, verbose_name='Размер')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания объявления')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления объявления')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    developer = models.ForeignKey(Developer, on_delete=models.PROTECT, verbose_name='Застройщик')
    service = models.ManyToManyField(Services, blank=True, null=True, verbose_name='Услуга')

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'


class Realtor(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    phone = models.CharField(max_length=16, verbose_name='Телефон')
    city = models.CharField(max_length=MAX_LENGTH, verbose_name='Город')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес работы')
    is_exists = models.BooleanField(default=True, verbose_name='Возможность взаимодействия')

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        verbose_name = 'Риэлтор'
        verbose_name_plural = 'Риэлторы'


class Order(models.Model):
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    comment = models.CharField(null=True, blank=True, verbose_name='Комментарий')
    building_time_start = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала строительства')
    building_time_finish = models.DateTimeField(verbose_name='Дата окончания строительства')
    key_time = models.DateTimeField(verbose_name='Дата выдачи ключей')

    house = models.ManyToManyField(House, through='PosOrder', verbose_name='Дом')
    realtor = models.ForeignKey(Realtor, on_delete=models.PROTECT, verbose_name='Риэлтор')

    def __str__(self):
        return f"№{self.pk} ({self.buyer_name} {self.buyer_firstname} - {self.house.name}) ({self.realtor.name})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Development(models.Model):
    date_development = models.DateTimeField(verbose_name='Дата постройки')
    developer = models.ForeignKey(Developer, on_delete=models.PROTECT, verbose_name='Застройщик')
    house = models.ManyToManyField(House, through='PosDevelopment', verbose_name='Дом')

    def __str__(self):
        return f'№{self.pk} - {self.date_development} {self.developer.name}'

    class Meta:
        verbose_name = 'Застройка'
        verbose_name_plural = 'Застройки'


class PosOrder(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, verbose_name='Дом')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')

    def __str__(self):
        return f'№{self.pk} {self.house.name} ({self.order.buyer_firstname} {self.order.buyer_name})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'


class PosDevelopment(models.Model):
    house = models.ForeignKey(House, on_delete=models.PROTECT, verbose_name='Дом')
    development = models.ForeignKey(Development, on_delete=models.PROTECT, verbose_name='Застройка')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.house.name} - №{self.development.pk}'

    class Meta:
        verbose_name = 'Позиция застройки'
        verbose_name_plural = 'Позиции застроек'
