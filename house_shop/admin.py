from django.contrib import admin
from .models import *


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    pass


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Development)
class DevelopmentAdmin(admin.ModelAdmin):
    pass


@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(PosDevelopment)
class PosDevelopmentAdmin(admin.ModelAdmin):
    pass
