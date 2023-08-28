from rest_framework import serializers
from .models import Todo, Magento
from django.utils import timezone


class TodoSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = '__all__'

    def get_is_expired(self, obj):
        return timezone.now() > obj.created_at + timezone.timedelta(minutes=obj.deadline)


class MagentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magento
        fields = '__all__'
