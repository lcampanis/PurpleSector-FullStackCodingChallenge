from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import uuid


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    tla = models.CharField(max_length=3, unique=True)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)


class Race(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    lap_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    lap_time = models.FloatField()
