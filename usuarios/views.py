
from bancas.models import Banca
from bilhetes.models import Bilhete
from django.contrib import messages
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

    todas_bancas = Banca.saldo

    context = {
        "nome_pagina": "Inicio",
        'todos_bilhetes': todos_bilhetes,
        "bilhetes_aguardando": bilhetes_aguardando.count(),
        "bilhetes_green": bilhetes_green.count(),
        "bilhetes_red": bilhetes_red.count(),
        "todas_bancas": todas_bancas


    }
    return render(request, "index.html", context)
