from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import ContactForm
from django import forms

def logoutUser(req):
    logout(req)
    return redirect('home:login')


def signup(req):
    if req.method == 'POST':
        new_user = User.objects.create_user(
            username=req.POST.get('username'),
            email=req.POST.get('email'),
            password=req.POST.get('password'),
            first_name=req.POST.get('fname'),
            last_name=req.POST.get('lname')
        )
        return redirect('home:login')
    else:
        return render(req, 'home/signup.html')

def loginUser(req):
    if req.method=='POST':
        user = authenticate(
            username=req.POST.get('username'),
            password=req.POST.get('password')
        )
        if user:
            login(req,user)
            return redirect('home:add_post')
        else:
            return HttpResponse("Invalid Credentials or Access Blocked !")
            
    else:
        return render(req,'home/login.html')

@login_required
def addPost(req):
    if req.method=='POST':
        new_post = Post(
            title=req.POST.get('title'),
            content=req.POST.get('content'),
            posted_by=req.user
        )
        new_post.save()
        return HttpResponse("Post Added Successfully !")
    else:
        return render(req,'home/add_post.html')


def index(req):
    posts = Post.objects.all()
    return render(req,'home/index.html',{'posts':posts})

def posts_by_id(req,post_id):
    posts= Post.objects.filter(id=post_id)
    return render(req,'home/index.html',{'posts':posts})

def posts_by_author(req):
    user = User.objects.get(username=req.GET['name'])
    posts= Post.objects.filter(posted_by= user)
    return render(req,'home/index.html',{'posts':posts})

def posts_archive_monthly(req):
    month=req.GET['month']
    year=req.GET['year']
    posts= Post.objects.filter(timestamp__month= month,timestamp__year=year)
    return render(req,'home/index.html',{'posts':posts})

@login_required
def contact_us(req):
    if req.method == "POST":
        #post logic
        form = ContactForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name,email,message)
            return HttpResponse("Your form submitted !")
        else:
            raise forms.ValidationError('You have to write something!')     
    else:
        form = ContactForm()
    return render(req,'home/contact.html',{'form':form})