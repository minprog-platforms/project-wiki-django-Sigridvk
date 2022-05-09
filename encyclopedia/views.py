from ctypes import sizeof
from logging import PlaceHolder
from os import name
from typing import Text
from django.forms import widgets
from django.forms.widgets import TextInput, Textarea
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
import markdown2
import random

from . import util
import encyclopedia


class NewSearchForm(forms.Form):
    search_term = forms.CharField(label="", widget=TextInput(attrs={'placeholder':'Search Encyclopedia'}))


class NewPageForm(forms.Form):
    title = forms.CharField(label="", widget=TextInput(attrs={'placeholder':'Give Title', 'size':'40', 'required': True,
    'class': 'NewForm'}))
    content = forms.CharField(label="", widget=Textarea(attrs={'placeholder':'Give Text in Markdown', 'rows':5, 'cols':40, 
    'class': 'NewForm', 'id':'content', 'required': True,}))


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
        "form": NewSearchForm()
    })
    else:
        return error(request)

def search_results(request):
    if request.method == "GET":
        form = NewSearchForm(request.GET)

        if form.is_valid():
            possible_entries = []
            search_term = form.cleaned_data["search_term"]
            for entries in util.list_entries():
                if search_term.lower() == entries.lower():
                    return entry(request, search_term)
                elif search_term.lower() in entries.lower():
                    possible_entries.append(entries)

            if len(possible_entries) == 0:
                return render(request, 'encyclopedia/search.html', {
                        "search_term" : search_term,
                        "form": NewSearchForm(),
                        "no_results": True
                    })
            else:
                return render(request, 'encyclopedia/search.html',{
                "entries": possible_entries,
                "form": NewSearchForm(),
                "search_term": search_term
            })
        else:
            return render(request, "{% url: 'index' %}", {
                "form": form
            })
    
    return error(request)

def new(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = f"#{title}\n"
            content += form.cleaned_data["content"]
            if any(title.lower() == te.lower() for te in util.list_entries()):
                return render(request, 'encyclopedia/new.html',{
                    "error":True,
                    "form": NewSearchForm(),
                    "new_form": form
                })
            else:
                util.save_entry(title, content)
                return entry(request, title)

    return render(request, 'encyclopedia/new.html',{
        "form": NewSearchForm(),
        "new_form": NewPageForm()
    })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return entry(request, random_entry)