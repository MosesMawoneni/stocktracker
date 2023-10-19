from rest_framework import serializers

from .models import Issue, Item, StorePersonnelProfile, Worker


class ItemShowAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "title",
            "shelf_number",
            "created_at",
            "present_quantity",
            "recent_purchase_quantity",
        ]


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["user", "name", "role"]


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorePersonnelProfile
        fields = ["user", "role", "is_present"]


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "item",
            "store_clerk",
            "worker",
            "quantity_issued",
            "date_issued",
            "description",
        ]
