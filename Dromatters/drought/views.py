from django.shortcuts import render
import tensorflow
# Create your views here.



def redi(request):
    return render(request, 'test.html',)
