from django.shortcuts import render,redirect

# Create your views here.
def registercustomer(request):
    return render(request,'accounts/registercustomer.html')

def registermanufacturer(request):
    return render(request,'accounts/registermanufacturer.html')

def login(request):
    return render(request,'accounts/login.html')
