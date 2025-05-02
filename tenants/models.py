from django.db import models

# Create your models here.
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Modelo Tenant
class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trial = models.BooleanField(default=True)

    auto_create_schema = True  # Django-tenants lo crea automáticamente

# Modelo Domain (subdominios o dominios para cada tenant)
class Domain(DomainMixin):
    pass
