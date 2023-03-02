from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','password']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email','password']
    
    def create(self,data):
        user = User.objects.create(
            username=data["username"],
            first_name = data["first_name"],
            last_name = data["last_name"],
            email = data["email"]
        )
        user.set_password(data["password"])
        user.save()
        return User

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__" 