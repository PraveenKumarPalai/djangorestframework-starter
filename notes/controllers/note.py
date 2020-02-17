from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from notes.models import (
    Note
)
from notes.serializers import (
    NoteSerializer
)
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


# ViewSets define the view behavior.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CreateNote(APIView):

    def post(self, request):
        note_serializer = NoteSerializer(data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data, status=status.HTTP_201_CREATED)
        return Response(note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notes = Note.objects.all()
        note_serializer = NoteSerializer(notes, many=True)
        return Response(note_serializer.data, status=status.HTTP_201_CREATED)
