from django.shortcuts import render

# Create your views here.

def index(request):
    print("AAAAAAAAAAAAAAAAAAAAA")
    return render(request, "accounts/index.html")
