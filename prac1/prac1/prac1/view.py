from django.http import HttpResponse
from django.shortcuts import render

# def main(request):
#     return HttpResponse("<h1>main</h1>")

def main(request):
    param = {'name' : 'taha', 'place' : 'unknown'}
    return render (request, 'main.html', param)