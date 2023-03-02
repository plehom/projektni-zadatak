from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import RegisterSerializer,UserSerializer,NoteSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.models import Note

# Create your views here.

class UsersAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response({"data":serializer.data})


class RegisterAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CreateNotesAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer 

    def post(self,request,*args,**kwargs):
        request.data["user"] = request.user.id
        return self.create(request, *args, **kwargs)



class GetNotesAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        queryset = Note.objects.filter(user=request.user.id)
        serializer = NoteSerializer(queryset,many=True)
        return Response({"data":serializer.data})

class GetNotesDetailAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request,pk):
        note = Note.objects.get(id=pk)
        if request.user == note.user:
            serializer = NoteSerializer(note,many=False)
            return Response({"data":serializer.data})
        else:
            return Response({"error"})

class UpdateNotesAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request,pk):
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note,data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response({"status":"error"})