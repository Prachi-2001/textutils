from django.http import HttpResponse
from django.shortcuts import render
import datetime

def Home(request):
    return render(request,'index1.html')


def about(request):
    file = open("textutils\one.txt",'r')
    return HttpResponse(file.read())


def analyse(request):
    # this below line print the data of text
    date = datetime.datetime.now()
    djtext = request.GET.get('some','default')
    text = request.GET.get('some','default')
    removepunc = request.GET.get('removepunc','off')
    capfirst = request.GET.get('capfirst','off')
    removespace = request.GET.get('removespace','off')
    removenewline = request.GET.get('removenewline','off')
    charcount = request.GET.get('charcount','off')
    capwhole = request.GET.get('capwhole','off')

    # for remove punctuations
    if removepunc=="on":
        punctuations = '''!()-[]{};:='"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char

        djtext = analysed
        

    # capitalise first 
    if capfirst=="on":
        analysed = djtext.title()
        djtext = analysed

    if charcount=="on":
        Charcount = 0
        for char in djtext:
            if char!=" ":
                Charcount = Charcount + 1
    
        param = {'analysed_text': Charcount}
        return render(request,'analyse.html',param) 

    if capwhole=="on":
        analysed = djtext.upper()
        djtext = analysed

    if removenewline=="on":
        analysed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analysed = analysed + char
    
        djtext = analysed

    if removespace=="on":
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
              analysed = analysed + char
    
    param = {'analysed_text': analysed, 'text' : text}
    return render(request,'analyse.html',param)         


# def capfirst(request):
#     return HttpResponse("capfirst")