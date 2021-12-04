import requests

from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import ShinigamiForm
from bleachpedia.apps.api.models import Shinigami


def list(request):
    try:
        url = F"{request.scheme}://{request.get_host()}{reverse('shinigami_list')}"
        response = requests.get(url, timeout=15)
        response = response.json()
    except Exception as e:
        response = []

    return render(request, "list.html", {"response": response})


def add(request):
    form = ShinigamiForm(request.POST or None)
    return render(request, "add.html", {})


def update(request, pk):
    instance = get_object_or_404(Shinigami, id=pk)
    form = ShinigamiForm(request.POST or None)

    return render(request, "add.html", {})