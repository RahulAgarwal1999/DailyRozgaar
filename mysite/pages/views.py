from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def customerindex(request):
    return render(request,'pages/customerindex.html')
