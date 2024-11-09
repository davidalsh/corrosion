from django.db import models
from corrosion.models import BaseModel


class CarItem(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CarSegment(CarItem):
    pass


class CarBodyStyle(CarItem):
    pass


class PackageItemType(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class PackageItem(CarItem):
    package_item_type = models.ForeignKey(PackageItemType, on_delete=models.CASCADE, related_name="package_items")

    def __str__(self):
        return f"{self.package_item_type} - {self.name}"


class Car(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    segment = models.ForeignKey(CarSegment, on_delete=models.CASCADE, related_name="cars")
    car_body_styles = models.ManyToManyField(CarBodyStyle, related_name="cars")

    def __str__(self):
        return self.name


class Package(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="packages")
    name = models.CharField(max_length=255)
    package_items = models.ManyToManyField(PackageItem, related_name="packages")

    def __str__(self):
        return f"{self.car} - {self.name}"
