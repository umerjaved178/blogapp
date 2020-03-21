from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import BlogDataBase
from .forms import FormClass
# Create your views here.



def index(request):
	if not request.user.is_authenticated:
		return redirect('login_url')
	posts=BlogDataBase.objects.all()
	context={"posts":posts,"user": request.user}

	return render(request,"blogs/index.html",context)


def detail(request,id):
	
	postDetail=BlogDataBase.objects.get(pk=id)
	context={"postDetail":postDetail}

	return render(request,"blogs/detail_View.html",context)


def newForm(request):

	form=FormClass()

	if request.method=='POST':
		form=FormClass(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")

	context={"form":form}
	return render(request,"blogs/form_page.html",context)


def delete(request,id):
	post=BlogDataBase.objects.get(pk=id)

	if request.method=='POST':
		post.delete()
		return redirect("/")

	context={"post":post}

	return render(request,"blogs/delete.html",context)


def edit(request,id):
	post=BlogDataBase.objects.get(pk=id)
	form=FormClass(instance=post)

	if request.method=='POST':
		form=FormClass(request.POST,instance=post)
		if form.is_valid():
			form.save()
		return redirect(detail,id=id)

	context={"form":form}
	return render(request,"blogs/edit.html",context)




def registerView(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login_url')

	else:
		form=UserCreationForm()

	return render(request,'registration/register.html',{"form":form})










