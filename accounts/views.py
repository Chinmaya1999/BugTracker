from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
	return render(request,'accounts/dashboard.html')

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=CreateUserForm()
		if request.method == 'POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user=form.cleaned_data.get('username')
				messages.success(request,'Account was created for '+user)
				return redirect('login')

		context={'form':form}
		return render(request,'accounts/registration.html',context)
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username=request.POST.get('username')
			password=request.POST.get('password')

			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'username or password is incorrect')
		context={}
		return render(request,'accounts/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')	
def addProject(request):

	if request.method == 'POST':
		projectName=request.POST.get('project_name')
		projectType=request.POST.get('project_type')
		manager=request.POST.get('manager')
		frontend=request.POST.get('frontend')
		backend=request.POST.get('backend')
		client=request.POST.get('client')
		description=request.POST.get('description')
		startDate=request.POST.get('startDate')
		dueDate=request.POST.get('dueDate')
		project_info=Projects(name=projectName,ProjectType=projectType,manager=manager,frontend=frontend,backend=backend,client_name=client,Description=description,start_date=startDate,due_date=dueDate)
		project_info.save()
		return redirect('home')


	return render(request,'accounts/addNewProject.html')

@login_required(login_url='login')
def projectReport(request):
	projects=Projects.objects.all()
	
	return render(request,'accounts/projectReport.html',{'projects':projects})

@login_required(login_url='login')
def updateProject(request,pk):
	project=Projects.objects.get(id=pk)
	form=ProjectsForm(instance=project)
	context={'form':form}
	if request.method == 'POST':
		form=ProjectsForm(request.POST,instance=project)
		if form.is_valid():
			form.save()
			return redirect('projectReport')
	return render(request,'accounts/updateProject.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
	project=Projects.objects.get(id=pk)
	context={'project':project}
	if request.method == 'POST':
		project.delete()
		return redirect('projectReport')
	return render(request,'accounts/deleteProject.html',context)
@login_required(login_url='login')	
def addBug(request,pk):
	context={}
	if request.method == 'POST':
		project=Projects.objects.get(id=pk)
		context={'project':project}
		bug_name=request.POST.get('bug_name')
		bug_description=request.POST.get('bug_description')
		priority=request.POST.get('priority')
		bug_info=ProjectBug(name=bug_name,project=project,bug_description=bug_description,priority=priority)
		bug_info.save()
		return redirect('projectReport')
	return render(request,'accounts/addBug.html',context)

@login_required(login_url='login')
def bugReport(request,pk):
	bugs=ProjectBug.objects.filter(project_id=pk)
	context={'bugs':bugs}
	return render(request,'accounts/bugReport.html',context)
@login_required(login_url='login')
def updateBug(request,pk):
	bug=ProjectBug.objects.get(id=pk)
	bugs=ProjectBug.objects.filter(project_id=pk)
	form=ProjectBugForm(instance=bug)
	context={'form':form}
	context1={'bugs':bugs}
	if request.method == 'POST':
		form=ProjectBugForm(request.POST,instance=bug)
		if form.is_valid():
			form.save()
			return redirect('projectReport')
	return render(request,'accounts/updateBug.html',context)

@login_required(login_url='login')
def deleteBug(request,pk):
	bug=ProjectBug.objects.get(id=pk)
	bugs=ProjectBug.objects.filter(project_id=pk)
	context={'bug':bug}
	if request.method == 'POST':
		bug.delete()
		return redirect('projectReport')
	return render(request,'accounts/deleteBug.html',context)

def userPage(request):
	context={}
	return render(request, 'accounts/user.html')
    
# Create your views here.
