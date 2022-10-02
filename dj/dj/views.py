from django.http import HttpResponse
from django.shortcuts import render

inf = {"info1": "Я люблю kpop",
       "info2": "Я люблю Дорамы",
       "info3": "Я люблю семью"}


def index(request):
    return HttpResponse("Hello World!")


def main_page(request):
    return render(request, "index.html")


def book(request):
    return render(request, "book.html")


def about(request):
    return render(request, "about.html", context=inf)


def rainbow(request):
    return render(request, "Rainbow.html")
