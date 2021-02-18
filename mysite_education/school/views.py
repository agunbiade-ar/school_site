from django.views.generic import (
	TemplateView, CreateView, ListView)

from school.models import Suggestion, Subject
from school.forms import SuggestionForm, StudentForm, SubjectForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
class AboutView(TemplateView):
	template_name = 'home-page.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

class NPSubjectListView(ListView):
	template_name = 'subjects-offered.html'
	model = Subject

	def get_queryset(self):
		return Subject.objects.filter(subject_category='N&P')	

	def get_context_data(self, *args, **kwargs):
		context = super(NPSubjectListView, self).get_context_data(*args, **kwargs)
		context['jsubject_category'] = Subject.objects.filter(subject_category='JSS')
		context['ssubject_category'] = Subject.objects.filter(subject_category='SSS')
		return context



def add_suggestion(request):
	if request.method == 'POST':
		form = SuggestionForm(request.POST)
		if form.is_valid():
			suggestion = form.save(commit=False)
			suggestion.save()
			return redirect('school:homepage')
	else:
		form = SuggestionForm()
	return render(request, 'school/add_suggestion.html', {'form': form})


def enroll_child(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.save()
			messages.success(request, "Child application submitted successfully, Thank you!" )
			return redirect('school:homepage')
	else:
		form = StudentForm()
	return render(request, 'school/enroll-child.html', {'form': form})


def add_subject(request):
	if request.method == 'POST':
		form = SubjectForm(request.POST)
		if form.is_valid():
			subject = form.save(commit=False)
			subject.save()
			messages.success(request, "Subject added successfully!" )
			return redirect('school:add-subject')
		else:
			messages.error(request, "Please, check your input and try again!")			
	else:
		form = SubjectForm()
	return render(request, 'school/add-subject.html', {'form': form})
