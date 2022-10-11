from bancas.models import Banca
from django.db import models


class Banca_entrada(models.Model):

    selecionar_banca = models.ForeignKey(
        Banca,
        on_delete=models.CASCADE,
        verbose_name='Selecione a banca',
    )

    valor_da_entrada = models.DecimalField(
        verbose_name='Valor da entrada',
        max_digits=100,
        decimal_places=2,
        null=True,
        blank=True


    )

    class Meta:
        verbose_name = 'Banca Entrada',
        verbose_name_plural = 'Entradas bancas',
        db_table = 'banca_entrada'

    def __str__(self):
        return f'{str(self.valor_da_entrada)}'
