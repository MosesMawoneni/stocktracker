from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    shelf_number = models.IntegerField()
    created_at = models.DateTimeField()
    present_quantity = models.IntegerField()
    recent_purchase_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.title} is on shelf number {self.shelf_number}"
