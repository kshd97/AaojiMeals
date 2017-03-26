from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
# Create your views here.

def signin(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user == None:
			return render(request,'Login/login.djt', {'error':'Invalid Username or Password'})
		else:
			login(request,user)
			user = request.user
			U = Customer.objects.get(user=user)
			return render(request,'info/index.djt',{'user':u})
	else:
		return render(request,'Login/signin.djt',None)	

def signup(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			u = User._default_manager.get(username__iexact=username) #fix for case sensitive username
			return render(request,'Login/signup.djt',{'error':'Username already already exists!'})
		except User.DoesNotExist:	
			address = request.POST['address']
			phno = request.POST['phno']
			email = request.POST['email']
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			user = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name)
			user.set_password(password)
			user.is_active = True
			user.save()
			profileobject = Customer(user=user,address=address,phno=phno)
			profileobject.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend' #user backend error fix
			authenticate(username=username,password=password)
			login(request,user)
			return render(request, 'info/index.djt', {'user':user})
	else:
		return render(request,'Login/signup.djt',None) 

def Signout(request):
	logout(request)
	return render(request,'Login/signin.html',None)
