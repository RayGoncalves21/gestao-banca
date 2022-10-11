from unicodedata import name

from bancas.models import Banca
from django.db import models


class Bilhete(models.Model):

    STATUS_BILHETE = [
        ("AGUARDANDO", "Aguardando"),
        ("GREEN", "Green"),
        ("RED", "Red")

    ]

    status = models.CharField(
        verbose_name='status',
        max_length=194,
        choices=STATUS_BILHETE,
        default="AGUARDANDO"
    )

    time_casa = models.CharField(
        verbose_name="Time jogando em casa",
        max_length=194,
        blank=True,
        null=True

    )

    time_fora = models.CharField(
        verbose_name="Time jogando fora",
        max_length=194,
        blank=True,
        null=True

    )

    valor_aposta = models.IntegerField(
        verbose_name='Valor apostado R$',
    )

    cotacao = models.FloatField(
        verbose_name="Cotação"
    )

    banca_apostada = models.ForeignKey(
        'bancas.Banca',
        verbose_name='Banca que aconteceu a aposta',
        on_delete=models.CASCADE,

    )

    horario_aposta = models.DateTimeField(
        verbose_name='Horario aposta',
        auto_now_add=True
    )

    def get_jogo(self):
        time_home = str(self.time_casa)
        time_away = str(self.time_fora)

        jogo_formatado = f'{time_home} x {time_away}'

        return jogo_formatado

    def get_valor_aposta(self):
        valor = self.valor_aposta

        valor_formatado = f'R$ {valor}'

        return valor_formatado

    def valor_ganho(self):
        valor = self.valor_aposta
        cotacao = self.cotacao

        ganho = valor * cotacao
        ganho_total = "{:.2f}".format(ganho)
        ganho_formatado = f"R$ {ganho_total}"

        return ganho_formatado

    def porcentagem(self):
        valor_aposta = self.valor_aposta
        cotacao = self.cotacao
        lucro = valor_aposta * cotacao

        aumento = lucro - valor_aposta
        percent = aumento / valor_aposta

        percentual = percent * 100

        percentual_formatado = "{:.0f}".format(percentual)

        return f'{percentual_formatado}%'

    def win(self):
        saldo_antigo = Banca.objects.get(Banca.saldo)
        saldo_novo = saldo_antigo + (self.valor_aposta * self.cotacao)
        if self.status == 'GREEN':
            saldo_novo.save()
            return saldo_novo
        return self.saldo_novo

    def loss(self):
        saldo_antigo = Banca.objects.get(Banca.saldo)
        saldo_novo = saldo_antigo - (self.valor_aposta * self.cotacao)
        if self.status == 'RED':
            saldo_novo.save()
            return saldo_novo
        return self.saldo_novo

    class Meta:
        verbose_name = 'Bilhete'
        verbose_name_plural = 'Bilhetes',
        db_table = 'bilhete'

    def __str__(self):
        return self.time_casa
