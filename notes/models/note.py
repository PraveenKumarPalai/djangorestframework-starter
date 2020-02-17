# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
import sys


class Note(models.Model):
    """
    This is for managing all the data related to note.
    title: the title of the note
    is_active: tells if entity is active or not
    """
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=255, default=None, null=True)
    text = models.CharField(max_length=255, default=None, null=True)
    last_update = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(max_length=255, default=None, null=True)

    class Meta:
        verbose_name = 'note'
        verbose_name_plural = 'note'
        app_label = 'notes'

    def __unicode__(self):
        return self.id

    objects = models.Manager()


class NoteAdmin(admin.ModelAdmin):

    list_per_page = 40

    list_display = [
        'id', 'title', 'text', 'last_update', 'is_active']
    # list_filter = ('title',)

    fieldsets = (
        (None, {'fields': ('id', 'title', 'text', 'last_update', 'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('id', 'title', 'text', 'last_update', 'is_active')}),
    )

    search_fields = ('title', 'text',)
    ordering = ['id']

    filter_horizontal = ()
