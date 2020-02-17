from django.contrib import admin

from notes.models import Note
from notes.models import NoteAdmin


# Register your models here.

# Organisation

admin.site.register(Note, NoteAdmin)