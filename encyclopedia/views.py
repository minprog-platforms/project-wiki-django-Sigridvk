from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    if any(title.lower() == t.lower() for t in util.list_entries()):
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "markdown_text": markdown2.markdown(util.get_entry(title))
    })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": "Error"
        })
