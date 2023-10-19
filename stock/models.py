from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    title = models.CharField(max_length=255)
    shelf_number = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField()
    present_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    recent_purchase_quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.title} is on shelf number {self.shelf_number}"


class StorePersonnelProfile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="profiles"
    )
    role = models.CharField(max_length=255)
    is_present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} our {self.role} {self.is_present}"


class Worker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="workers"
    )
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Issue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="issues")
    store_clerk = models.ForeignKey(
        StorePersonnelProfile, on_delete=models.PROTECT, related_name="issues"
    )
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    quantity_issued = models.IntegerField(validators=[MinValueValidator(1)])
    date_issued = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"{self.quantity_issued} {self.item.title} was issued on {self.date_issued}"
        )
