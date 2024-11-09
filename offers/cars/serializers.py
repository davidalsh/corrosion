from rest_framework import serializers
from offers.cars import models


class BaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "price")


class CarSegmentSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.CarSegment


class CarBodyStyleSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.CarBodyStyle


class ColorSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Color


class RimsSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Rims


class UpholsterySerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.Upholstery


class MultimediaSystemSerializer(BaseItemSerializer):
    class Meta(BaseItemSerializer.Meta):
        model = models.MultimediaSystem


class PackageSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    rims = RimsSerializer(many=True)
    upholstery = UpholsterySerializer(many=True)
    multimedia_systems = MultimediaSystemSerializer(many=True)

    class Meta:
        model = models.Package
        fields = (
            "id",
            "name",
            "colors",
            "rims",
            "upholstery",
            "multimedia_systems",
        )


class CarSerializer(serializers.ModelSerializer):
    segment = CarSegmentSerializer()
    car_body_styles = CarBodyStyleSerializer(many=True)
    packages = PackageSerializer(many=True)

    class Meta:
        model = models.Car
        fields = (
            "id",
            "name",
            "segment",
            "car_body_styles",
            "packages",
        )
