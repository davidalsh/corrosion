from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from offers.cars.models import Car, PackageItemType
from offers.cars.serializers import CarSerializer, PackageItemTypeSerializer


class CarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=False, methods=['GET'])
    def get_package_item_types(self, request):
        return Response(PackageItemTypeSerializer(PackageItemType.objects.all(), many=True).data)
