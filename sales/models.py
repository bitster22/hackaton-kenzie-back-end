from django.db import models
import uuid

class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    disccount = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()