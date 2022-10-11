
from bancas.views import registrar_banca, total
from bilhetes.views import informacoes_bilhete, registrar_bilhete
from django.contrib import admin
from django.urls import path
from usuarios.views import index

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '',
        index,
        name="index",

    ),

    path(
        'registrar-bilhete/',
        registrar_bilhete,
        name="registrar_bilhete",

    ),
    path(
        'informacoes-bilhete/<int:id>',
        informacoes_bilhete,
        name="informacoes_bilhete",
    ),
    path(
        "registrar-banca/",
        registrar_banca,
        name="registrar_banca"
    ),
    path(
        "bancas/",
        total,
        name="total"
    ),
]
