

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from bancas.forms import AtualizaBancaForm, BancaRegistroForm
from bancas.models import Banca


def registrar_banca(request):

    form = BancaRegistroForm()

    if request.method == "POST":
        form = BancaRegistroForm(request.POST)

        if form.is_valid():
            banca = form.save(commit=False)

            banca.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar_banca",
        "form": form
    }

    return render(request, "registrar_banca.html", context)


def informacoes_bancas(request, id):
    banca = get_object_or_404(
        Banca,
        id=id
    )

    form = AtualizaBancaForm()

    if form.is_valid():
        form.save(commit=False)

        form.save()

        return redirect("index")

    context = {
        "nome_pagina": "informacoes banca",
        "banca": banca,
        "form": form
    }
    return render(request, "informacoes_banca.html", context)


def total(request):
    todas_bancas = Banca.objects.all()
    soma = Banca.objects.aggregate(Sum('saldo'))
    soma_total = str(soma['saldo__sum'])
    formatado = f'R$ {soma_total}'

    context = {
        "nome_pagina": "Inicio",
        "soma": soma,
        "soma_total": soma_total,
        "formatado": formatado,
        "todas_bancas": todas_bancas,

    }
    return render(request, "bancas.html", context)
