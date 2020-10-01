from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import UserDetails,WorkerDetails
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def registeruser(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        number = request.POST.get('number2')
        address = request.POST.get('address')

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request,'That username is already taken')
                return redirect('registeruser')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()

                u_id = User.objects.get(username=username)
                addusr = UserDetails(user_id=u_id,number=number,address=address)
                addusr.save()

                # messages.success(request,'You are now registered and can log in')
                return redirect('loginuser')

    return render(request,'accounts/registeruser.html')



def registerworker(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        number = request.POST.get('number')
        job = request.POST.get('job')
        address = request.POST.get('address')
        cardtype = request.POST.get('cardtype')
        cardnumber = request.POST.get('cardnumber')

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request,'That username is already taken')
                return redirect('registeruser')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()

                u_id = User.objects.get(username=username)
                addusr = WorkerDetails(user_id=u_id,number=number,address=address,job=job,cardtype=cardtype,cardnumber=cardnumber)
                addusr.save()

                # messages.success(request,'You are now registered and can log in')
                return redirect('loginuser')

    return render(request,'accounts/registerworker.html')


def loginworker(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboardworker')
        else:
            # messages.error(request,"Invalid Credentials")
            return redirect('loginworker')
    else:
        return render(request,'accounts/loginworker.html')


def loginuser(request):
    return render(request,'accounts/loginuser.html')

@login_required
def dashboardworker(request):
    return render(request,'accounts/dashboardworker.html')

@login_required
def dashboardcustomer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboarduser')
        else:
            # messages.error(request,"Invalid Credentials")
            return redirect('loginuser')
    else:
        return render(request,'accounts/loginuser.html')

def dashboarduser(request):
    return render(request,'accounts/dashboarduser.html')

def dashboardworker(request):
    return render(request,'accounts/dashboardworker.html')
