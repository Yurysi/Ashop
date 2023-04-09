from django.shortcuts import render

def index(request):
    return render(request, "core/index.html")

def contact(request):
    return render(request, "core/contact.html")

def blog(request):
    return render(request, "core/blog.html")
