from django.contrib import admin
from offers.cars.models import (
    Car,
    CarSegment,
    CarBodyStyle,
    Package,
    Upholstery,
    MultimediaSystem,
    Color,
    Rims,
)

models = (
    Car,
    CarSegment,
    CarBodyStyle,
    Upholstery,
    MultimediaSystem,
    Color,
    Rims,
)


admin.site.register(models)


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    ordering = ("car__name", "name")
