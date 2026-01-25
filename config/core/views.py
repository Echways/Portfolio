from django.http import JsonResponse
from django.shortcuts import render


def healthcheck_view(request):
    return JsonResponse({"status": "ok"})


def handler404(request, exception):
    response = render(request, "404.html", status=404)
    return response


def handler500(request):
    response = render(request, "500.html", status=500)
    return response
