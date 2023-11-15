from django.db import models
import uuid


class Bedroom(models.Model):
    TYPE_CHOICE = (("E", "Economico"), ("P", "Padrão"), ("L", "Luxuoso"))

    STATUS_CHOICE = (
        ("L", "Limpos"),
        ("O", "Ocupados"),
        ("M", "Em Manutenção"),
        ("D", "Disponivel"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=5, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICE, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, null=False)
