from django.shortcuts import render

# Create your views here.


def redi(request):
    return render(request, 'test.html',)
