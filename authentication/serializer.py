from rest_framework import serializers, exceptions
from . import models 

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=128)
    first_name = serializers.CharField(min_length=3, max_length=250,
                                       required=False)
    last_name = serializers.CharField(min_length=3, max_length=250,
                                      required=False)

    class Meta:
        model = models.User
        fields = [
            'username', 'email'
            'password'
        ]

    def validate(self, attrs):
        if (
            (attrs.get('password') is None) or ((attrs.get('email') is None))
        ):
            raise exceptions.NotAcceptable("Email mismatching")
        return True

    def create(self, validated_data):
        user = models.User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class BookSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    publish_date = serializers.DateTimeField()
    book_owner = serializers.CharField()


class UserProfileSerializer(serializers.Serializer):
    user_role = serializers.CharField()
    user_department = serializers.CharField()
    employee = serializers.CharField()

class LibrarySerializer(serializers.Serializer):
    library_name = serializers.CharField()    
    # members = serializers.CharField()
    