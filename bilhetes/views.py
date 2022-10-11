from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from bilhetes.forms import AtualizaBilheteForm, BilheteForm
from bilhetes.models import Bilhete


def registrar_bilhete(request):

    form = BilheteForm()

    if request.method == "POST":
        form = BilheteForm(request.POST)

        if form.is_valid():
            bilhete = form.save(commit=False)

            bilhete.save()

            messages.success(
                request,
                'Bilhete Registrado com sucesso'
            )

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Bilhete",
        "form": form
    }

    return render(request, 'registrar_bilhete.html', context)


def informacoes_bilhete(request, id):

    bilhete = get_object_or_404(
        Bilhete,
        id=id
    )

    form = AtualizaBilheteForm()

    if request.method == "POST":
        form = AtualizaBilheteForm(
            request.POST,
            instance=bilhete
        )

        if form.is_valid():

            form.save(commit=False)

            bilhete.status = ("AGUARDANDO", "GREEN", "RED")

            bilhete.save()

            messages.success(
                request,
                "Bilhete atualizado com sucesso"
            )

            return redirect("index")
        else:

            return HttpResponseNotAllowed(
                ["POST"],
                "Método Não permitido"
            )

    context = {
        "nome_pagina": "Informações Bilhetes",
        "bilhete": bilhete,
        "form": form
    }

    return render(request, "informacoes_bilhete.html", context)
