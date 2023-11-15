from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    JOB_ROLE = (("A", "Atendente"), ("G", "Gerente"), ("AD", "Admin"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, max_length=100)
    job_role = models.CharField(max_length=20, choices=JOB_ROLE, null=False)
