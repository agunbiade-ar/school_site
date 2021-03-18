from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from PIL import Image
from django.urls import reverse

GENOTYPE_CHOICES = (
    ('AA', 'AA'),
    ('AS', 'AS'),
    ('SS', 'SS'),
)

CLASS_CHOICES = (
    ('KD', 'Kindergaten'),
    ('PN', 'Pre-Nursery'),
    ('NU', 'Nursery'),
    ('PR', 'Primary'),
    ('JSS', 'Junior'),
    ('SSS', 'Senior'),
)

SUBJECT_CATEGORY_CHOICES = (
    ('N&P', 'Nursery & Primary'),
    ('JSS', 'Junior'),
    ('SSS', 'Senior'),
)

# Create your models here.
class Suggestion(models.Model):
	phone_regex = RegexValidator(regex=r'^\d{11}$', message="Phone number must be entered in the format: '99999999999'. Up to 11 digits allowed.")
	name = models.CharField(max_length=200)
	phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
	suggestion_text = models.TextField()
	published_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Student(models.Model):
	student_first_name=models.CharField(max_length=200)
	student_last_name=models.CharField(max_length=200)
	student_dob = models.DateField(help_text='Please enter in the format yyyy-mm-dd')
	student_pic = models.ImageField(default = 'placeholder.jpg', upload_to = 'student_pic')
	class_choices = models.CharField(choices=CLASS_CHOICES, max_length=15, default='Kindergaten', 
		help_text='Please click on this to select the class you are applying for')
	address = models.TextField()
	parent_name = models.CharField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\d{11}$', message="Phone number must be entered in the format: '99999999999'. Up to 11 digits allowed.")
	phone_number_1 = models.CharField(validators=[phone_regex], max_length=11, blank=True)
	phone_number_2 = models.CharField(validators=[phone_regex], max_length=11, blank=True)
	genotype = models.CharField(choices=GENOTYPE_CHOICES, max_length=3, default='AA',
		help_text='Please click on this to select the Genotype of your child')
	medical_condition = models.TextField()

	def __str__(self):
		return self.student_first_name

class Subject(models.Model):
	subject_title = models.CharField(max_length=200)
	subject_category = models.CharField(choices=SUBJECT_CATEGORY_CHOICES, max_length=20, default='Nursery & Primary',
		help_text='Please click on this to select the category the subject falls under')

	def __str__(self):
		return self.subject_title

class Events(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	event_date = models.DateTimeField(default=timezone.now)

	class Meta:
		verbose_name_plural = 'Events'

	def get_absolute_url(self):
		return reverse("school:event-detail", kwargs={'pk':self.pk })

	def __str__(self):
		return self.title