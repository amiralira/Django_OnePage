from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'rtl/index.html')


def index_view_en(request):
    return render(request, 'original/index.html')