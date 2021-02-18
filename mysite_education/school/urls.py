from django.urls import path
from school.views import *

app_name = 'school'

urlpatterns = [
    path('', AboutView.as_view(), name='homepage'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add-suggestion', add_suggestion, name='add-suggestion'),
    path('enroll-your-child', enroll_child, name='enroll-your-child'),
    path('add-subject', add_subject, name='add-subject'),
    path('subjects-offered', NPSubjectListView.as_view(), name='subjects-offered'),
]
