from django.contrib import admin
from offers.cars.models import (
    Car,
    CarSegment,
    CarBodyStyle,
    Package,
    PackageItem,
    PackageItemType,
)

models = (
    Car,
    CarSegment,
    CarBodyStyle,
    PackageItemType,
)


admin.site.register(models)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    ordering = ("car__name", "name")


@admin.register(PackageItem)
class PackageItemAdmin(admin.ModelAdmin):
    ordering = ("package_item_type", "name")
