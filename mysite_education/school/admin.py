from django.contrib import admin
from school.models import Suggestion, Student, Subject

# Register your models here.
admin.site.register(Suggestion)
admin.site.register(Student)
admin.site.register(Subject)