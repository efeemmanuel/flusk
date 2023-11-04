from django.shortcuts import render, redirect , get_object_or_404
app_name="appusers"
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

#from .forms import CustomerInfoForm
from django.contrib.auth.decorators import login_required

from payments.decorators import verified_required
from payments.models import *
from .forms import *


# Create your views here.



def index(request):
    return render(request, 'index.html')
    
    
    
    
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})

   
   
   
def user_login(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request,'registration/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('/')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'registration/login.html',{'form': form})
   


def course(request):
    item_count = beginners_class.objects.count()
    items_count = advance_class.objects.count()
    data = {'item_count': item_count, 'items_count': items_count}
    return render(request, 'course.html', data)
    
    
def freeclass(request):
    beginners = beginners_class.objects.all()
    data = {'beginners':beginners}
    return render(request, 'freeclass.html',data)
    

def freecourse(request, id):
    beginners = beginners_class.objects.all()
    details = beginners_class.objects.get(id=id)
    data = {'beginners':beginners, 'details':details}
    return render(request, 'freecourse.html',data)
    
   
   
@login_required
def advanceclass(request):
    advance = advance_class.objects.all()
    user = request.user
    user_has_verified_payment = Payment.objects.filter(user=user, verified=True).exists()
    data = {'advance':advance, 'user_has_verified_payment': user_has_verified_payment,}
    return render(request, 'advanceclass.html',data)
    
    
@verified_required
def advancecourse(request, id):
    advance = advance_class.objects.all()
    advance_details = advance_class.objects.get(id=id)
    data = {'advance_details':advance_details, 'advance':advance}
    return render(request, 'advancecourse.html',data)
    
    
def dashboard(request):
    user = request.user
    user_has_verified_payment = Payment.objects.filter(user=user, verified=True).exists()
    
    data={'user_has_verified_payment': user_has_verified_payment}
    return render(request, 'dashboard.html', data)
    

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            a = (request.POST['name'])
            b = (request.POST['email'])
            c = (request.POST['phone_number'])
            d = (request.POST['message'])
            g = Contact(name=a,email=b,phone_number=c,message=d)
            g.save()
            messages.success(request, 'Message sent successfully')
            return redirect('/')
    data= {'forms':form,}
    return render(request, 'contact.html', data)
