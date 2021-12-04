from django.db import models


class Shinigami(models.Model):

    first_name = models.CharField(max_length=80, verbose_name="Nombre")
    last_name = models.CharField(max_length=80, verbose_name="Apellido")
    shikai = models.CharField(max_length=80)
    bankai = models.CharField(max_length=80)

    def __str__(self):
        return F"{self.last_name} {self.first_name}"
