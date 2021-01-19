from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def open_python(request):
    return render(request,"python.html")