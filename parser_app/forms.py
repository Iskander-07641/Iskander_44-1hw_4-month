from django import forms


class ParseForm(forms.Form):
    url = forms.URLField(label='URL для парсинга', required=True)
