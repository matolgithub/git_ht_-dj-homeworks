from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsAdvertisementOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()

    serializer_class = AdvertisementSerializer

    filterset_class = AdvertisementFilter

    filter_backends = [DjangoFilterBackend]

    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["update", "partial_update", "delete"]:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        return []
