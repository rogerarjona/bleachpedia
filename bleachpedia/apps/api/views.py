from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Shinigami
from .serializers import ShinigamiSerializer


@csrf_exempt
def shinigami_list(request):
    if request.method != "GET":
        return HttpResponse(status=404)

    shinigamis = Shinigami.objects.all()
    serializer = ShinigamiSerializer(shinigamis, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def shinigami_add(request):
    if request.method != "POST":
        return HttpResponse(status=404, content="404 - Si deseas crear un shinigami, debes utilizar el verbo POST")

    data = JSONParser().parse(request)
    serializer = ShinigamiSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shinigami_detail(request, pk):

    if request.method == "POST":
        return HttpResponse(status=404)

    try:
        shinigami = Shinigami.objects.get(pk=pk)
    except Shinigami.DoesNotExist:
        return HttpResponse(status=404, content="404 - Shinigami no encontrado.")

    if request.method == "GET":
        serializer = ShinigamiSerializer(shinigami)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ShinigamiSerializer(shinigami, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        shinigami.delete()
        return HttpResponse(status=204)



