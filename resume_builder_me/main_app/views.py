from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Resume, Project, Gpa
from .forms import ResumeForm, ProjectFormSet, GpaFormSet



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
	return render(request, 'logout.html')

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
		formset_project = ProjectFormSet(instance=Resume())
		formset_gpa = GpaFormSet(instance=Resume())
		if request.method == "POST":
			form = ResumeForm(request.POST)
			formset_project = ProjectFormSet(request.POST,request.FILES,instance=resume)
				#if formset_project.is_valid():
			formset_gpa = GpaFormSet(request.POST, request.FILES,instance=resume)
			if formset_gpa.is_valid() and formset_project.is_valid():
				
				
				if form.is_valid():
					  formset_gpa.save()
					  formset_project.save()
					  resume = form.save()
					  return HttpResponse("Your resume was saved")


				return render(request, 'new_resume.html', {'form' : form, 'formset_project' : formset_project, 'formset_gpa': formset_gpa})	  
		return render(request, 'new_resume.html', {'form' : form, 'formset_project' : formset_project, 'formset_gpa': formset_gpa})
			
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
