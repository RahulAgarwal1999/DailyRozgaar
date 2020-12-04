from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import UserDetails,WorkerDetails,Service,ServiceHistory
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
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
        # address = request.POST.get('address')

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request,'That username is already taken')
                return redirect('registeruser')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.is_staff=False;
                user.is_superuser=False;
                user.save()

                u_id = User.objects.get(username=username)
                addusr = UserDetails(user_id=u_id,number=number)
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
        # address = request.POST.get('address')
        cardtype = request.POST.get('cardtype')
        cardnumber = request.POST.get('cardnumber')

        if password == password2:
            if User.objects.filter(username=username).exists():
                # messages.error(request,'That username is already taken')
                return redirect('registerworker')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.is_staff=True;
                user.is_superuser=False;
                user.save()

                u_id = User.objects.get(username=username)
                addusr = WorkerDetails(user_id=u_id,number=number,job=job,cardtype=cardtype,cardnumber=cardnumber)
                addusr.save()

                # messages.success(request,'You are now registered and can log in')
                return redirect('loginworker')

    return render(request,'accounts/registerworker.html')

def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboardadmin')
        else:
            # messages.error(request,"Invalid Credentials")
            return redirect('loginadmin')
    else:
        return render(request,'accounts/loginadmin.html')

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

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


@login_required
def dashboardadmin(request):
    user = request.user
    servicelist = Service.objects.order_by('-list_date')
    paginator = Paginator(servicelist,10)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)

    count = Service.objects.count()
    context = {
        'list':paged_list,
        'count':count,
    }
    return render(request,'adminpages/dashboardadmin.html',context)

@login_required
def adminrfqreceived(request):
    user = request.user
    servicelist = Service.objects.order_by('-list_date')
    paginator = Paginator(servicelist,10)
    page = request.GET.get('page')
    paged_list = paginator.get_page(page)

    count = Service.objects.count()
    context = {
        'list':paged_list,
        'count':count,
    }
    return render(request,'adminpages/adminrfqreceived.html',context)

@login_required
def dashboarduser(request):
    user=request.user
    if request.method == 'POST':
        service = request.POST['service']
        adetails = request.POST['details']
        time = request.POST['time']
        number = request.POST['contact']
        email = request.POST['email']
        addressl1 = request.POST['addressl1']
        addressl2 = request.POST['addressl2']
        city = request.POST['city']
        state = request.POST['state']
        code = request.POST['code']

        user = request.user
        data = Service(user_id=user,service=service,adetails=adetails,time=time,number=number,email=email,addressl1=addressl1,addressl2=addressl2,state=state,city=city,code=code)
        data.save()

        history=ServiceHistory(user_id=user,service=service,adetails=adetails,time=time,addressl1=addressl1,addressl2=addressl2,state=state,city=city,code=code)
        history.save()

        return redirect(request.path_info)

    data = UserDetails.objects.get(user_id=user)
    context={
    'data':data,
    }
    return render(request,'accounts/dashboarduser.html',context)

@login_required
def userHistory(request):
    user=request.user
    data=ServiceHistory.objects.filter(user_id=user).order_by('-list_date')
    context={
        'data':data
    }
    return render(request,'accounts/user_service_history.html',context)



@login_required
def accountsettingsuser(request):
    if request.method=='POST':
        contact = request.POST['contact']
        addressl1 = request.POST['addressl1']
        addressl2 = request.POST['addressl2']
        city = request.POST['city']
        state = request.POST['state']
        code = request.POST['code']

        user = request.user

        Data = UserDetails.objects.get(user_id=user)
        Data.number = contact
        Data.addressl1 = addressl1
        Data.addressl2 = addressl2
        Data.city = city
        Data.state = state
        Data.code = code

        Data.save()
        return redirect(request.path_info)

    user = request.user
    data = UserDetails.objects.get(user_id=user)
    context = {
        'data':data
    }

    return render(request,'accounts/accountsettingsuser.html',context)



@login_required
def dashboardworker(request):
    if request.user.is_staff and not request.user.is_superuser:
        user = request.user
        if request.method == 'POST':
            if 'status' in request.POST:
                status = request.POST['status']
                data = WorkerDetails.objects.get(user_id = user)
                data.status = status
                data.save()
                return redirect(request.path_info)

        data = WorkerDetails.objects.get(user_id = user)
        context = {
            'data':data,
        }
        return render(request,'accounts/dashboardworker.html',context)

def accountsettingsworker(request):
    return render(request,'accounts/accountsettingsworker.html')
