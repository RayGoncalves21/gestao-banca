

from email.policy import default

from django.db import models


class Banca(models.Model):

    nome_banca = models.CharField(
        verbose_name="Nome da Banca",
        max_length=80,
    )
    saldo = models.DecimalField(
        verbose_name="Saldo",
        default=0,
        max_digits=100,
        decimal_places=2,

    )

    data_registro_banca = models.DateTimeField(
        verbose_name='Data inicio banca',
        auto_now_add=True,
        null=True,
        blank=True,

    )

    class Meta:
        verbose_name = 'Banca',
        verbose_name_plural = 'Bancas',
        db_table = 'banca'

    def __str__(self):
        return self.nome_banca
