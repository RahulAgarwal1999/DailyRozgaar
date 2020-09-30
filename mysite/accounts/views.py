from django.shortcuts import render,redirect

# Create your views here.
def registeruser(request):
    return render(request,'accounts/registeruser.html')

def registerworker(request):
    return render(request,'accounts/registerworker.html')

def loginworker(request):
    return render(request,'accounts/loginworker.html')

def loginuser(request):
    return render(request,'accounts/loginuser.html')
