
from bancas.models import Banca
from bilhetes.models import Bilhete
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseNotAllowed
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.utils import timezone


def index(request):

    todos_bilhetes = Bilhete.objects.all()
    bilhetes_aguardando = todos_bilhetes.filter(
        status="AGUARDANDO"
    )
    bilhetes_green = todos_bilhetes.filter(
        status="GREEN"
    )
    bilhetes_red = todos_bilhetes.filter(
        status="RED"
    )

    soma = Banca.objects.aggregate(Sum('saldo'))
    soma_total = str(soma['saldo__sum'])
    formatado = f'R$ {soma_total}'

    context = {
        "nome_pagina": "Inicio",
        'todos_bilhetes': todos_bilhetes,
        "bilhetes_aguardando": bilhetes_aguardando.count(),
        "bilhetes_green": bilhetes_green.count(),
        "bilhetes_red": bilhetes_red.count(),

        "soma": soma,
        "soma_total": soma_total,
        "formatado": formatado,

    }
    return render(request, "index.html", context)
