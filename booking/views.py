from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import CustomAccountManager


class Home(View):
    def get(self, request):
        return render(request, "index.html")
