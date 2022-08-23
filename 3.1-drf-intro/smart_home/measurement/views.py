from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


# Создание датчика. Указываются поля: название, описание датчика.
class CreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        new_data = SensorDetailSerializer(data=request.data)
        new_data.save()

        return Response({'status': 'OK'})


# Получение списка датчиков.
class ListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Получение информации по конкретному датчику.
class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # Изменение данных датчика. Указываются название и/или описание.
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        serializer.save()

        return Response(serializer.data)


# Добавление измерения. Указываются поля: ID датчика, температура.
class ListCreateAPIView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        new_data = MeasurementSerializer(data=request.data)
        new_data.save()

        return Response({'status': 'OK'})
