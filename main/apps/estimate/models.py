from django.db import models
from main.apps.management.models import Equipment
from main.apps.user.models import User


def estimate_number_generator(estimate_id):
    estimate = Estimate.objects.get(id=estimate_id)
    estimator_long_id = estimate.created_by.id + 100
    estimate_date_created = str(estimate.created_at).replace('-', '')[2:8]
    return estimate_date_created + str(estimator_long_id) + str(estimate.id).zfill(3)


class Estimate(models.Model):
    note = models.TextField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    archive = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return estimate_number_generator(self.id)


class EstimateEquipment(models.Model):
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, blank=False, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, blank=False)
    quantity = models.FloatField(blank=False)
    price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return estimate_number_generator(self.estimate.id) + " " + self.equipment.name
