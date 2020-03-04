#i have created this file - Taha
from django.http import HttpResponse


#till video 6 
# def index(request):
#     return HttpResponse("""<a href = https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9
#     ah7DDtYtflgwMwpT3xmjXY9&index=7> Code with harry django</a> """)

# def about(request):
#     return HttpResponse("Hello World <h2>about</h2>")

# def txt(request):
#     file = open('E:\\Taha\\django\\textutils\\textutils\\textutils\\hello.txt', 'r')
#     return HttpResponse(file.read())

def index(request):
    return HttpResponse("<h1>Home</h1>")

def removepunc(request):
    return HttpResponse("""remove Punc    <button> <a href = http://127.0.0.1:8000/>BACK 
    </a></button>""")


def capitalize(request):
    return HttpResponse("""Capitalize    <button> <a href = http://127.0.0.1:8000/>BACK 
    </a></button>""")