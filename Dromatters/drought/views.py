from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect


def redi(request):
    return render(request, 'test.html',)
