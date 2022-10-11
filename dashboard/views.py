from bilhetes.models import Bilhete
from django.shortcuts import render


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

    context = {
        "nome_pagina": "Inicio da dashboard",
        'todos_bilhetes': todos_bilhetes.count(),
        "bilhetes_aguardando": bilhetes_aguardando.count(),
        "bilhetes_green": bilhetes_green.count(),
        "bilhetes_red": bilhetes_red.count(),


    }

    return render(request, "index.html", context)
