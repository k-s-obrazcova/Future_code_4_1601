# Generated by Django 5.0.6 on 2024-06-20 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pos_parametr',
            options={'verbose_name': 'Характеристика товара', 'verbose_name_plural': 'Характеристики товара'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='buyer_lastname',
            new_name='buyer_firstname',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='agent_lastname',
            new_name='agent_firstname',
        ),
        migrations.RenameField(
            model_name='supply',
            old_name='date_supply',
            new_name='data_supply',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_exists',
        ),
        migrations.AddField(
            model_name='product',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='В наличии?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(max_length=255, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_finish',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(max_length=255, verbose_name='Адрес доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('SH', 'Магазин'), ('CR', 'Курьер'), ('PP', 'Пункт выдачи')], default='SH', max_length=2, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='parametr',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='pos_order',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество продукта'),
        ),
        migrations.AlterField(
            model_name='pos_order',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Скидка на продукт'),
        ),
        migrations.AlterField(
            model_name='pos_order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='pos_parametr',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='parametr',
            field=models.ManyToManyField(through='shop.Pos_parametr', to='shop.parametr', verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='shop.tag', verbose_name='Тег'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='agent_telephone',
            field=models.CharField(max_length=20, verbose_name='Телефон представителя'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
