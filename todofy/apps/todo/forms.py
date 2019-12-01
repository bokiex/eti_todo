from django import forms


class TodoForm(forms.Form):
    content = forms.CharField()
