from logging import PlaceHolder
from os import name
from django.forms.widgets import TextInput
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import markdown2

from . import util


class NewSearchForm(forms.Form):
    search_term = forms.CharField(label="", widget=TextInput(attrs={'placeholder':'Search Encyclopedia'}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : NewSearchForm()
    })

def error(request):
    return render(request, "encyclopedia/error.html", {
        "title": "Error",
        "form":NewSearchForm()
    })

def entry(request, title):
    if any(title.lower() == te.lower() for te in util.list_entries()):
        return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "markdown_text": markdown2.markdown(util.get_entry(title)),
        "form":NewSearchForm()
    })
    else:
        return error(request)

def search_results(request):
    if request.method == "GET":
        form = NewSearchForm(request.GET)

        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            for entries in util.list_entries():
                if search_term.lower() == entries.lower():
                    return entry(request, search_term)
                elif search_term.lower() in entries.lower():
                    pass
        else:
            return render(request, "{% url: 'index' %}", {
                "form": form
            })
    else:
        return error(request)