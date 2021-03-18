from django import forms
from django.db import models
from school.models import Suggestion, Student, Subject, Events
from django.forms import Textarea

class SuggestionForm(forms.ModelForm):

	class Meta():
		model = Suggestion
		fields = ('name', 'phone_number', 'suggestion_text')


class StudentForm(forms.ModelForm):

	class Meta():
		model = Student
		fields = ('student_first_name', 'student_last_name', 'student_dob', 'student_pic',
		 'class_choices','address', 'parent_name','phone_number_1', 'phone_number_2', 'genotype',
		 'medical_condition')

		widgets= {
		'address': Textarea(attrs={'cols':30, 'rows': 3}),
		'medical_condition': Textarea(attrs={'cols':30, 'rows': 3}),
		}

class SubjectForm(forms.ModelForm):

	class Meta():
		model = Subject
		fields = ('subject_title', 'subject_category')

class EventForm(forms.ModelForm):

	class Meta():
		model = Events
		fields = ('title', 'description', 'event_date')

		widgets= {
		'description': Textarea(attrs={'cols':30, 'rows': 3}),
		}
