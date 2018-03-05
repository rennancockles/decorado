# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import DocumentForm
from .models import Document


def index(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            # newdoc = form.save(commit=False)
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            messages.success(request, "Arquivo enviado com sucesso!")

            # return HttpResponseRedirect(newdoc.get_absolute_url())
            return HttpResponseRedirect(reverse('index'))
    else:
        form = DocumentForm

    documentos = Document.objects.all()

    return render(request, 'decorapp/home.html', {'documentos': documentos, 'form': form})
