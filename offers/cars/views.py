from rest_framework.viewsets import ReadOnlyModelViewSet
from offers.cars.models import Car
from offers.cars.serializers import CarSerializer


class CarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
