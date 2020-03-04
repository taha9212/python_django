from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h2>main</h2>")

def index(request):
    return render(request, 'main.html')


def removepunc(request):
    djdata = request.GET.get('data', 'dafault')
    djbutton = request.GET.get('removepunc', 'off')
    print(djdata)
    print(djbutton)
    if djbutton == "on":
        analyze = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        for char in djdata:
            if char not in punctuations:
                analyze = analyze + char
        pm = {'purpose' : 'removing punctuations', 'analyzed' : analyze}
        return render(request, 'remove.html',pm)
    else :
        return HttpResponse ("pls check the button")