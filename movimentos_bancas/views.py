from unicodedata import name

from bancas.models import Banca
from django.shortcuts import render

from .models import Banca_entrada


class Entrada(self):
    def registrar_entrada(self):
        saldo_antigo = Banca.objects.get(name='saldo')
        saldo_novo = Banca_entrada.objects.get(name='valor_da_entrada')
        saldo_novo.valor_da_entrada += saldo_antigo.saldo

        saldo_antigo.save()

        return self.valor_da_entrada

    def __str__(self):
        return f'{str(self.valor_da_entrada)}'
