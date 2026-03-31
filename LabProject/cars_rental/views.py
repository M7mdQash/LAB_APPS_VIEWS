from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from password_generator import PasswordGenerator


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def password_generate(request:HttpRequest):
    pwo = PasswordGenerator()
    pwo.minlen = 10

    password = pwo.generate()
    return HttpResponse(f"password is: {password}")