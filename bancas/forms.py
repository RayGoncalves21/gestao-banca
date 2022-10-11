from django import forms

from bancas.models import Banca


class BancaRegistroForm(forms.ModelForm):

    class Meta:
        model = Banca
        fields = "__all__"


class AtualizaBancaForm(forms.ModelForm):

    class Meta:
        model = Banca
        fields = "__all__"
