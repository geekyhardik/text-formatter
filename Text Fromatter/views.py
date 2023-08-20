from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def analyze(request):
    param = {}
    dtext = request.POST.get('text', 'default')

    spaceremove = request.POST.get('spaceremove', 'off')
    puncremove = request.POST.get('puncremove', 'off')
    newline = request.POST.get('newline', 'off')
    charcount = request.POST.get('charcount', 'off')
    upper = request.POST.get('upper', 'off')

    if spaceremove == "on":
        analyzed = ""
        for char in dtext:
            if char != " ":
                analyzed = analyzed + char
        param = {'name': 'Removing Space', 'AnalyzedText': analyzed}
        dtext = analyzed

    if puncremove == 'on':
        analyzed = ''
        punctuations = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'name': 'Punctuations Remover', 'AnalyzedText': analyzed}
        dtext = analyzed

    if newline == 'on':
        analyzed = ''
        for char in dtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        param = {'name': 'New line Remover', 'AnalyzedText': analyzed}
        dtext = analyzed

    if upper == "on":
        analyzed = ''
        for char in dtext:
            analyzed = analyzed + char.upper()
        param = {'name': 'New line Remover', 'AnalyzedText': analyzed}
        dtext = analyzed

    if charcount == 'on':
        count = 0
        for char in dtext:
            count += 1
        param = {'name': 'Char counter', 'AnalyzedText': count}

    if (puncremove != "on" and newline != "on" and spaceremove != "on" and upper != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', param)
