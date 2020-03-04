from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def remove(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
    get_data = request.GET.get('data', 'empty')
    get_option = request.GET.get('RPoption', 'off')
    get_option_cap = request.GET.get('cap', 'off')
    get_option_nlr  = request.GET.get('newlineremover', 'off')
    get_option_esr = request.GET.get('extraspaceremover', 'off')
    print(get_data)
    if get_option == 'on':
        analyzing = ""
        for char in get_data:
            if char not in punctuations:
                analyzing = analyzing + char
        para = {'before' : get_data, 'After' : analyzing}
        return render(request,'remove.html', para)
    elif get_option_cap == 'on':
        analyzing = get_data.upper()
        para = {'before' : get_data, 'After' : analyzing}
        return render(request, 'remove.html', para)
    elif  get_option_nlr == 'on':
        analyzing = ""
        for char in get_data:
            if char != "\n":
                analyzing = analyzing + char
        para = {'before' : get_data, 'After' : analyzing}
        return render(request, 'remove.html', para)
    elif get_option_esr == 'on':
        analyzing = ""
        for index, char in enumerate(get_data):
            if get_data[index] == " " and get_data[index +1] == " ":
                pass
            else:
                analyzing = analyzing + char
                para = {'before' : get_data, 'After' : analyzing}
        return render(request, 'remove.html', para)

    else:
        return HttpResponse('You didnt check any box')
