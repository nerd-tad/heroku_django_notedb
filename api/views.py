from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from api.models import Notes
from .serializers import NoteSerializer
from api import serializers

# Create your views here.
@api_view(['GET']) #LIST OF METHODS
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/note/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single object'
        },
        {
            'Endpoint': '/notes/create',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'creates a note with data sent in a post request'
        },
        {
            'Endpoint': '/notes/id/update',
            'method': 'POST',
            'body': {'body': ''},
            'description': 'updates a note with data sent in a post request'
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'deletes an existing node'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Notes.objects.all()  #they all are python objects. gotta turn them into json objects, serializer does that
    serializer  = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk): #pk is primary key(or id of a each element)
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data #with post requests, request contains data
    note = Notes.objects.create(
        body = data.get('body')
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data #with post requests, request contains data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Notes.objects.get(id = pk)
    note.delete()
    return Response('Note deleted successfully')