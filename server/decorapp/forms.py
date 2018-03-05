# -*- coding: utf-8 -*-

from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ["docfile"]
        labels = {"docfile": "Selecione o arquivo"}
