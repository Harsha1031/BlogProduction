from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators  import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from Blog import forms
from Blog.models import CommentModel, PosModel

# Create your views here.
@login_required
def home(request):
    name = PosModel.objects.get_queryset()
    return render(request,'home.html',{'name':name})



def index(request):
    name = PosModel.objects.get_queryset()
    return render(request,'index.html',{'name':name})

def Register(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user1=form.save()
            user1.set_password(user1.password)
            user1.save()
            return HttpResponseRedirect(reverse('login'))
    return render(request,'register.html',{'form':form,})

@login_required
def post_detail(request,pk):
    form = get_object_or_404(PosModel, pk=pk)
    name = CommentModel.objects.get_queryset().filter(pk=pk)
    return render(request,'post_detail.html',{'form':form,'name':name})
 

@login_required
def comment(request,pk):
    post = get_object_or_404(PosModel, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.post = post
            comment.save()
            print(form.cleaned_data['text'])
            return HttpResponseRedirect(reverse('home'))
    else:
        form = forms.CommentForm()
    return render(request, 'comment.html', {'form': form})

@login_required
def PostView(request):
    form = forms.PostForm()
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.author=request.user
            ins.save()
            print(ins.id)
            return HttpResponseRedirect(reverse('home'))
    return render(request,'post.html',{'form':form,'name':request.user.username})



def Login1(request):
    if request.method == "POST":
        username =request.POST.get('username')
        passw =request.POST.get('password')
        user1=authenticate(username=username,password=passw)

        if user1:
            if user1.is_active:
                login(request,user=user1)
                #print(user.get_username())
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("<h1>You are inactive.</h1>")
        else:
            return HttpResponse("<h1>username or password is wrong</h1>")
    return render(request,'login.html')

@login_required        
def LogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))