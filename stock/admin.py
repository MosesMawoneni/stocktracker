from django.contrib import admin


from . import models


# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "shelf_number",
        "created_at",
        "present_quantity",
        "recent_purchase_quantity",
    ]

    search_fields = ["title", "shelf_number"]


@admin.register(models.StorePersonnelProfile)
class StorePersonnelProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "role", "is_present"]
    autocomplete_fields = ["user"]
    search_fields = ["role"]


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "item",
        "store_clerk",
        "worker",
        "quantity_issued",
        "date_issued",
        "description",
    ]
    autocomplete_fields = ["item", "store_clerk", "worker"]
    search_fields = ["item", "store_clerk", "worker"]


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "role"]
    autocomplete_fields = ["user"]
    search_fields = ["user", "name", "role"]
