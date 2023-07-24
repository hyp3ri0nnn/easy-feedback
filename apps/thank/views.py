from rest_framework import viewsets
from apps.thank.serializers import ThankSerializer
from rest_framework import permissions
from apps.thank.models import Thank
from rest_framework.response import Response


class ThankViewSet(viewsets.ModelViewSet):
    queryset = Thank.objects.all()
    serializer_class = ThankSerializer
    permission_classes = [permissions.AllowAny] 

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        serializer.save()