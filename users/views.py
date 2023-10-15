from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth import authenticate,login
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import sched, time
import threading



def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.error(request, "we can't find this account! kindly signup.")
            return redirect('users:signin')

        user = authenticate(username = username, password = password)
        print(user)
        if user is None:
            messages.error(request, 'Wrong password.')
            return redirect('users:signin')
        
        login(request , user)
        
        #if profile_obj.is_completed == False:
 
        return redirect('users:profile')

    return render(request , 'login.html')

def register(request):
    form = NewUserForm()
    
    # usernames = []
    # allusers = User.objects.all()
    # usern = allusers.values('username')
    # for keys in usern:
    #     usernames.append(keys['username'])
    
    if request.method =='POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user_obj = User(username = username , password=password)
            user_obj.set_password(password)
            #user_obj.save()
            
            profile_obj = Profile.objects.create(userid = user , amount=100)
            profile_obj.save()
            
            return redirect('/accounts/login')
        else:
            messages.error(request, 'account not created for some reasons')
        
    context={
        'form':form,
    }
    return render(request,'register.html',context)

# def do_something(scheduler):
#     scheduler.enter(60, 1, do_something, (scheduler,))
#     print("doing stuff...")


# def my_function():
#     numlist = []
#     num = 100
#     num = num - 10
#     numlist.append(num)
#     print(numlist)
#     return numlist

# def run_function():
    
#     thread = threading.Timer(60.0, run_function) # 60 seconds = 1 minute
#     thread.start()
#     numlist = my_function()
#     return numlist
    



@login_required
def profile(request):
    current_user = User.objects.get(id=request.user.id)
    profile_obj = Profile.objects.filter(userid =current_user)

    amountlist = []
    timelist = []
    
    
    print(amountlist)
    print(timelist)
    
    for data in profile_obj.all():
        amountlist.append(data.amount)
        
        
    for i in range(len(amountlist)):
        timelist.append((i+1)*60)
    
    if request.method == 'POST':
        amount = request.POST['amount']
        # time = request.POST['time']

        newdata = Profile.objects.create(userid = current_user, amount=amount)
        newdata.save()
        
    context = {
        'profile_obj' : profile_obj,
        'amountlist' : amountlist,
        'timelist': timelist,
        'data' : current_user
    }
    
    return render(request, 'profile.html', context)