from django import forms
from .models import packagedetails
class packageForm (forms.ModelForm):
    class Meta:
        model= packagedetails
        fields = "__all__"
        exclude = ['user', ]
        

class inviteform(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email        