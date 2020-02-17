# users/urls.py
 
from django.conf.urls import url
from notes.views import CreateNote

urlpatterns = [
    url(r'^$', CreateNote.as_view()),
]