from django.db import models
import uuid

class BedroomBook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    check_in = models.DateField(auto_now_add=True)
    check_out = models.DateField()
    booked = models.BooleanField(default=False)
