from django.shortcuts import render,redirect
from.models import Create
from.forms import CreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as authlogin,logout as authlogout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')
def create(request):
    # frm=CreateForm()
    if request.POST:
        form=CreateForm(request.POST)
        if form.is_valid :
            form.save()
    else:
        form=CreateForm()
    return render(request,"create.html",{'form':form})
    
def list(request):
    list=Create.objects.all()
    print(list)
    return render(request,'list.html',{'do_list':list})

def edit(request,pk): 
    
    edit_instance=Create.objects.get(pk=pk)
    if request.POST:
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        edit_instance.title=title
        edit_instance.desc=desc
        edit_instance.save()
    frm=CreateForm(instance=edit_instance)
    
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
       instance=Create.objects.get(pk=pk)
       instance.delete()
       list=Create.objects.all()
       
       return render(request,'list.html',{'do_list':list})

def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('signup')
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,"User created")
                return redirect('login')
        else:
            messages.info(request,"Password does'nt match")
            return redirect('signup')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        lusername=request.POST.get('lusername')
        lpassword=request.POST.get('lpassword')
        user=authenticate(username=lusername,password=lpassword)
        if user is not None:
            authlogin(request,user)
            messages.info(request,"Logged in")
            return redirect("home")
        else:
            messages.info(request,"Retry")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    authlogout(request)
    return redirect("home")
