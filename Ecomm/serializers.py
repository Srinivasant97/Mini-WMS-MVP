from django.db.models import fields
from rest_framework import serializers
from .models import order, Inventory


class InventorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    Lines = serializers.JSONField()

    class Meta:
        model = order
        fields = ("source", "order_number", "Lines")
