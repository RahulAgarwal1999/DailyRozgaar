from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def our_team(request):
    return render(request,'pages/our_team.html')
