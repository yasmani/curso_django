from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    fecha_nacimiento = models.DateField(null=True, blank=True)


    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuario_set",  # Evita conflicto con la tabla auth_user_groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuario_permissions_set",  # Evita conflicto con auth_user_user_permissions
        blank=True,
    )

    class Meta:
        permissions = []
    def __str__(self):
        return self.username

