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


class PackageItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackageItemType
        fields = ("name",)


class PackageItem(serializers.ModelSerializer):
    package_item_type = serializers.StringRelatedField()

    class Meta:
        model = models.PackageItem
        fields = ("id", "package_item_type", "name", "price")


class PackageSerializer(serializers.ModelSerializer):
    package_items = PackageItem(many=True)

    class Meta:
        model = models.Package
        fields = (
            "id",
            "name",
            "package_items",
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
