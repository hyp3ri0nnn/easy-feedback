from rest_framework import serializers
from apps.thank.models import Thank


class ThankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thank
        fields = ("title", "description", "publish_permission", "image")