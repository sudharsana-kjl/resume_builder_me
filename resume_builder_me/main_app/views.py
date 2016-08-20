from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Resume, Project
from .forms import ResumeForm, ProjectFormSet



def index(request):
	return render(request, 'index.html')


def signin(request):
	if request.method == "POST":
		roll_no = request.POST.get("roll_no")
		password = request.POST.get("pass")
		user = authenticate(username = roll_no, password = password)
		if user != None:
			login(request, user)
			return render(request, 'success.html')
		else:
			return render(request, 'signin.html', 
				{'error' : "Invalid credentials or webmail is down. Please try again."})
	return render(request, 'signin.html')

def logout_view(request):
	if request.user.is_authenticated():
		logout(request)
	return HttpResponse("You are logged out")

def about(request):
	return render(request, 'about.html')

def my_resume(request):
	if request.user.is_authenticated:
		resume = Resume.objects.filter(user = request.user)
		print(resume)
		if len(resume) != 0:
			result = {'status' : True, 'resume' : resume[0]}
		else:
			result = {'status' : False}
		return render(request, 'my_resume.html', {'r' : result})
	return HttpResponse("Not valid")

def new_resume(request):
	if request.user.is_authenticated:
		form = ResumeForm()
		formset = ProjectFormSet(instance=Resume())
		if request.method == "POST":
			form = ResumeForm(request.POST)
			if form.is_valid():
				resume = form.save()
				formset = ProjectFormSet(request.POST,request.FILES,instance=resume)
				if formset.is_valid():
					formset.save()
					return HttpResponse("Your resume was saved")
		return render(request, 'new_resume.html', {'form' : form, 'formset' : formset})
			
	return HttpResponse("Not valid")

def edit_resume(request):
	if request.user.is_authenticated:
		resume = get_object_or_404(Resume, user = request.user)
		resume_form = ResumeForm(instance = resume)
		if request.method == "POST":
			resume_form = ResumeForm(request.POST, instance = resume)
			if resume_form.is_valid():
				resume.save()
				return HttpResponse("Your resume was edited successfully")
		return render(request, 'edit_resume.html', {'form': resume_form})
	return HttpResponse("Not valid")

def delete_resume(request):
	return HttpResponse("Yet to implement")
