from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request,'pages/index.html')

def our_team(request):
    return render(request,'pages/our_team.html')

@login_required
def customerindex(request):
    return render(request,'pages/customerindex.html')

@login_required
def workerindex(request):
    return render(request,'pages/workerindex.html')
