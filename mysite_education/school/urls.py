from django.urls import path
from school.views import *

app_name = 'school'

urlpatterns = [
    path('', AboutView.as_view(), name='homepage'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('add-suggestion/', add_suggestion, name='add-suggestion'),
    path('event-list/', EventListView.as_view(template_name='school/events.html'), name='event-list'),

    #create event
    path('create-event/', CreateEventView.as_view(template_name='school/event_form.html',
    ), name='create-event'),

    #see event detail
    path('event-detail/<int:pk>/', EventDetailView.as_view(template_name=
    "school/event_detail.html"), name='event-detail'),

    #delete an event
    path('event/<int:pk>/remove/', EventDeleteView.as_view(
        template_name='school/event_confirm_delete.html'), name='event-remove'),

    #update
    path('event/<int:pk>/edit/', EventUpdateView.as_view(template_name=
    "school/event_form.html"), name='event-update'),

    path('enroll-your-child/', enroll_child, name='enroll-your-child'),
    path('add-subject/', add_subject, name='add-subject'),
    path('subjects-offered/', NPSubjectListView.as_view(), name='subjects-offered'),
]
