from filecmp import clear_cache
from re import I
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class MyView(View):
    def get(self, request):
        return render(request, 'main/index.html')
