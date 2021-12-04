import requests

from django.shortcuts import render
from django.urls import reverse


def list(request):
    try:
        url = F"{request.scheme}://{request.get_host()}{reverse('shinigami_list')}"
        response = requests.get(url, timeout=15)
        response = response.json()
    except Exception as e:
        response = []

    return render(request, "list.html", {"response": response})
