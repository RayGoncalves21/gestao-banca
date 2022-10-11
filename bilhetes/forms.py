from django import forms

from bilhetes.models import Bilhete


class BilheteForm(forms.ModelForm):

    class Meta:
        model = Bilhete
        fields = "__all__"


class AtualizaBilheteForm(forms.ModelForm):
    status_bilhete = forms.ChoiceField(required=True)

    class Meta:
        model = Bilhete
        fields = [
            "status",
        ]
        error_messages = {
            "status": {
                "required": "Por favor, atualize o status do bilhete"
            }
        }
