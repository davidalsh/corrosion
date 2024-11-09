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


class Color(CarItem):
    pass


class Rims(CarItem):
    pass


class Upholstery(CarItem):
    pass


class MultimediaSystem(CarItem):
    pass


class Car(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    segment = models.ForeignKey(CarSegment, on_delete=models.CASCADE, related_name="cars")
    car_body_styles = models.ManyToManyField(CarBodyStyle, related_name="cars")

    def __str__(self):
        return self.name


class Package(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="packages")
    name = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color, related_name="package_details")
    rims = models.ManyToManyField(Rims, related_name="package_details")
    upholstery = models.ManyToManyField(Upholstery, related_name="package_details")
    multimedia_systems = models.ManyToManyField(MultimediaSystem, related_name="package_details")

    def __str__(self):
        return f"{self.car} - {self.name}"
